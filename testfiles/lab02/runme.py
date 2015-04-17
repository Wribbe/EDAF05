#!/bin/python2.7

import sys

def main():

    lines = load_data(sys.argv[1])
    sorted_words = sort_by_smallest_letter(lines)
    root = get_letter_nodes(sorted_words)
#    for line in lines:
#        words = get_next_words(line, root)
#        print "{} : {}".format(line, words)
#    print_nodes(root)
    words = get_next_words("never", root)
    print words

def get_letter_nodes(tuples):
    root = Node("root")
    for letters, word in tuples:
        current_node = root
        sub_letters = []
        for letters in sub_letters:
            for letter in letters:
                next_node = current_node.get(letter)
                if not next_node:
                    next_node = current_node.add_child(Node(letter))
                current_node = next_node
            current_node.word.append(word)
    return root

def print_nodes(root):
    queue = [root]
    while len(queue) > 0:
        node = queue.pop(0)
        print "{}".format(node.name),
        word = node.word
        if word:
            print word,
        for child_name, child_node in node.child_nodes.iteritems():
            queue.append(child_node)

def get_next_words(letters, current_node):
    word = letters
    words = []
    current_path = []
    letters = sorted(letters[1:])
    get_next_words_sub(letters, current_node, words, current_path, 0)
    try:
        words.remove(word)
    except:
        pass
    return words

def get_next_words_sub(letters, current_node, words, current_path, faults):
    if len(letters) == 0 or faults > 1 or current_node.seen:
#        for node in current_node.child_nodes.values():
#            if node.word:
#                words.extend(node.word)
        return
    current_node.seen = "true"
    child_node = current_node.child_nodes.get(letters[0])
    if child_node:
        if child_node.word:
            words.extend(child_node.word)
            return
        current_path.append(child_node)
        get_next_words_sub(letters[1:], child_node, words, current_path, faults)
    for child_node in current_node.child_nodes.values():
        get_next_words_sub(letters, child_node, words, current_path, faults+1)
    current_node.seen = ""
    for child_node in current_node.child_nodes.values():
        child_node.seent = ""


class Node(object):

    def __init__(self, name):
        self.word = []
        self.child_nodes = {}
        self.name = name
        self.seen = ""

    def get(self, node_name):
        return self.child_nodes.get(node_name)

    def add_child(self, Node):
        self.child_nodes[Node.name] = Node
        return Node

def sort_by_smallest_letter(words):
    tuples = []
    sorted_letters = [sorted(x) for x in words]
    for letters, words in zip(sorted_letters, words):
        tuples.append((letters, words))
    return sorted(tuples)

def load_data(filename):
    stripped = []
    input_lines = open(filename).readlines()
    for line in input_lines:
        stripped.append(line.strip())
    return stripped

if __name__ == "__main__":
    main()

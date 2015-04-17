#!/bin/python2.7

import sys

def main():
    lines = [x.strip() for x in open(sys.argv[1]).readlines()]
    tuples = []
    for line in lines:
        tuples.append(get_subwords(line))
    root = Node("root")
    for tuple in tuples:
        list, word = tuple
        if word == "every":
            print list
    for sub_words, word in tuples:
        for sub_letter_list in sub_words:
            make_nodes(root, sub_letter_list, word)
    get_words(root, "never")

def get_words(root, word):
    word = sorted(word[1:])
    print word
    for letter in word:
        current_node = root.children.get(letter)
        print current_node.name

def make_nodes(root, letters, word):
    current_node = root
    for letter in letters:
        child = current_node.children.get(letter)
        if word == "every":
            print letter
        print child
        if child:
            current_node = child
        else:
            current_node = current_node.append(letter)
    current_node.words.append(word)
    if word == "every":
        print current_node.name

class Node(object):
    
    def __init__(self, name):
        self.children = {}
        self.name = name
        self.words = []

    def append(self, name):
        child = Node(name)
        self.children[name] = child
        return child

def get_subwords(word):
    original_word = word
    word = list(word)
    subwords = []
    for letter in word:
        temp_word = list(word)
        temp_word.remove(letter)
        subwords.append(sorted(temp_word))
    return (subwords, original_word)

if __name__ == "__main__":
    main()

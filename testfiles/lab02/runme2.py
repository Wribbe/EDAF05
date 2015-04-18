import sys

def main():
    lines = [x.strip() for x in open(sys.argv[1]).readlines()]
    tuples = []
    for line in lines:
        tuples.append(get_subwords(line))
    root = Node("root")
    for sub_words, word in tuples:
        for sub_letter_list in sub_words:
            make_nodes(root, sub_letter_list, word)

    nodes = {}
    children = {}
    for node_name in lines:
        current_node = nodes.get(node_name)
        children_list = get_children(root, node_name)
        if current_node == None:
            new_node = Node(node_name)
            nodes[node_name] = new_node
            current_node = new_node
        for child_name in children_list:
            child = nodes.get(child_name)
            if child:
                current_node.children[child_name] = child
            else:
                new_child = Node(child_name)
                current_node.children[child_name] = new_child
                nodes[child_name] = new_child

    compare_lines = [x.strip() for x in open(sys.argv[2]).readlines()]
    for line in compare_lines:
        reset_nodes(nodes.values())
        from_word, to_word = line.split()
        find_path_in_nodes(from_word, to_word, nodes)

def reset_nodes(nodes):
    for node in nodes:
        node.visited = ""

def find_path_in_nodes(from_word, to_word, nodes):
    queue = [nodes[from_word]]
    next_items = []
    depth = 0
    while len(queue) > 0:
        current_node = queue.pop(0)
        if current_node.name == to_word:
            print "Found path from {} to {} with depth {}.".format(from_word, to_word, depth)
            return
        if not current_node.visited:
            next_items.extend(current_node.children.values())
            current_node.visited = "visited"
        if len(queue) == 0:
            queue.extend(next_items)
            next_items = []
            depth += 1

def get_children(root, word):
    current_node = root
    original_word = word
    word = sorted(word[1:])
    for letter in word:
        current_node = current_node.children.get(letter)
    words = list(current_node.words)
    try:
        words.remove(original_word)
    except:
        pass
    return words

def make_nodes(root, letters, word):
    current_node = root
    for letter in letters:
        child = current_node.children.get(letter)
        if child:
            current_node = child
        else:
            current_node = current_node.append(letter)
    if not word in current_node.words:
        current_node.words.append(word)

class Node(object):

    def __init__(self, name):
        self.children = {}
        self.name = name
        self.words = []
        self.visited = ""

    def append(self, name):
        child = Node(name)
        self.children[name] = child
        return child

def get_subwords(word):
    original_word = word
    word = sorted(word)

    subwords = []
    for letter in word:
        temp_word = list(word)
        temp_word.remove(letter)
        subwords.append(temp_word)
    return (subwords, original_word)

def print_nodes(root):
    queue = [root]
    next_queue = []
    while len(queue) > 0:
        current_node = queue.pop(0)
        print current_node.name,
        for node in current_node.children.values():
            next_queue.append(node)
        if len(queue) == 0:
            queue.extend(next_queue)
            next_queue = []
            print

if __name__ == "__main__":
    main()

import sys

def main():

    # Get and massage input.
    lines = [x.strip() for x in open(sys.argv[1]).readlines()]

    # Create and store tuples of ([sub_words], word).
    tuples = []
    for line in lines:
        tuples.append(get_subwords(line))

    # Create association node structure based on sublists with root as base.
    root = Node("root")
    for sub_words, word in tuples:
        for sub_letter_list in sub_words:
            make_nodes(root, sub_letter_list, word)

    # Get path test input from input file.
    paths = []
    compare_lines = [x.strip() for x in open(sys.argv[2]).readlines()]
    for line in compare_lines:
        from_word, to_word = line.split()
        depth, path = find_path_with_subword_tree(from_word, to_word, root)
        print depth
        if path: 
            paths.append(path)
    sys.stderr.write("\n".join(paths))

def reset_nodes(nodes):
    for node in nodes:
        node.visited = ""

def find_path_with_subword_tree(from_word, to_word, tree_root):

    queue = [[from_word]]
    next_queue = []
    visited = {}
    depth = 0
    while queue:
        current_path = queue.pop(0)
        current_word = current_path[-1]
        if current_word == to_word:
            return (depth, " --> ".join(current_path))
        if not visited.get(current_word):
            children = get_children(tree_root, current_word)
            for child in children:
                if not visited.get(child):
                    new_path = list(current_path)
                    new_path.append(child)
                    next_queue.append(new_path)
            visited[current_word] = True
        if not queue:
            queue.extend(next_queue)
            next_queue = []
            depth += 1
    return (-1, "")

def get_children(root, word):
    current_node = root
    original_word = word
    word = sorted(word[1:])
    for letter in word:
        current_node = current_node.children.get(letter)
    words = list(current_node.words)
    words.remove(original_word)
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
        self.parent = ""

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

if __name__ == "__main__":
    main()

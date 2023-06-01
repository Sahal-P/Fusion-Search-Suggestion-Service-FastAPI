class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.is_end_of_word = True

    def search(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]
        return current.is_end_of_word

    def starts_with(self, prefix):
        current = self.root
        for char in prefix:
            if char not in current.children:
                return []
            current = current.children[char]

        return self._collect_words(current, prefix)

    def _collect_words(self, node, prefix):
        words = []
        if node.is_end_of_word:
            words.append(prefix)

        for char, child in node.children.items():
            words.extend(self._collect_words(child, prefix + char))

        return words


# Example usage:
trie = Trie()
trie.insert("apple")
trie.insert("appleuuu")
trie.insert("applekkkkkkkk")
trie.insert("apple0000000000")
trie.insert("banana")
trie.insert("orange")

print(trie.search("apple"))  # Output: True
print(trie.search("grape"))  # Output: False

print(trie.starts_with("app"))  # Output: ['apple']
print(trie.starts_with("ban"))  # Output: ['banana']
print(trie.starts_with("ora"))  # Output: ['orange']
print(trie.starts_with("gr"))   # Output: []
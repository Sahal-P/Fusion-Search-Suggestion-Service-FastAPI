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
        
        def get_words(node, prefix):
            words = []
            if node.is_end_of_word:
                words.append(prefix)
            
            for char, child_node in node.children.items():
                words.extend(get_words(child_node, prefix + char))
            
            return words
        
        return get_words(current, prefix)


# Example usage:
trie = Trie()
trie.insert("apple")
trie.insert("appleuo")
trie.insert("apphdudjd")
trie.insert("apploeieuehej")
trie.insert("banana")
trie.insert("orange")

print(trie.search("apple"))  # Output: True
print(trie.search("grape"))  # Output: False

print(trie.starts_with("app"))  # Output: ['apple']
print(trie.starts_with("ban"))  # Output: ['banana']
print(trie.starts_with("ora"))  # Output: ['orange']
print(trie.starts_with("gr"))   # Output: []


# from pygtrie import Trie

# # Create a Trie instance
# trie = Trie()

# # Insert words into the Trie
# trie["apple"] = True
# trie["banana"] = True
# trie["orange"] = True

# # Search for words in the Trie
# print("apple" in trie)  # Output: True
# print("grape" in trie)  # Output: False

# # Get a list of words starting with a prefix
# print(trie.keys("app"))  # Output: ['apple']
# print(trie.keys("ban"))  # Output: ['banana']
# print(trie.keys("ora"))  # Output: ['orange']
# print(trie.keys("gr"))   # Output: []
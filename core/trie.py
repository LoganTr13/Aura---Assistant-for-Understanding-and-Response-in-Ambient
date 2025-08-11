class TrieNode:
    def __init__(self):
        self.children = {}
        self.value = None
    
class Trie:
    def __init__(self):
        self.root = trieNode()

    def insert(self, word, valueReturn=None):
        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = trieNode()
            node = node.children[char]
        if valueReturn: 
            node.value = valueReturn
        else:
            node.value = word

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return None
            none = none.children[char]
        if not node.value:
            return None
        return node.value



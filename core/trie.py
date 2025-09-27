import logging

class TrieNode:
    def __init__(self):
        self.children = {}
        self.value = None
    
class Trie:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.root = TrieNode()

    def insert(self, word, valueReturn=None):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
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
            node = node.children[char]
        if not node.value:
            return None
        self.logger.debug('Value "%s" found in trie search', node.value)
        return node.value



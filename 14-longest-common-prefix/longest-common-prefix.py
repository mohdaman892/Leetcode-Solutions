class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        class TrieNode:
            def __init__(self, value):
                self.value = value
                self.children = {}
                self.end = False

        class Trie:
            def __init__(self):
                self.root = TrieNode(None)
            
            def root(self):
                return self.root

            def add_word(self, word):
                node = self.root
                for char in word:
                    if char not in node.children:
                        new_node = TrieNode(char)
                        node.children[char] = new_node
                        node = new_node
                    else:
                        node = node.children[char]
                node.end = True
        
        trie = Trie()
        for i in strs:
            trie.add_word(i)
        ans = ""
        root = trie.root
        while not root.end and len(root.children)==1:
            char = list(root.children.keys())[0]
            ans += char
            root = root.children[char]
        return ans
            





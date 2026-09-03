#trie has multiple children
# one character
# string retrieval/ autocomplete

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class PrefixTree:
    
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        #split and put itß
        # cat c a t ,
        # find c a t 
        # fin

        node = self.root

        for char in word : 
            if char not in node.children :
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True

    def search(self, word: str) -> bool:
            node = self.root

            for char in word:
                if char not in node.children:
                    return False
                else:
                    node = node.children[char]
            return node.is_end


    def startsWith(self, prefix: str) -> bool:
        node = self.root

        for char in prefix:
            if char not in node.children:
                return False

            else:
                node = node.children[char]
        # if there is a path get true
        return True









        
        
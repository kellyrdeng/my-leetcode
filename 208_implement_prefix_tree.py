class Trie:

    def __init__(self):
        self.root = TrieNode(None, False)

    def insert(self, word: str) -> None:
        self.insertHelper(word, self.root)

    def insertHelper(self, word, node):
        #base cases:
        if len(word) == 0: #done with word
            return
        if len(word) == 1: 
            if word not in node.children: #doesn't exist, so add it
                new_node = TrieNode(word[0], True)
                node.children[word[0]] = new_node
            else: #already exists, just change isWord to True
                node.children[word].isWord = True
            return
        
        if word[0] not in node.children: #add it
            new_node = TrieNode(word[0], False)
            node.children[word[0]] = new_node
        
        #continue recursion
        self.insertHelper(word[1:], node.children[word[0]])

    def search(self, word: str) -> bool:
        return self.searchHelper(word, self.root)

    def searchHelper(self, word, node):
        #base case:
        if len(word) == 1 and word in node.children:
            return node.children[word].isWord

        if word[0] not in node.children:
            return False
        else: #found cur char AND there's more chars left
            return self.searchHelper(word[1:], node.children[word[0]])
        
    def startsWith(self, prefix: str) -> bool: #TODO
        return self.startsWithHelper(prefix, self.root)

    def startsWithHelper(self, prefix, node):
        #base case:
        if len(prefix) == 1 and prefix in node.children:
            return True

        if prefix[0] not in node.children:
            return False
        else: #found cur char AND there's more chars left
            return self.startsWithHelper(prefix[1:], node.children[prefix[0]])

class TrieNode:

    def __init__(self, val, isWord):
        self.val = val #char
        self.children = {} #dict of child nodes where val -> child node
        self.isWord = isWord
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

class Node:
    def __init__(self):
        self.child = {}
        self.word = False

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.child:
                curr.child[c] = Node()
            curr = curr.child[c]
        curr.word = True
        return None
        

    def search(self, word: str) -> bool:

        def dfs (index, node):
            if index == len(word):
                return node.word
            c = word[index]

            if c == '.':
                for key in node.child.keys():
                    if dfs(index+1, node.child[key]):
                        return True
                return False
            if c not in node.child:
                    return False
            
            return dfs(index+1, node.child[c])
        
        return dfs(0, self.root)

                    
        

class Trie:
    def __init__(self):
        self.trie = {}
    
    def insert(self,word: str) -> None:
        d = self.trie
        for c in word:
            if c not in d:
                d[c] = {}
            d = d[c]
        d['.'] = '.'
    
    def search(self, word: str) -> bool:
        d = self.trie
        for c in word:
            if c not in d:
                return False
            d = d[c]
        return '.' in d
    
    def startsWith(self,prefix: str) -> bool:
        d = self.trie
        for c in prefix:
            if c not in d:
                return False
            d = d[c]
        return True

def runTrie(operations, arguments):
    output = []
    trie = None

    for op, arg in zip(operations, arguments):
        if op == "Trie":
            trie = Trie()
            output.append(None)

        elif op == "insert":
            trie.insert(arg[0])
            output.append(None)

        elif op == "search":
            output.append(trie.search(arg[0]))

        elif op == "startsWith":
            output.append(trie.startsWith(arg[0]))

    return output

ops = ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
args = [
    [],
    ["apple"],
    ["apple"],
    ["app"],
    ["app"],
    ["app"],
    ["app"]
]

print(runTrie(ops, args))

"""
code sample:\n
    words = ["hello", "world", "how", "are", "you", "heck"] \n
tree = SearchTree(words)\n
print(tree.firstNThatStartWith(3, "h")) #-> ['how', 'heck', 'hello']\n
"""


from collections import defaultdict


inifiniteDict = lambda: defaultdict(inifiniteDict)

class ValueTree:
    """
    methods:
    """
    def insert(self, word):
        node = self.root
        for letter in word:
            node = node[letter]
        node['word'] = word

    

    def insertWithValue(self, word, value):
        self.wordCount += 1
        node = self.root
        for letter in word:
            node = node[letter]
        node['word'] = word
        node['value'] = value

        return self.wordCount


    def insertDict(self, wordsToValueDictionary: dict):
        """inserts a dictionary of words to values"""
        for word, value in wordsToValueDictionary.items():
            self.insertWithValue(word, value)

    def __init__(self, wordsToValueDictionary={}):
        self.root = inifiniteDict()
        self.wordCount = 0
        for word, value in wordsToValueDictionary.items():
            self.insertWithValue(word, value)

    def getValue(self, word):
        node = self.root
        for letter in word:
            if letter not in node:
                return None
            node = node[letter]
        return node['value']
        
    def valueSearch(self, n: int, letters) -> dict|bool:
        """
        param: n - the number of words you want to return

        
        code sample:
        print(tree.firstNThatStartWith(2, "h")) -> {'how': value, 'hey': value}
        """
        node = self.root
        for letter in letters:
            if letter not in node:
                continue
                # return False
            node = node[letter]

        que = [node]
        valuesCollected = {}

        while len(que) > 0:
            node = que.pop(0)
            if 'value' in node:
                key = node['word']
                value = node['value']
                valuesCollected[key] = value
                if len(valuesCollected) >= n:
                    return valuesCollected
            for letter in node:
                if letter != 'word' and letter != 'value':
                    que.append(node[letter])

        return valuesCollected
# your code goes here!

class Anagram:
    def __init__(self, word):
        self.word = word
    
    def match(self, words):
        matches = []
        for w in words:
            if sorted(w.lower()) == sorted(self.word.lower()) and w.lower() != self.word.lower():
                matches.append(w)
        return matches
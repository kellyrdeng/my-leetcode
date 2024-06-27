class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        dict1, dict2 = self.string_to_dict(word1), self.string_to_dict(word2)
        freq1, freq2 = list(dict1.values()), list(dict2.values())
        freq1.sort()
        freq2.sort()

        return set(dict1.keys()) == set(dict2.keys()) and freq1.sort() == freq2.sort()

    def string_to_dict(self, word): #returns dictionary with char -> freq
        d = {}

        for c in word:
            d[c] = d.get(c, 0) + 1

        return d

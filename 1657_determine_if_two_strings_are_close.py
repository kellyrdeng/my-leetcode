class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        #check if they have the same letters
        if set(word1) != set(word2):
            return False

        #check if they have the same frequency of frequencies
        list1, list2 = self.string_to_list(word1), self.string_to_list(word2)
        list1.sort()
        list2.sort()
        return list1 == list2

    def string_to_list(self, word):
        list_representation = [0] * 26

        for c in word:
            i = ord(c) - 97
            list_representation[i] += 1
        
        return list_representation

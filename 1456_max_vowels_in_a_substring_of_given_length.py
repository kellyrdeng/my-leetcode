class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        substr = s[:k] #first substring
        max_vowels = 0

        for char in substr:
            if char in vowels:
                max_vowels += 1

        count = max_vowels #count vowels in each substring
        for i in range(k, len(s)):
            removed = s[i - k]
            added = s[i]

            if removed in vowels:
                count -= 1
            if added in vowels:
                count += 1

            max_vowels = max(count, max_vowels)
        
        return max_vowels

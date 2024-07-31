class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ('a', 'e', 'i', 'o', 'u')
        l, r = 0, len(s) - 1
        res = [x for x in s]

        while l < r:
            if s[l].lower() not in vowels:
                l += 1
                continue
            if s[r].lower() not in vowels:
                r -= 1
                continue

            res[l], res[r] = res[r], res[l]
            l, r = l + 1, r - 1
            
        return ''.join(res)

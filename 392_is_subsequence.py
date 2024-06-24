class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        #return if s is a subsequence of t
        if len(s) == 0:
            return True
        if len(s) > len(t):
            return False

        i = 0 #index of s
        for char in t:
            if i <= len(s) -1 and s[i] == char:
                i += 1
        
        return i == len(s)

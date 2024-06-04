class Solution:
    """ def partition(self, s: str) -> List[List[str]]:
        res = []
        self.backtrack(res, s, 0, [])
        return res
    
    def backtrack(self, res, s, start, current_partition):
        if start == len(s):
            if all(self.is_palindrome(part) for part in current_partition):  # check if each part is a palindrom
                res.append(current_partition.copy())
            return
        for end in range(start + 1, len(s) + 1):
            current_partition.append(s[start:end])
            self.backtrack(res, s, end, current_partition)
            current_partition.pop()
        
    def is_palindrome(self, s):
        return s == s[::-1] """

    def partition(self, s: str):
        if not s:
            return [[]]
        
        ans = []
        for i in range(1, len(s) + 1):
            if s[:i] == s[:i][::-1]:  # prefix is a palindrome
                for suf in self.partition(s[i:]):  # process suffix recursively
                    ans.append([s[:i]] + suf)
        
        return ans

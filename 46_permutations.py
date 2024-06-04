class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.backtrack(res, nums, [])
        return res
    
    def backtrack(self, res, nums, current_perm):
        if len(current_perm) == len(nums):
            res.append(current_perm.copy())
            return
        for num in nums:
            if num not in current_perm:
                current_perm.append(num)
                self.backtrack(res, nums, current_perm)
                current_perm.remove(num)

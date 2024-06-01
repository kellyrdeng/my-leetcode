class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        expected = range(0, len(nums) + 1)
        expected_sum = sum(expected)
        return expected_sum - sum(nums)

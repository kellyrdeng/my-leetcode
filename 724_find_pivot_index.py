class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix = [0] #prefix[i] contains the sum of everything to the left of nums[i]
        postfix = [0] #postfix[i] contains the sum of everything to the right of nums[i]
        prefix_sum = postfix_sum = 0

        for i in range(len(nums) - 1):
            prefix_sum += nums[i]
            prefix.append(prefix_sum)
    
        for i in range(len(nums) - 1, 0, -1):
            postfix_sum += nums[i]
            postfix.insert(0, postfix_sum)

        for i in range(len(nums)):
            if prefix[i] == postfix[i]:
                return i

        return -1

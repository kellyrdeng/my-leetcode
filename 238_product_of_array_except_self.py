class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1] * len(nums)
        
        prefix = 1
        for i in range(len(nums)):
            answer[i] = prefix
            prefix *= nums[i]
            
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            answer[i] *= postfix
            postfix *= nums[i]

        return answer
    #[1, 2, 3, 4]
    #prefix = [1, 1, 2, 6]
    #postfix = [24, 12, 4, 1]

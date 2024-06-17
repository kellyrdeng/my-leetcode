class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1 for x in nums]
        
        prefix = 1
        for i in range(1, len(nums)):
            answer[i] = prefix * nums[i - 1]
            prefix = answer[i]
            
        postfix = 1
        for i in range(len(nums) - 2, -1, -1):
            cur_postfix = postfix * nums[i + 1]
            postfix = cur_postfix
            answer[i] *= cur_postfix

        return answer
    #[1, 2, 3, 4]
    #prefix = [1, 1, 2, 6]
    #postfix = [24, 12, 4, 1]

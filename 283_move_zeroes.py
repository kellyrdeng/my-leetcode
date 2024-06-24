class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #everything to the left of left is non-zero
        #everything to the right of right is zeroes
        left, right = 0, len(nums) - 1 

        while left < right: #ends when left = right aka perfectly partitioned
            if nums[left] != 0:
                left += 1
                continue
            else: #move zero to the end
                nums.pop(left)
                nums.insert(right, 0)
                right -= 1

            

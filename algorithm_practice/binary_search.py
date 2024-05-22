class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = low + ((high - low) // 2)

            if target == nums[mid]:
                return mid
            elif target < nums[mid]: #check left side
                high = mid - 1
            else: #target > nums[mid], check right side
                low = mid + 1
        
        return -1

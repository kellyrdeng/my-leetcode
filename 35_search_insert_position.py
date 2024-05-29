class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = low + ((high - low) // 2)
            if target == nums[mid]:
                return mid

            if target < nums[mid]:
                high = mid - 1
            else: #target > nums[mid]
                low = mid + 1

        return low #since low = high + 1 right now, where they cross is where it should be inserted

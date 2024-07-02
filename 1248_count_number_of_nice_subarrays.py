class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        valid_subarrays = 0
        left, middle, odds = 0, 0, 0

        for right in range(len(nums)):
            if nums[right] % 2 == 1:
                odds += 1

            while odds > k: #shift left/middle
                if nums[left] % 2 == 1:
                    odds -= 1
                left += 1
                middle = left

            if odds == k:
                #move middle to next odd
                while nums[middle] % 2 == 0:
                    middle += 1

                valid_subarrays += 1 + middle - left

        return valid_subarrays

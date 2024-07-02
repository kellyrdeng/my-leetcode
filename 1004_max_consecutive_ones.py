class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left, right = 0, 0
        consecutive_ones = 1 #starts at 1 to account for the first window
        flipped = 0 #must stay <= k
        maximum = 0

        while right < len(nums):
            if nums[right] == 0:
                flipped += 1

            #check if valid:
            while flipped > k: #if invalid, increment left until valid
                if nums[left] == 0:
                    flipped -= 1
                left += 1
                consecutive_ones -= 1

            maximum = max(maximum, consecutive_ones)

            #make move
            right += 1
            consecutive_ones += 1

        return maximum

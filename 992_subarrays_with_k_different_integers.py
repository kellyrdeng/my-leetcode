class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.sliding_window_at_most_k(nums, k) - self.sliding_window_at_most_k(nums, k - 1)

    def sliding_window_at_most_k(self, nums, k):
        good_subarrays = 0
        left = 0

        for right in range(len(nums)):
            #find current subarray and count the distinct ints
            subarray = nums[left:right + 1]
            counts = Counter(subarray)

            while len(counts) > 2: #if more than 2 distinct, increment left pointer
                dropped = nums[left]
                left += 1

                #update counts
                counts[dropped] -= 1
                if counts[dropped] == 0: del counts[dropped]

            good_subarrays += right - left + 1

        return good_subarrays

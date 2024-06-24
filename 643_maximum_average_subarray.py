class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left, right = 0, k - 1

        #calculate first sum: nums[0] + ... + nums[k - 1]
        sum = 0
        i = left
        while i <= right:
            sum += nums[i]
            i += 1

        max_avg = sum / k #[1, 2, 3, 4]

        while right < len(nums) - 1:
            #adjust sum
            sum -= nums[left]
            sum += nums[right+1]

            #adjust window
            left, right = left + 1, right + 1

            #calculate avg for current window
            avg = sum / k
            if avg > max_avg:
                max_avg = avg

        return max_avg

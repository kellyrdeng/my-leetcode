class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        counts = {}
        for x in nums:
            counts[x] = counts.get(x, 0) + 1

        match = 0 #each pair counted twice
        for x in counts:
            if k - x not in counts:
                continue

            if x * 2 == k:
                match += counts[x]
            else:
                match += min(counts[x], counts[k - x])

        return match // 2

        ''' TWO POINTER SOLUTION
        nums.sort() #[1, 3, 3, 3, 4]
        left, right = 0, len(nums) - 1
        pairs = 0

        while left < right:
            sum = nums[left] + nums[right]
            if sum == k:
                left, right = left + 1, right - 1
                pairs += 1

            if sum < k:
                left += 1
            if sum > k:
                right -= 1

        return pairs
        '''

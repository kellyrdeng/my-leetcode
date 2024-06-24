class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        counts = {} #x: 
        for x in nums:
            if x in counts:
                counts[x] += 1
            else:
                counts[x] = 1

        pairs = 0
        for x in counts:
            if k - x not in counts:
                continue

            if x * 2 == k:
                pairs += counts[x]
            else:
                pairs += min(counts[x], counts[k - x])

        return pairs // 2

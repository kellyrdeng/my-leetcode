class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []
        maxCandies = max(candies) - extraCandies
        
        for kid in candies:
            result.append(kid >= maxCandies)

        return result

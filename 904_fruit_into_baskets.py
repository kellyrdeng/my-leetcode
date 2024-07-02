class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left = 0
        baskets = {} #represents different kinds of fruit encountered, should be 2
        max_fruits = 0

        for right in range(len(fruits)):
            baskets[fruits[right]] = baskets.get(fruits[right], 0) + 1

            while len(baskets) > 2: #too many fruit kinds, move left pointer
                drop = fruits[left]
                baskets[drop] -= 1
                if baskets[drop] == 0:
                    del baskets[drop]
                left += 1

            max_fruits = max(max_fruits, right - left + 1)

        return max_fruits

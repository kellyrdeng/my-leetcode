class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x

        low, high = 2, x
        while low <= high:
            mid = low + ((high - low) // 2)
            mid_square = mid * mid
            if mid_square == x:
                return mid

            if mid_square > x: #mid is too big
                high = mid - 1
            else: #mid is too small
                low = mid + 1

        return high

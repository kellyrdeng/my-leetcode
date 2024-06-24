class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitude = 0
        max_alt = 0

        for x in gain:
            altitude += x
            max_alt = max(altitude, max_alt)

        return max_alt

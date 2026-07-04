class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitude = 0
        highest = 0

        for g in gain: d
            altitude += g
            highest = max(highest, altitude)

        return highest
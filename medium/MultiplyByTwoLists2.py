from typing import List
from bisect import bisect_left, bisect_right

class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7

        pos = []
        digits = []

        for i, ch in enumerate(s):
            if ch != '0':
                pos.append(i)
                digits.append(int(ch))

        m = len(digits)

        # powers of 10
        pow10 = [1] * (m + 1)
        for i in range(1, m + 1):
            pow10[i] = (pow10[i - 1] * 10) % MOD

        # prefix modulo of concatenated digits
        prefMod = [0] * (m + 1)
        for i, d in enumerate(digits):
            prefMod[i + 1] = (prefMod[i] * 10 + d) % MOD

        # prefix digit sums
        prefSum = [0] * (m + 1)
        for i, d in enumerate(digits):
            prefSum[i + 1] = prefSum[i] + d

        ans = []

        for l, r in queries:
            left = bisect_left(pos, l)
            right = bisect_right(pos, r) - 1

            if left > right:
                ans.append(0)
                continue

            length = right - left + 1

            x = (
                prefMod[right + 1]
                - prefMod[left] * pow10[length]
            ) % MOD

            digit_sum = prefSum[right + 1] - prefSum[left]

            ans.append((x * digit_sum) % MOD)

        return ans
class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        a = 0
        for i in patterns:
            if word.find(i) >= 0:
                a += 1
        return a
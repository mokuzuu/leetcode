from collections import defaultdict


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d = defaultdict(int)
        for i in nums:
            d[i] += 1

        for k in d:
            if d[k] == 1:
                return k

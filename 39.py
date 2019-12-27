class Solution:
    def combinationSum(self, candidates: [int], target: int) -> [[int]]:
        res = list()
        self.helper(res, list(), candidates, target, 0)
        return res

    def helper(self, res: [int], tmp, candidates: [int], target: int, index: int):
        if(target <= 0):
            if(target == 0):
                res.append(list(tmp))
            return

        for i in range(index, len(candidates)):
            tmp.append(candidates[i])
            self.helper(res, tmp, candidates, target, i)
            tmp.remove(tmp.size() - 1)


print(Solution().combinationSum([2, 3, 6, 7], 7))

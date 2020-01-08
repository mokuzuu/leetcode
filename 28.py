import re


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle is "":
            return 0
        repatter = re.compile(r"{}".format(needle))
        result = repatter.search(haystack)
        if result is None:
            return -1
        return result.start()

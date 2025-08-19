# Longest Increasing Subsequence

import bisect
from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = []

        for n in nums:
            i = bisect.bisect_left(sub, n)
            if i == len(sub):
                sub.append(n)
            else:
                sub[i] = n
        return len(sub)

if __name__ == "__main__":
    s = Solution()

    nums = []
    print(s.lengthOfLIS(nums))
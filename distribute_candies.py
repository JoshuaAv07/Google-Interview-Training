class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:

        candyTypes = set(candyType)
        n = len(candyTypes)
        max_candies = len(candyType) // 2
        return min(n, max_candies)

if __name__ == "__main__":
    s = Solution()
    candyType = [1,1,2,2,3,3]
    s.distributeCandies(candyType)
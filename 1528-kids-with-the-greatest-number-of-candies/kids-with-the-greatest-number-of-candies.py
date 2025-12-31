class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        max_c = max(candies)
        ans = []
        for ch in candies:
            if ch+extraCandies>=max_c:
                ans.append(True)
            else:
                ans.append(False)
        return ans
        
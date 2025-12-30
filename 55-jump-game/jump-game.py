class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        power = 0
        for n in nums:
            if power < 0:
                return False
            elif n > power:
                power = n
            power -= 1
            
        return True
        
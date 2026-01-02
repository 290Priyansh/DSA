class Solution(object):
    def repeatedNTimes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)/2
        
        map1 = {}
        for ch in nums:
            if ch in map1:
                map1[ch]+= 1
            else:
                map1[ch]=1
        for key,value in map1.items():
            if value == n:
                return key
        


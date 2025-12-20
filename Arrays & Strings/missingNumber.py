class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = len(nums)
        nums.sort()
        for i in range(len(nums)):
            if(nums[i]==i):
                continue
            
            return i
        return a


        

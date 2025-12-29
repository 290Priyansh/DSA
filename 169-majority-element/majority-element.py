class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mid = len(nums)//2
        nums.sort()
        count = 1
       
        for i in range(len(nums)-1):
            count+=1       
            if nums[i] != nums[i+1]:
                count = 1
            if count>mid:
                return nums[i]
        return nums[0]
            
            


        
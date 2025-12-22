class Solution(object):
    def pivotIndex(self, nums):
        sum = 0
        for num in range(len(nums)):
            sum += nums[num]
        left_sum =0
        for i in range (len(nums)):
            right_sum = sum-left_sum-nums[i]
            if(left_sum == right_sum):
                return i
            left_sum +=nums[i]
        return -1
        
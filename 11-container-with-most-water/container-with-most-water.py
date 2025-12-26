class Solution(object):
    def maxArea(self, height):
        left = 0
        right = len(height)-1
        maxArea = 0
        while(left<right):
            width = right-left
            currArea = min(height[left],height[right])* width
            maxArea = max(currArea,maxArea)
            if(height[left]<height[right]):
                left+=1
            else:
                right-=1
        return maxArea
       
        
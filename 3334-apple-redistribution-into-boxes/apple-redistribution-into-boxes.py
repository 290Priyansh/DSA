class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        sumApple = sum(apple)
        count = 0       
        capacity.sort(reverse = True)
        for num in capacity:            
            sumApple -= num
            count+=1
            if sumApple <= 0:
                return count
        
        
class Solution:
    def mySqrt(self, x: int) -> int:
        
        if x == 0 or x == 1:
            return x
  
        i = 0

        while i * i <= x:
            if i * i == x:
                return i
            i += 1
        
        #If i*i is greater than the target, answer must be previous one if x == 10, 3x3 = 9, 4x4 = 16 so answer must be approximately three
        return i-1 

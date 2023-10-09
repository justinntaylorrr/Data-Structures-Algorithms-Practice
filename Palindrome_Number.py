class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        num = x
        reversed_num = 0

        while num > 0:
            remainder = num % 10
            reversed_num = remainder + (reversed_num * 10)
            num = num // 10

        if reversed_num == x:
            return True
        else:
            return False

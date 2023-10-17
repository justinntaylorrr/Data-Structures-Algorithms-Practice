class Solution:
    def addBinary(self, a: str, b: str) -> str:
        

        # 0 + 0 = 0.
        # 0 + 1 = 1.
        # 1 + 0 = 1.
        # 1 + 1 = 10 ( carry 1 to the next significant bit)
        # 1 + 1 + 1 = 11( carry 1 to the next significant bit)


        result = ""
        carry = 0

        #Ensures both inputs are the same length

        while len(a) < len(b):
            a = "0" + a
    
        while len(b) < len(a):
            b = "0" + b

        for i in range(len(a)-1, -1, -1):
            r = int(a[i]) + int(b[i]) + carry
            result = str(r % 2) + result
            
            carry = r // 2

        if carry:
            result = str(carry) + result
                
        return result

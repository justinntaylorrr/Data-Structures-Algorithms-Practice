#Finds a string 'needle' in a string 'haystack' and returns index of the first occurence

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        for i in range(len(haystack) - len(needle) + 1):
            j = haystack[i:i + len(needle)]

            if j == needle:
                 return i
            
        return -1

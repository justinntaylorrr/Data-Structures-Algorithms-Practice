class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if len(strs) == 0:
            return ""

        firstword = strs[0]

        for i in range(len(firstword)):
            for otherwords in strs[1:]:
                if (i == len(otherwords) or otherwords[i] != firstword[i]):
                    return firstword[0:i]

        return firstword

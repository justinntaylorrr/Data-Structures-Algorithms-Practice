#Example 1:
#Input: strs = ["eat","tea","tan","ate","nat","bat"]

#Output: [["bat"],["nat","tan"],["ate","eat","tea"]]


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        

        results = []

        for i in strs:
            sorted_word = "".join(sorted(i))
            
            for j in results:
                if sorted_word == "".join(sorted(j[0])):
                    j.append(i)
                    break
                
            else:
                results.append([i])
                
        return results

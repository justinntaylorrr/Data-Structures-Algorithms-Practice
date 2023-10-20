#Example 1:
#Input: strs = ["eat","tea","tan","ate","nat","bat"]

#Output: [["bat"],["nat","tan"],["ate","eat","tea"]]


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        

        anagram_dict = {}

        for word in strs:
            sorted_word = "".join(sorted(word))
        
            if sorted_word in anagram_dict:
                anagram_dict[sorted_word].append(word)
            else:
                anagram_dict[sorted_word] = [word]

        return list(anagram_dict.values())

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        numDict = {}
        
        for i in range(len(nums)):
            j = target - nums[i]
            
            if j in numDict:
                return [numDict[j], i]
            numDict[nums[i]] = i
        return []

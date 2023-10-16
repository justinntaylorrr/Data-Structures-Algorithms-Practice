class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        new_nums = []
        nums_length = len(nums)

        for i in range(0, nums_length):
            if nums[i] != val:
                new_nums.append(nums[i])

        nums[:] = new_nums
        k = len(new_nums)   
        return k

#Removes values = val from list then updates original list so they're removed 'in place'
#Example Input [1,2,4,3,3,0,4] val = 3
#Output [1,2,4,0,4]

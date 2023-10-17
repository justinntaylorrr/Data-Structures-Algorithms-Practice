#Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        start = 0
        end = len(nums) - 1

        while start <= end:
            midpoint = (start + end) // 2
        
            if nums[midpoint] == target:
                return midpoint
        
            elif nums[midpoint] < target:
                start = midpoint + 1
        
            elif nums[midpoint] > target:
                end = midpoint - 1

            else:
                return midpoint
        
        return start

#My O(n) solution, One Time AC
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        ind=0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[ind]=nums[i]
                ind+=1
        for i in range(ind,len(nums)):
            nums[i]=0
        
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums)<=1: return
        for i in range(len(nums)-1,0,-1):
            if nums[i-1]<nums[i]: break
        if i==1 and nums[i-1]>nums[i]: self.reverse(nums,0)
        else:
            for j in range(len(nums)-1,i-1,-1):
                if nums[i-1]<nums[j]: break
            
            temp=nums[i-1]
            nums[i-1]=nums[j]
            nums[j]=temp
            
            self.reverse(nums,i)
        
    def reverse(self, nums, i):
        left,right=i,len(nums)-1
        while left<right:
            temp=nums[left]
            nums[left]=nums[right]
            nums[right]=temp
            left+=1
            right-=1
        
        
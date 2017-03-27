#One Time AC.
class Solution(object): 
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left=self.searchLeft(nums,target)
        right=self.searchRight(nums,target)
        return [left,right]
    
    def searchLeft(self,nums,target):
        left,right=0,len(nums)-1
        while left<=right:
            mid=(left+right)/2
            if nums[mid]==target and (mid==0 or nums[mid-1]<nums[mid]):
                return mid
            elif nums[mid]==target and nums[mid-1]==nums[mid]:
                right=mid-1
            elif nums[mid]<target:
                left=mid+1
            else:
                right=mid-1
        return -1
        
    def searchRight(self,nums,target):
        left,right=0,len(nums)-1
        while left<=right:
            mid=(left+right)/2
            if nums[mid]==target and (mid==len(nums)-1 or nums[mid+1]>nums[mid]):
                return mid
            elif nums[mid]==target and nums[mid+1]==nums[mid]:
                left=mid+1
            elif nums[mid]>target:
                right=mid-1
            else:
                left=mid+1
        return -1
        
    
    
    
    
    
    
    
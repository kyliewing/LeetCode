#My binary search solution, One Time AC. O(logn) time, O(1) space.
class Solution(object):
    def search(self, nums, target):
        #:type nums: List[int]
        #:type target: int
        #:rtype: int
        if len(nums)<=0: return -1
        return self._helper(0,len(nums)-1,nums,target)
        
    def _helper(self, left, right, nums, target):
        if left==right and nums[left]!= target: return -1
        mid=(left+right)/2
        if target==nums[mid]: return mid
        if nums[left]>nums[mid]:
            if nums[mid]<=target<=nums[right]:
                return self._helper(mid+1,right,nums,target)
            else:
                return self._helper(left,mid-1,nums,target)
        else:
            if nums[left]<=target<=nums[mid]:
                return self._helper(left,mid-1,nums,target)
            else:
                return self._helper(mid+1,right,nums,target)
        

class Solution(object):
    def search(self, nums, target):
        if len(nums)<=0: return -1
        left,right=0,len(nums)-1
        while left<right:
            mid=(left+right)/2
            if target==nums[mid]: return mid
            if nums[left]>nums[mid]:
                if nums[mid]<=target<=nums[right]:
                    left=mid+1
                else:
                    right=mid-1
            else:
                if nums[left]<=target<=nums[mid]:
                    right=mid-1
                else:
                    left=mid+1
        if nums[left]==target: return left
        else: return -1
        
        
        
        



            
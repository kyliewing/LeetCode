"""
The idea is to sort an input array and then run through all indices of a possible first element of a triplet. For each possible first element we make a standard bi-directional 2Sum sweep of the remaining part of the array. Also we want to skip equal elements to avoid duplicates in the answer without making a set or smth like that.
"""
#O(n^2)
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res=[]
        nums=sorted(nums)   #notice nums=sorted(nums)
        for i in range(len(nums)-2):
            if i==0 or (i>0 and nums[i-1]!=nums[i]):
                low,high,two_sum=i+1,len(nums)-1,0-nums[i]
                while low<high:
                    if nums[low]+nums[high]==two_sum:
                        res.append([nums[low],nums[high],nums[i]])
                        while low<high and nums[low]==nums[low+1]: low+=1
                        while low<high and nums[high]==nums[high-1]: high-=1
                        low,high=low+1,high-1
                    elif nums[low]+nums[high]<two_sum:
                        low+=1
                    else:
                        high-=1
        return res
                    
                
                
                
                
                
        
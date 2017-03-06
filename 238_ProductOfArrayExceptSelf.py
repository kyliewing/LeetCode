#My Brute Force solution, O(n^2), TLE
class Solution(object):
    def productExceptSelf(self, nums):
        #:type nums: List[int]
        #:rtype: List[int]
        res=[]
        for i in range(len(nums)):
            temp=1
            for j in range(len(nums)):
                if j!=i:
                    temp*=nums[j]
            res.append(temp)
        return res

#Two directions scan version, O(n) time, O(1) space
class Solution(object):
    def productExceptSelf(self, nums):
        res=[1]*len(nums)
        temp=nums[0]
        for i in range(1,len(nums)): #forwards scan
            res[i]*=temp
            temp*=nums[i]
        temp=nums[-1]
        for i in range(len(nums)-2,-1,-1): #backwards scan
            res[i]*=temp
            temp*=nums[i]
        return res
            
        
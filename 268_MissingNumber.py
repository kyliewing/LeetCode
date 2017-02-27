
#My hash_table version, O(n) time, O(n) space, One Time AC.
class Solution(object):
    def missingNumber(self, nums):
        #:type nums: List[int]
        #:rtype: int
        list_length=len(nums)
        if list_length==0: return 0
        my_hash={}
        for i in range(list_length):
            my_hash[nums[i]]=my_hash.get(nums[i],0)+1
        for i in range(list_length+1):
            if i not in my_hash: 
                return i
                
#My sum difference version, O(n) time, O(1) space, One Time AC.
class Solution(object):
    def missingNumber(self, nums):
        list_length=len(nums)
        if list_length==0: return 0
        sum_total=sum_list=0
        for i in range(list_length+1):
            sum_total+=i
        for i in range(list_length):
            sum_list+=nums[i]
        return sum_total-sum_list


#Sum difference version 2.
class Solution(object):
    def missingNumber(self, nums):
        list_length=len(nums)
        res=list_length
        for i in range(list_length):
            res+=i-nums[i]
        return res
        
#Bit Manipulation verion:
#We all know that a^b^b =a, which means two xor operations with the same number will eliminate the number and reveal the original number.
class Solution(object):
    def missingNumber(self, nums):
        res=len(nums)
        for i in range(len(nums)):
            res=res^i^nums[i]
        return res
 
#Binary Serach version, O(nlogn) time
class Solution(object):
    def missingNumber(self, nums):
        nums=sorted(nums)  #sort nums
        left,right=0,len(nums)
        while left<right:
            mid=(left+right)/2
            if nums[mid]>mid: 
                right=mid
            else:
                left=mid+1
        return right #or left 
                
        
        
        
        

        
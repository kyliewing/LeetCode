#Your runtime beats 55.22% of python submissions. (One Time AC)
#Given an array and a value, remove all instances of that value in place and return the new length.
#Do not allocate extra space for another array, you must do this in place with constant memory.
#The order of elements can be changed. It doesn't matter what you leave beyond the new length.
#Example:Given input array nums = [3,2,2,3], val = 3
#Your function should return length = 2, with the first two elements of nums being 2.

class Solution(object):
    def removeElement(self, nums, val):
        length=len(nums)
        numbers=0
        if length==0:
            return numbers
        for i in range(length):  #Don't miss range
            if nums[i]!=val:
                nums[numbers]=nums[i]
                numbers+=1
        return numbers
                
            
#A more concise version       
class Solution(object):
    def removeElement(self,nums,val):
        dis_index=i=0
        for i in range(len(nums)):
            if nums[i]!=val:
                nums[dis_index]=nums[i]
                dis_index+=1
        return dis_index
        
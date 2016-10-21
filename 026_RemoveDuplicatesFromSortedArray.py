#"Two Pointers"
#Your runtime beats 51.79% of python submissions. (One Time AC)
#Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.
#Do not allocate extra space for another array, you must do this in place with constant memory.
#My solution is not clean
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length=len(nums)
        number=0                   ##Need to take care of the name of the variable, len is not a correct name
        if length==0 or length==1:
            return length
        i=0
        while i<length-1:
            temp=i
            while temp<length-1 and nums[temp+1]==nums[i]:  ##The name is nums, not a
                temp+=1
            if temp==length-1:    ##boundary case(end)
                if nums[temp-1]!=nums[temp]:
                    number+=1
                    nums[number]=nums[temp]
                return number+1
            number+=1             ##move the distinct number forward
            nums[number]=nums[temp+1]
            i=temp+1
        return number+1
                
        

#Your runtime beats 77.23% of python submissions.
#Two pointer version:
class Solution(object):
    def removeDuplicates(self, nums):
        i=slow=fast=0           #Two pointers
        while fast<len(nums):   #Condition where len(nums) is 0 or 1 is contained
            while fast<len(nums) and nums[fast]==nums[slow]: #Notice the order of these two conditions, becuase of "lazy and"
                fast+=1
            nums[i]=nums[slow]
            i,slow=i+1,fast
        return i
            

#Your runtime beats 58.21% of python submissions.
#One scan version:
class Solution(object):
    def removeDuplicates(self, nums):
        if len(nums)<2: return len(nums)#When length of nums is 0 or 1
        cou=1                           #Deal with index from 1, and leave index 0 what it is
        for i in range(1,len(nums)):    #Loop from index 1
            if nums[i]!=nums[i-1]:      #If find a new element, move it to the index cou
                nums[cou]=nums[i]
                cou+=1
        return cou
        
            
            

            
            
            
                
        
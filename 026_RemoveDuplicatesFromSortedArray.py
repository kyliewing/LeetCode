#Your runtime beats 51.79% of python submissions. (One Time AC)
#Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.
#Do not allocate extra space for another array, you must do this in place with constant memory.
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length=len(nums)
        number=0                   ##Need to take care of the name of the variable, len is not a ocrrect name
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
                
        
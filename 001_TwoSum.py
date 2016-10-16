#Hash Table:O(n)
class Solution(object):
    def twoSum(self,nums,target):
        if len(nums)<=1:
            return False
        my_dict={}
        for i in range(len(nums)):
            if nums[i] in my_dict:
                return [my_dict[nums[i]],i]
            else:
                my_dict[target-nums[i]]=i

#Your runtime beats 59.26% of python submissions.
class Solution(object):
    def twoSum(self, nums, target):
        if len(nums)<=1:
            return False
        my_dict={}
        for i in range(len(nums)):
            if target-nums[i] in my_dict:
                return [my_dict[target-nums[i]],i]
            else:
                my_dict[nums[i]]=i
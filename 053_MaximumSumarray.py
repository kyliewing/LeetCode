#DP
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==1: return nums[0]
        sub_array=[]
        for i in range(len(nums)):
            if i==0: sub_array.append(nums[0])
            else:
                sub_array.append(max(sub_array[i-1]+nums[i],nums[i]))
        return max(sub_array)
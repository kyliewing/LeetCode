#DP
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0: return 0  #notice corner case
        money=[0]*len(nums)
        for i in range(len(nums)):
            if i==0: money[i]=nums[i]
            elif i==1: money[i]=max(nums[i],nums[i-1])
            else:
                money[i]=max(money[i-1],money[i-2]+nums[i])
        return money[-1]
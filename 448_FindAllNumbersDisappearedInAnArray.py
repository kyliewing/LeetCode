#My hash table, O(n) space version.
class Solution(object):
    def findDisappearedNumbers(self, nums):
        #:type nums: List[int]
        #:rtype: List[int]
        my_hash={}
        res=[]
        for num in nums:
            my_hash[num]=my_hash.get(num,0)+1
        for i in range(1,len(nums)+1):
            if i not in my_hash:F
                res.append(i)
        return res

#O(1) space version.
#The basic idea is that we iterate through the input array and mark elements as negative using nums[nums[i] -1] = -nums[nums[i]-1]. 
class Solution(object):
    def findDisappearedNumbers(self, nums):
        res=[]
        for i in range(len(nums)):
            index=abs(nums[i])-1
            nums[index]=-abs(nums[index])
        for i in range(len(nums)):
            if nums[i]>0:
                res.append(i+1)
        return res
        
        
        
        
        
            
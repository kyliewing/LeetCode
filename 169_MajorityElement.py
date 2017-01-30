
#My Hash Table version
class Solution(object):
    def majorityElement(self, nums):
        #:type nums: List[int]
        #:rtype: int
        my_dict={}
        for num in nums:
            my_dict[num]=my_dict.get(num,0)+1  # my_dict.get(num,0) (default 0)
        for element in my_dict:
            if my_dict[element]>len(nums)/2: return element

                
#Moore's Voting Algorithm
class Solution(object):
    def majorityElement(self,nums):
        vote,count=nums[0],1
        for i in range(1,len(nums)):
            if count==0: vote,count=nums[i],count+1
            elif nums[i]==vote: count+=1
            else: count-=1
        return vote
            
            
            
            
            
            
            
            
            
            
            
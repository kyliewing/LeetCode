#My hash table verion, One Time AC
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        my_hash={}
        for i in range(len(nums)):
            if nums[i] not in my_hash:
                my_hash[nums[i]]=i
            else:
                if i-my_hash[nums[i]]<=k:
                    return True
                else:
                    my_hash[nums[i]]=i
        return False

#More concise hash table version:
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        my_hash={}
        for i,v in enumerate(nums):
            if v in my_hash and i-my_hash[v]<=k:
                return True
            my_hash[v]=i
        return False


#Sliding Window version:
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        my_hash={}
        for i,v in enumerate(nums):
            if i>k:
                del my_hash[nums[i-k-1]]  #del dic[key]
            if v in my_hash:
                return True
            else:
                my_hash[v]=i
        return False
        
        
        
        
        
        
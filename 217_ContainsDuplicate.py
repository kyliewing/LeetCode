#My hash table version:
class Solution(object):
    def containsDuplicate(self, nums):
        #:type nums: List[int]
        #:rtype: bool
        my_hash={}
        for num in nums:
            my_hash[num]=my_hash.get(num,0)+1
        for key in my_hash:
            if my_hash[key]>1: 
                return True
        return False

#My hash table version 2:
class Solution(object):
    def containsDuplicate(self, nums):
        my_hash={}
        for num in nums:
            my_hash[num]=my_hash.get(num,0)+1
        return len(my_hash)!=len(nums)

#My build in funcion version:
class Solution(object):
    def containsDuplicate(self, nums):
        return len(set(nums))!=len(nums)








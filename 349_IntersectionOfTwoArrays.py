#My hash table version, O(n+m) time, O(n+m) sapce, One Time AC.
class Solution(object):
    def intersection(self, nums1, nums2):
        #:type nums1: List[int]
        #:type nums2: List[int]
        #:rtype: List[int]
        my_dict={}
        res=[]
        for num in nums1:
            if num not in my_dict:
                my_dict[num]=1
        for num in nums2:
            if num in my_dict and my_dict[num]==1:
                res.append(num)
                my_dict[num]-=1
        return res

#Python build in function "set" version:
class Solution(object):
    def intersection(self, nums1, nums2):
        return list(set(nums1)&set(nums2))

#Sort firstly, then use two pointers version:
class Solution(object):
    def intersection(self, nums1, nums2):
        nums1=sorted(nums1)
        nums2=sorted(nums2)
        i,j=0,0
        res=[]
        while i<len(nums1) and j<len(nums2):
            if nums1[i]<nums2[j]:
                i+=1
            elif nums1[i]>nums2[j]:
                j+=1
            else:
                res.append(nums1[i])
                i,j=i+1,j+1          #don't forget this line
        return list(set(res))

#Binary Search version:
class Solution(object):
    def intersection(self, nums1, nums2):
        nums1=sorted(nums1)
        my_hash={}
        for num in nums2:
            if self.binarySearch(nums1,num) and num not in my_hash:
                my_hash[num]=1
        return my_hash.keys()
        
    def binarySearch(self, array, target):#standard binary search
        left,right=0,len(array)-1
        while left<=right:
            mid=(left+right)/2
            if target==array[mid]:
                return True
            elif target<array[mid]:
                right=mid-1
            else:
                left=mid+1
        return False
        
  
  
  
  
  
  
  
            
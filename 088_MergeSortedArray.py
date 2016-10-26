#"Array" "Two Pointers"
#Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
#You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2 The number of elements initialized in nums1 and nums2 are m and n respectively.
#:rtype: void Do not return anything, modify nums1 in-place instead. "In-place" is very important

#Your runtime beats 39.50% of python submissions.
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        #:rtype: void Do not return anything, modify nums1 in-place instead. "In-place" is very important
        """
        i=j=temp=0
        while i<m and j<n:   #Need to loop on the effective elements
            if nums1[temp]<nums2[j]: i,temp=i+1,temp+1 #If nums1 < nums2, then just move temp one step forward
            else:
                for cur in range(m+n-1,temp,-1): #Else, "insert" the current element in nums2 into nums1
                    nums1[cur]=nums1[cur-1]      #All the elements in nums1 before m+n all shilft right
                nums1[temp]=nums2[j]             #"Insert" the current element in nums2
                temp,j=temp+1,j+1
        if i==m and j<n:                         #If some elements remains in nums2
            for cur in range(j,n):
                nums1[temp]=nums2[cur]
                temp+=1
            
                


#Backwards Version: Because if go backwards, then existed elements in nums1 will not be polluted.
#Your runtime beats 96.79% of python submissions.
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        i,j,temp=m-1,n-1,m+n-1         #Backwards
        while j>-1:                    #We need to deal with every element in nums2
            if nums1[i]>nums2[j] and i>-1: #We put the larger one into temp index. Notice "i>-1", if i==0, then nums1 is done.
                nums1[temp]=nums1[i]
                temp,i=temp-1,i-1
            else:
                nums1[temp]=nums2[j]
                temp,j=temp-1,j-1
                
                
                
        
            
                
                
                
            
            
            
            
                        
                
            
            
            
            
        
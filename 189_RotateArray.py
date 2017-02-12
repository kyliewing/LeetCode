#My solution, Time O(n), Space O(n), need a copy of nums list:
class Solution(object):
    def rotate(self, nums, k):
        #:type nums: List[int]
        #:type k: int
        #:rtype: void Do not return anything, modify nums in-place instead.
        copy=[]
        for num in nums:
            copy.append(num)
        for i in range(len(nums)):
            nums[(i+k)%len(nums)]=copy[i]

#My solution, Time O(n), Space O(n), need a copy of nums list:
class Solution(object):
    def rotate(self, nums, k):
        copy=[]
        for num in nums:
            copy.append(num)
        for i in range(len(nums)):
            nums[i]=copy[(i+len(nums)-k)%len(nums)]


#Time O(n), Space O(k%length(nums)), need to copy part of the list, The Normal One
class Solution(object):
    def rotate(self, nums, k):
        length=len(nums)
        if length<=1: return
        step=k%length
        temp=[]
        for i in range(step):
            temp.append(nums[length-step+i])
        for i in range(length-1,step-1,-1):
            nums[i]=nums[i-step]
        for i in range(step):
            nums[i]=temp[i]
        
#Time O(n), Space O(1), Reverse Version, The Reverse One
class Solution(object):
    def rotate(self, nums, k):
        length=len(nums)
        if length<=1: return
        step=k%length      #get the step
        self.reverse(nums,0,length-1)  #reverse the whole list
        self.reverse(nums,0,step-1)    #reverse the left part
        self.reverse(nums,step,length-1)  #reverse the right part
        
        
    def reverse(self, nums, i, j):  #Reverse a list from i to j
        while(i<j):
            temp=nums[i]
            nums[i]=nums[j]
            nums[j]=temp
            i,j=i+1,j-1
    

#Time O(n), Space O(1), In Place, Place every element directly to it's required place version
#Notice that if we meet the original index again, we do the same thing to it's following element.
class Solution(object):
    def rotate(self, nums, k):
        length=len(nums)
        step=k%length   #this is the real step
        start=cur=count=0
        while count<length:  # when meet the start again, start+=1  , we need to do lenght time of change
            cur=start  #set cur=start for the beganing of each cycle
            pre=nums[start] 
            while count<length:  #for each cycle
                temp=nums[(cur+step)%length]
                nums[(cur+step)%length]=pre
                pre=temp
                cur=(cur+step)%length
                count+=1  #maintain the count
                if cur==start: break  #meet the start again
            start+=1
            
        
        
        
        
        
        
        
        

            
            
        
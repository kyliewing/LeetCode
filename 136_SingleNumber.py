#"Hash Table" "Bit Manipulation"!
#Given an array of integers, every element appears twice except for one. Find that single one.
#Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

#My Hash Table version. O(N)
#Your runtime beats 60.11% of python submissions.
class Solution(object):
    def singleNumber(self, nums):
        d={}
        for num in nums:
            if num in d: d[num]=2 #num appears twice
            else: d[num]=1#num appears once
        return d.keys()[d.values().index(1)] #Notice the usage of d.keys() and d.values().index()
        

#Your runtime beats 77.29% of python submissions.
class Solution(object):
    def singleNumber(self, nums):
        d={}
        for num in nums:
            d[num]=d.get(num,0)+1#num appears once
        return d.keys()[d.values().index(1)] #Notice the usage of d.keys() and d.values().index()



#Bit Manipulation version:
#Logic: XOR will return 1 only on two different bits. So if two numbers are the same, XOR will return 0. Finally only one number left. A ^ A = 0 and A ^ B ^ A = B.
#0 ^ N = N and N ^ N = 0
#Your runtime beats 99.76% of python submissions.
class Solution(object):
    def singleNumber(self, nums):
        res=0
        for num in nums: 
            res=res^num # res equals the XOR of all the elements in nums
        return res
        

##############??????????????
def singleNumber3(self, nums):
    return 2*sum(set(nums))-sum(nums)
    
def singleNumber4(self, nums):
    return reduce(lambda x, y: x ^ y, nums)
    
def singleNumber(self, nums):
    return reduce(operator.xor, nums)






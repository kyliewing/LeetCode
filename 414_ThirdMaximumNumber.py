
#My thrice scans version:
class Solution(object):
    def thirdMax(self, nums):
        #:type nums: List[int]
        #:rtype: int
        first=second=third=min_num=-2147483649 #set to min_num
        for num in nums:  #find the first number in the first scan
            if num>first: first=num
        for num in nums:  #find the second number in the second scan
            if num<first and num>second: second=num
        for num in nums:  #find the third number in the third scan
            if num<second and num>third: third=num
        if third!=min_num: return third #if third exists, return third
        else: return first #if thrid does not exists, return first


#Python Build-in Function Version:
class Solution(object):
    def thirdMax(self,nums):
        nums=set(nums)
        if len(nums)<3:
            return max(nums)
        nums.remove(max(nums))
        nums.remove(max(nums))
        return max(nums)


#Once scan version, maintian first, second and third all the time:
class Solution(object):
    def thirdMax(self,nums):
        first=second=third=None
        for num in nums:
            if num==first or num==second or num==third: continue #do not care duplicates
            if first==None or num>first:  #if first has not been set or num>first
                third=second #notice the order of these three lines, change the value of three max
                second=first
                first=num
            elif second==None or num>second:  #if second has not been set or num>second, change the value of two max
                third=second#notice it's elif
                second=num
            elif third==None or num>third: #if third has not been set or num>third, change the value of one max
                third=num
        return third if third!=None else first
        
        
        
        
        
        
        
        

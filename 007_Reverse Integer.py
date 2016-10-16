#Your runtime beats 21.67% of python submissions.
#My solution is not clean
class Solution(object):
    def reverse(self, x):
        result=0
        digit_list=[]
        x_abs=abs(x)
        while x_abs!=0:
            digit_list.append(x_abs%10)
            x_abs/=10
        mul=1
        for i in range(len(digit_list)-1,-1,-1):
            result+=digit_list[i]*mul
            mul*=10
        if (result<-(1<<31) or result>(1<<31)):
#overflow(assume the input is 32-bit integer)
            return 0
        if x<0:
            return -result
        return result
    
#Your runtime beats 73.89% of python submissions.
#Convert integer into string, then reverse the string
class Solution(object):
    def reverse(self, x):
        s=str(x)    #Convert integer into string
        res= int('-'+s[1:][::-1]) if s[0]=='-' else int(s[::-1]) #Deal with positive and negative integer
        return res if -1*(0x7fffffff+1) <= res <= 0x7fffffff else 0  #Check overflow


#Your runtime beats 31.11% of python submissions.
#Do not convert into string, reverse integer
class Solution(object):
    def reverse(self, x):
        absx,res=abs(x),0   #Deal with the absolute value
        while absx:
            res=res*10+absx%10  #Times the res by 10 and add the right most digit every loop
            absx/=10            #Divided by 10 every time
        res=res if -(0x7fffffff+1)<=res<=0x7fffffff else 0 #Check the overflow
        return res if x>0 else -res
        
        
        

#Your runtime beats 21.67% of python submissions.
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
            return 0
        if x<0:
            return -result
        return result
        
        
        

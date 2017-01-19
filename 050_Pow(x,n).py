#"Binary Search" "Math"
#Implement pow(x, n).

#My intuitive version: Runtime Error
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if x==0 or x==1: return x
        if n==0: return float(1)
        res=float(1)
        for i in range(n):   #Line 15: MemoryError
            res*=x
        return res
 



#My recursive version: Time Limit Exceeded
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if x==0 or x==1: return x
        if n==0: return float(1)
        if n==1: return x
        if n==-1: return 1/x #Notice that n could be negative
        return self.myPow(x,n/2)*self.myPow(x,((n+1)/2))#Do not forget self here. Notice n/2 and (n+1)/2
        
            

#My recursive version: O(logN)
#Your runtime beats 98.64% of python submissions.
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if x==0 or x==1: return x
        if n==0: return float(1)
        if n==1: return x
        if n==-1: return 1/x #Notice that n could be negative
        if n%2==0: return self.myPow(x,n/2)**2#n is even
        else: return self.myPow(x,n/2)**2*x**(n-n/2-n/2)#n is odd
        
        

##################################         
#Consise version: O(logN)
#Your runtime beats 92.22% of python submissions.
class Solution(object):
    def myPow(self, x, n):
        if n==0: return 1
        if x==0: return 0
        if n<0:
            n=-n
            x=1/x
        return self.myPow(x*x,n/2) if n%2==0 else x*self.myPow(x*x,n/2)
        
        

#################################
#Iterative version: O(logN)
#Your runtime beats 90.18% of python submissions.
class Solution(object):
    def myPow(self, x, n):
        if n<0:
            n=-n
            x=1/x
        res=1
        while n>0:
            if n&1: res*=x #Notice bit manipulatioin #If n is odd
            x*=x  #x*x
            n>>=1  #equals to n=n>>1
        return res
        
        
            
##################################               
#Bit Manipulation version: O(logN)
#In bit format and for a unsigned number, the number is represented as k0*2^0 + k1*2^1 + ... +k31*2^31. Therefore, once we know the pow(x,2^0), pow(x,2^1), ..., pow(x,2^31), we can get pow(x,n). And pow(x,2^m) can be constructed easily as pow(x,2^m) = pow(x,2^(m-1))*pow(x,2^(m-1)).
#Your runtime beats 97.27% of python submissions.
class Solution(object):
    def myPow(self, x, n):
        if n<0:
            n=-n
            x=1/x
        res=1
        pow_list=[x]
        for i in range(1,32):
            pow_list.append(pow_list[i-1]*pow_list[i-1]) #Calculate x^(2^i) in for i from 0 to 31
        for i in range(0,32):
            if n&1<<i: res*=pow_list[i] #if the ith bit of n is 1, then res * x(2^i)
        return res                
            
        

#Double x
class Solution(object):
    def myPow(self,x,n):
        if n==0: return 1
        if n<0:
            n=-n
            x=1/x
        return self.myPow(x*x,n/2) if n%2==0 else x*self.myPow(x*x,n/2)

#Double myPow
class Solution(object):
    def myPow(self,x,n):
        if n==0: return 1
        if n<0:
            n=-n
            x=1/x
        temp=self.myPow(x,n/2)
        return temp*temp if n%2==0 else x*temp*temp


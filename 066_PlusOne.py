#"Array" "Math"
#Given a non-negative number represented as an array of digits, plus one to the number.
#The digits are stored such that the most significant digit is at the head of the list.

#My solution:
#Convert to str and int version:
#Your runtime beats 42.87% of python submissions. (7 min)
class Solution(object):
    def plusOne(self, digits):
        s=''
        for d in digits: s+=str(d) #Convert the list to string
        newdig=int(s)+1            #Plus one
        res=[]
        for c in str(newdig):      #Convert the string to int then append each digit to list
            res.append(int(c))
        return res
        
            
 
#Your runtime beats 30.32% of python submissions.
#Cleaner version:
#No conversion version:
class Solution(object):
    def plusOne(self, digits):
        for i in range(len(digits)-1,-1,-1): #Backwards loop
            if digits[i]==9:                 #if it's 9, then change it to 0
                digits[i]=0
            else:                            #meet the first digit that is not 9, plus one and return 
                digits[i]+=1
                return digits
        digits.insert(0,1)                   #all 999..., insert 1 in the head
        return digits
                
        
            
#Your runtime beats 69.38% of python submissions.
#Conversion version 2:
class Solution(object):
    def plusOne(self, digits):
        num=0
        for i in range(len(digits)):               #Convert to integer
            num+=digits[i]*pow(10,len(digits)-1-i)
        return [int(d) for d in str(num+1)]        #Plus one, then convert to string, then append to list
        
                
        
            
               
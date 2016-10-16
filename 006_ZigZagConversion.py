#String:O(n)
##Your runtime beats 42.87% of python submissions.
#My solution is not clean
class Solution(object):
    def convert(self, s, numRows):
        if(numRows==1 or numRows>=len(s)):
            return s
        res=[""]*numRows
        period=2*(numRows-1)
        for row in range(numRows):
            index=row
            if row==0 or row==numRows-1:
                while(index<len(s)):
                    res[row]+=s[index]
                    index+=period
            else:
                while(index<len(s)):
                    res[row]+=s[index]
                    if index+(2*(numRows-row-1))<len(s):
                        res[row]+=s[index+(2*(numRows-row-1))]
                    index+=period
        return "".join(res)


#Your runtime beats 46.81% of python submissions.
#Cleaner Solution
class Solution(object):
    def convert(self, s, numRows):
        if numRows<=1: return s
        cycle,length,res=2*(numRows-1),len(s),""   
        for i in range(numRows):                 #Loop on every row
            for j in range(i,length,cycle):      #In every row, append new char by cycle
                res+=s[j]   
                j_2=j+cycle-2*i                  #Some rows has the second char in one cycle
                if (j_2-j)%cycle!=0 and j_2<length: #Notice to gurantee two conditions
                    res+=s[j_2]
        return res
                    
                
        

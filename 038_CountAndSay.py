#Your runtime beats 0.45% of python submissions.
#The count-and-say sequence is the sequence of integers beginning as follows: 1, 11, 21, 1211, 111221, ...
#Given an integer n, generate the nth sequence.
class Solution(object):
    def countAndSay(self, n):
        res=['1']
        if n==0 or n==1:  #For the 1th sequence
            return ''.join(res)
        for i in range(n-1):
            temp_res=[]
            j=0
            temp=j
            if i==0:
                temp_res=temp_res+['1']+[res[0]]#For the 2th sequence
            else:
                while j<len(res)-1:            #For the 3th and more sequences (Note it's len(res)-1, not len(res))
                    count=1
                    while j<len(res)-1 and res[j+1]==res[j]:
                        count+=1
                        j+=1
                    temp_res=temp_res+[str(count)]+[res[j]]
                    temp=j+1
                    j=temp
                if len(res)>1 and res[-1]!=res[-2]:  #The critical case
                    temp_res=temp_res+['1']+[res[-1]]
            res=temp_res
        return ''.join(res)
            
                    
                
                
class Solution(object):
    def countAndSay(self,n):
        res="1"
        for i in range(n-1):
            cur=""
            j=0
            while j<len(res):
                count=1
                while j+1<len(res) and res[j]==res[j+1]:
                    count+=1
                    j+=1
                cur=cur+str(count)+res[j]
                j+=1
            res=cur
        return res
                
                    
            
            
        
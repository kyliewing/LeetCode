Python

#My iterative solution, One Time AC
class Solution(object):
    def letterCombinations(self, digits):
        if len(digits)==0: return []
        my_dict={'0':[' '],'1':['*'],'2':['a','b','c'],'3':['d','e','f'],'4':['g','h','i'],'5':['j','k','l'],'6':['m','n','o'],'7':['p','q','r','s'],'8':['t','u','v'],'9':['w','x','y','z']}
        combs=my_dict[digits[0]]
        for i in range(1,len(digits)):
            temp=[]
            for char in combs:
                for next_char in my_dict[digits[i]]:
                    temp.append(char+next_char)
            combs=temp
        return combs

#My recursive solution
class Solution(object):
    def letterCombinations(self,digits):
        
#My iterative queue version

        
                
                
            
            


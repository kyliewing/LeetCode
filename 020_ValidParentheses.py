#"Stack"
#Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#Your runtime beats 85.35% of python submissions.
#My solution
class Solution(object):
    def isValid(self, s):
        stack_dict={'(':')', '{':'}', '[':']'}    #Usage of Hash Table
        stack_list=[]                             
        for char in s:  
            if char=='(' or char =='{' or char=='[' or len(stack_list)==0:#If it's left bracket or empty, then append it
                stack_list.append(char)
            elif (stack_dict.has_key(stack_list[-1])) and char==stack_dict[stack_list[-1]]:#If the last char has key and it's a pair
                stack_list.pop()#The delete the last char
            else:
                stack_list.append(char)
        if len(stack_list)==0:
            return True
        return False
                
        

#Your runtime beats 60.58% of python submissions.
#A simpler version: use dictionary and stack
class Solution(object):
    def isValid(self, s):
        stackDict={')':'(', '}':'{', ']':'['}    #Usage of Hash Table
        stack=[]                                 #Initialize the stack
        for c in s:
            if stack and c in stackDict and stack[-1]==stackDict[c]: #The condition that stack will pop one char,Notice it's == not =
                stack.pop() 
            else:
                stack.append(c)                  #The condition that stack will push one char
        return not stack
        
                
  
#A version which can track the place where cause the error
class Solution(object):
    def isValid(self,s):
        my_dict={')':'(','}':'{',']':'['}
        stack=[]
        for c in s:
            if stack and c in my_dict:
                if stack.pop()!=my_dict[c]:
                    return False
            else:
                stack.append(c)
        return not stack
                      
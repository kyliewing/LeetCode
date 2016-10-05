#Your runtime beats 85.35% of python submissions.
#Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
class Solution(object):
    def isValid(self, s):
        stack_dict={'(':')', '{':'}', '[':']'}
        stack_list=[]
        for char in s:
            if char=='(' or char =='{' or char=='[' or len(stack_list)==0:
                stack_list.append(char)
            elif (stack_dict.has_key(stack_list[-1])) and char==stack_dict[stack_list[-1]]:
                stack_list.pop()
            else:
                stack_list.append(char)
        if len(stack_list)==0:
            return True
        return False
                
        
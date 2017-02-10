#My reverse the whole list, then reverse by word version:
class Solution:
    # @param s, a list of 1 length strings, e.g., s = ['h','e','l','l','o']
    # @return nothing
    def reverseWords(self, s):
        s=self._reverse(s)  #reverse the whole string
        begin=0
        for i in range(len(s)):
            if s[i]==' ':
                s[begin:i]=self._reverse(s[begin:i])  #list indices using : not ,
                begin=i+1 
        s[begin:]=self._reverse(s[begin:])   #reverse the last word

    def _reverse(self, s):
        if len(s)==0: return s
        begin,end=0,len(s)-1
        while begin<end:
            s[begin],s[end]=s[end],s[begin]
            begin,end=begin+1,end-1

#Python build in function version:
#Slice of list can use reverse() function, does not work. But, we can assign the reversed part to the slice of list.
class Solution(object):
    def reverseWords(self, s):
        s.reverse()
        begin=0
        for i in range(len(s)):
            if s[i]==" ":
                s[begin:i]=reversed(s[begin:i])
                begin=i+1
        s[begin:]=reversed(s[begin:])

#Python one line version 1:
class Solution(object):
    def reverseWords(self, s):
        s[:]= list(' '.join(''.join(s).split(' ')[::-1]))


#Python one line version 2:
class Solution(object):
    def reverseWords(self, s):
        s[:]=list(' '.join(reversed(''.join(s).split(' '))))


        
            
            
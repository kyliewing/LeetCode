#"Hash Table" "Two pointers" "String"
#Given a string, find the length of the longest substring without repeating characters.
#Given "abcabcbb", the answer is "abc", which the length is 3.
#Given "pwwkew", the answer is "wke", with the length of 3.
#Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

#My hash-table&two pointers version
#Your runtime beats 85.81% of python submissions.
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        p1,my_dict,max_len=0,{},0 #use p1 as the first pointer and use i as the second pointer
        for i in range(len(s)): #loop each character of s
            if s[i] in my_dict: #if s[i] in hash table, calculate the max_len and delete the chars from hash table before s[i]
                max_len=max(max_len,i-p1)
                while s[p1]!=s[i]:
                    del my_dict[s[p1]] #delete a key from dictionary
                    p1+=1
                p1+=1
            if s[i] not in my_dict: my_dict[s[i]]=1
            if i==len(s)-1: max_len=max(max_len,i-p1+1)#for the length of the last substring
        return max_len
                
        
                
            
####################################           
#Hash Table&Two Pointers version.
#Your runtime beats 74.06% of python submissions.
#the basic idea is, keep a hashmap which stores the characters in string as keys and their positions as values, and keep two pointers which define the max substring. move the right pointer to scan through the string , and meanwhile update the hashmap. If the character is already in the hashmap, then move the left pointer to the right of the same character last found. Note that the two pointers can only move forward.
#Notice that 
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        my_dict,max_len,p1={},0,0
        for i in range(len(s)):
            if s[i] in my_dict: p1=max(p1,my_dict[s[i]]+1)#The variable "p1" is used to indicate the index of first character of this substring. If the repeated character's index is less than p1 itself, which means the repeated character in the hash map is no longer available this time
            my_dict[s[i]]=i
            max_len=max(max_len,i-p1+1)
        return max_len

 

        
                
            
            
            
        
#O(m*n) Brute Force (Time Limit Exceeded):
class Solution(object):
    def findAnagrams(self, s, p):
        :type s: str
        :type p: str
        :rtype: List[int]
        
        my_dict,res={},[]
        for c in p:
            if c not in my_dict: my_dict[c]=1
            else: my_dict[c]+=1
        for i in range(len(s)-len(p)+1):  #O(n)
            cur_dict={}
            for j in range(len(p)):       #O(m)
                if s[i+j] not in cur_dict: cur_dict[s[i+j]]=1
                else: cur_dict[s[i+j]]+=1
            if cur_dict==my_dict: res.append(i)
        return res


#O(n) Sliding Window Version:
class Solution(object):
    def findAnagrams(self,s,p):
        my_dict,res,cur_dict={},[],{}
        if len(s)<len(p): return res
        for c in p:         #Make hash_talbe for p
            if c not in my_dict: my_dict[c]=1
            else: my_dict[c]+=1
        for i in range(len(p)):#Pre-load sliding window
            if s[i] not in cur_dict: cur_dict[s[i]]=1
            else: cur_dict[s[i]]+=1
        if cur_dict==my_dict: res.append(0)#Corner case: pre_loaded hash table==p's hash table
        for i in range(m,n): #Moving sliding window
        for i in range(len(p),len(s)):
            cur_dict[s[i-len(p)]]-=1
            if cur_dict[s[i-len(p)]]==0: del cur_dict[s[i-len(p)]]
            if s[i] not in cur_dict: cur_dict[s[i]]=1
            else: cur_dict[s[i]]+=1
            if cur_dict==my_dict: res.append(i-(len(p)-1))
        return res


#O(n) Sliding Window, a more concise version, using array to imitate hash_table
class Solution(object):
    def findAnagrams(self,s,p):
        p_hash,s_hash,res,n,m=[0]*256,[0]*256,[],len(s),len(p)
        if n<m: return res
        for c in p: p_hash[ord(c)]+=1  #Make hash_talbe for p
        for i in range(m): s_hash[ord(s[i])]+=1#Pre-load sliding window
        if s_hash==p_hash: res.append(0)#Corner case: pre_loaded hash table==p's hash table
        for i in range(m,n): #Moving sliding window
            s_hash[ord(s[i])]+=1
            s_hash[ord(s[i-m])]-=1
            if s_hash==p_hash: res.append(i-m+1)
        return res
            
            
        
        










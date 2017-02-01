
#My using sort solution:
class Solution(object):
    def frequencySort(self, s):
        #:type s: str
        #:rtype: str
        if(len(s)<=2): return s
        my_dict,result={},""
        for c in s: #build the dictionary for s, key is c, value is occurance number
            my_dict[c]=my_dict.get(c,0)+1
        vals=sorted(my_dict.values(),reverse=True) #notice reverse=true
        for val in vals:
            key_index=my_dict.values().index(val)
            result+=my_dict.keys()[key_index]*val #notice the () after keys()
            del my_dict[my_dict.keys()[key_index]] #do not miss my_dict.keys()
        return result


#My using sort solution 2:
class Solution(object):
    def frequencySort(self, s):
        if len(s)<=2: return s
        my_dict,result={},""
        for c in s:
            my_dict[c]=my_dict.get(c,0)+1
        my_dict_list=sorted(my_dict.iteritems(), key=lambda d:d[1], reverse=True) #notice the use of iteritems() and lambda expression, and notice after sorting, my_dict is nolonger a dictionary, it's a list
        for key in my_dict_list:
            result+=key[0]*key[1]
        return result


#Bucket sort solution, average O(n):
class Solution(object):
    def frequencySort(self, s):
        my_dict,result={},""
        for c in s:
            my_dict[c]=my_dict.get(c,0)+1
        buckets=[[] for i in range(len(s)+1)] # notice the use of "[] for i in range(len(s)+1)"
        print(buckets)
        for key in my_dict:
            buckets[my_dict[key]].append(key)
        for i in range(len(s),0,-1):
            for j in range(len(buckets[i])):
                result+=buckets[i][j]*my_dict[buckets[i][j]]
        return result

        
        
        
        
        
        
            
        
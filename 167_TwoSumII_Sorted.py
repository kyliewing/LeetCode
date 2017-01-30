#My dictionary hash table version, One Time AC
class Solution(object):
    def twoSum(self, numbers, target):
        my_dict={}
        for i in range(len(numbers)):
            if numbers[i] in my_dict:
                return [my_dict[numbers[i]],i+1]
            else:
                my_dict[target-numbers[i]]=i+1
        
            
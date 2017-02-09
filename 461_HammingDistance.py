#Build in function version:
class Solution(object):
    def hammingDistance(self, x, y):
        return bin(x^y).count('1')  #bin and count


# x&(x-1) version
class Solution(object):
    def hammingDistance(self, x, y):
        xor=x^y
        count=0
        while xor: #no more one remains
            count+=1  #plus the last one
            xor=xor & (xor-1) #delete the last one
        return count


        
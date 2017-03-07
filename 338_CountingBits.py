#My intuitive O(n*sizeof(integer)) solution, One Time AC.
class Solution(object):
    def countBits(self, num):
        #:type num: int
        #:rtype: List[int]
        res=[]
        for i in range(num+1):
            s=bin(i)[2:]
            bits=0
            for c in s:
                if c=='1':
                    bits+=1
            res.append(bits)
        return res

#How we handle this question on interview [Thinking process + DP solution], One Time AC.
class Solution(object):
    def countBits(self, num):
        res=[0]*(num+1)
        offset=1
        for i in range(1,num+1):
            if i==offset*2:
                offset*=2
            res[i]=res[i-offset]+1;
        return res


#An easy recurrence for this problem is f[i] = f[i / 2] + i % 2.
class Solution(object):
    def countBits(self, num):
        res=[0]*(num+1)
        for i in range(1,num+1):
            res[i]=res[i>>1]+(i&1)
        return res




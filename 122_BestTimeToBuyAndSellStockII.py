#My iterative version, not concise:
class Solution(object):
    def maxProfit(self, prices):
        #:type prices: List[int]
        #:rtype: int
        buy=sell=result=0
        i=0
        while sell<len(prices):
            while buy<len(prices)-1 and prices[buy+1]<prices[buy]:
                buy+=1
            if buy==len(prices)-1: return result  #Don't forget this line
            sell=buy+1
            while sell<len(prices)-1 and prices[sell+1]>prices[sell]:
                sell+=1
            result+=prices[sell]-prices[buy]
            buy=sell=sell+1
        return result

#Concise solution one:
class Solution(object):
    def maxProfit(self, prices):
        result=0
        for i in range(len(prices)-1):
            if prices[i+1]>prices[i]:
                result+=prices[i+1]-prices[i]
        return result


#List Comprehension version:
#Basically, if tomorrow's price is higher than today's, we buy it today and sell tomorrow. Otherwise, we don't.
class Solution(object):
    def maxProfit(self, pric1es):
        return sum([max(prices[i+1]-prices[i],0) for i in range(len(prices)-1)])
        
        
        
        
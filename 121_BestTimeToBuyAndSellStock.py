#"Array" "Dynamic Programing"
#Say you have an array for which the ith element is the price of a given stock on day i.
#If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.
#Example 1: Input: [7, 1, 5, 3, 6, 4] Output: 5
#max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger than buying price)


# Time Limit Exceeded ! O(n^2)
class Solution(object):
    def maxProfit(self, prices):
        if len(prices) in [0,1]: return 0
        res=max([max(prices[i+1:])-prices[i] for i in range (len(prices)-1)])
        return res if res>0 else 0



#Similar to "Max Subarray Problem", "Kadane's algorithm"
#Your runtime beats 99.52% of python submissions.
class Solution(object):
    def maxProfit(self, prices):
        buy,profit=-1,0 #Notice initialize buy<min(prices) and profit=0
        for i in range(len(prices)-1):
            if prices[i]>=prices[i+1]: continue#if the later one lower than the former one, nothing to do
            buy=prices[i] if buy==-1 else min(buy,prices[i])#maintain buy as the lowest price for now
            profit=prices[i+1]-prices[i] if profit==0 else max(profit,prices[i+1]-buy)#maintain profit as the most profit for now
        return profit
            
            
#A concise version.
#Your runtime beats 94.48% of python submissions.
class Solution(object):
    import sys
    def maxProfit(self, prices):
        min_buy,max_profit=sys.maxint,0 #Notice initialize buy=maxint and profit=0
        for i in range(len(prices)):
            min_buy=min(min_buy,prices[i])#maintain buy as the lowest price for now
            max_profit=max(max_profit,prices[i]-min_buy)#maintain profit as the most profit for now
        return max_profit
            
            
            
#Dynamic Programming version.
#Your runtime beats 81.30% of python submissions.
class Solution(object):
    def maxProfit(self, prices):
        if len(prices) in [0,1]: return 0 #corner case
        dp=[0]*len(prices) 
        min_buy=prices[0]
        for i in range(1,len(prices)):
            dp[i]=max(dp[i-1],prices[i]-min_buy)#fill the DP table
            min_buy=min(min_buy,prices[i])#maintain buy as the lowest price for now
        return dp[-1]
            
            
            
            
        
     
                
                    
            
            
                    
                    
                
                
            
            
            
            
        
                  
        
     
                
                    
            
            
                    
                    
                
                
            
            
            
            
        
                    
        
     
                
                    
            
            
                    
                    
                
                
            
            
            
            
        
        
        
        

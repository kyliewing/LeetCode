class Solution(object):
    def convert(self, s, numRows):
        if(numRows==1 or numRows>=len(s)):
            return s
        res=[""]*numRows
        period=2*(numRows-1)
        for row in range(numRows):
            index=row
            if row==0 or row==numRows-1:
                while(index<len(s)):
                    res[row]+=s[index]
                    index+=period
            else:
                while(index<len(s)):
                    res[row]+=s[index]
                    if index+(2*(numRows-row-1))<len(s):
                        res[row]+=s[index+(2*(numRows-row-1))]
                    index+=period
        return "".join(res)
                    
                
        

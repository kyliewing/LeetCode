#"Math" "String"
#Given an integer, convert it to a roman numeral. Input is guaranteed to be within the range from 1 to 3999.
#Symbol I   V   X   L   C   D   M
#Value  1   5   10  50  100 500 1,000

#My list version
#Your runtime beats 83.57% of python submissions.
class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        roman=[['M',1000],['CM',900],['D',500],['CD',400],['C',100],['XC',90],['L',50],['XL',40],['X',10],['IX',9],['V',5],['IV',4],['I',1]]
        res=""
        for symbol in roman:
            res+=symbol[0]*(num//symbol[1])
            num%=symbol[1]
        return res
        
        
###################################################
#Simple version
#Your runtime beats 87.44% of python submissions.
class Solution(object):
    def intToRoman(self, num):
        M= ["", "M", "MM", "MMM"]
        C= ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        X= ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        I= ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        return M[num/1000]+C[(num%1000)/100]+X[(num%100)/10]+I[(num%10)]
        
        


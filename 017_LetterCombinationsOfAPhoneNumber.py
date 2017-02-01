Python

#My iterative solution, One Time AC
class Solution(object):
    def letterCombinations(self, digits):
        if len(digits)==0: return []
        my_dict={'0':[' '],'1':['*'],'2':['a','b','c'],'3':['d','e','f'],'4':['g','h','i'],'5':['j','k','l'],'6':['m','n','o'],'7':['p','q','r','s'],'8':['t','u','v'],'9':['w','x','y','z']}
        combs=my_dict[digits[0]]
        for i in range(1,len(digits)):
            temp=[]
            for char in combs:
                for next_char in my_dict[digits[i]]:
                    temp.append(char+next_char)
            combs=temp
        return combs

#My recursive solution
class Solution(object):
    def letterCombinations(self,digits):
        
#My iterative queue version

        
                
                
            
            
C++
class Solution {
public:
    vector<string> letterCombinations(string digits) {
        vector<string> result;
        if (digits.empty()) {return result;}
        static const vector<string> mapp={" ","*","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"};
        result.push_back("");
        for (int i=0; i<digits.size(); i++){
            int num=digits[i]-'0';
            if (num<0 || num>9){ continue;}
            const string& candidate=mapp[num];
            vector<string> temp;
            for (int j=0; j<result.size(); j++){
                for (int k=0; k<candidate.size(); k++){
                    temp.push_back(result[j]+candidate[k]);
                }
            }
            result=temp;//or result.swap(temp);
            
        }
        return result;
        
    }
};
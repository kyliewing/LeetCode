#My solution:
class Solution(object):
    def fizzBuzz(self, n):
        #:type n: int
        #:rtype: List[str]
        result=[]
        for i in range(1,n+1):
            if i%15==0:
                result+=["FizzBuzz"]
            elif i%3==0:
                result+=["Fizz"]
            elif i%5==0:
                result+=["Buzz"]
            else:
                result+=[str(i)]
        return result

#My solution:
class Solution(object):
    def fizzBuzz(self,n):
        result=[]
        for i in range(1,n+1):
            if i%15==0:
                result.append("FizzBuzz")
            elif i%3==0:
                result.append("Fizz")
            elif i%5==0:
                result.append("Buzz")
            else:
                result.append(str(i))
        return result

#List comprehension verison:
class Solution(object):
    def fizzBuzz(self,n):
        return ["Fizz"*(not i%3)+"Buzz"*(not i%5) or str(i) for i in range(1,n+1)]
                
                
                
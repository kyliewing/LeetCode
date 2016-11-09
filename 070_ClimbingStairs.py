#"Dynamic Programming"
#You are climbing a stair case. It takes n steps to reach to the top.
#Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

#My recusive without repeated computing version, it's top-down approach(recursive)
#Your runtime beats 92.73% of python submissions.
class Solution(object):
    __results={} #Use dictionary to void repeated computing
    def climbStairs(self, n):
        if n in [0,1]:                #Termination case
            if n not in self.__results:
                self.__results[n]=1
            return 1
        else:
            if n-2 not in self.__results:
                self.__results[n-2]=self.climbStairs(n-2) #Add n-2 to the dictionary
            if n-1 not in self.__results:
                self.__results[n-1]=self.climbStairs(n-1) #Add n-1 to the dictionary
            return self.__results[n-1]+self.__results[n-2] #Basic recursive idea
        

#Bottom-up approach(iterative version)
#Your runtime beats 92.73% of python submissions.
class Solution(object):
    def climbStairs(self, n):
        if n in [0,1]: return 1              #Termination case
        one_step_before=1                    #always maintain one_step_before and two_step_before
        two_step_before=1
        for i in range(1,n):
            temp=one_step_before+two_step_before
            two_step_before=one_step_before
            one_step_before=temp
        return temp
            

#Bottom-up approach(iterative version), a concise version
#Your runtime beats 80.22% of python submissions.
class Solution(object):
    def climbStairs(self, n):
        one_step_before=two_step_before=1
        for _ in range(n-1):
            one_step_before,two_step_before=one_step_before+two_step_before,one_step_before
        return one_step_before #if n=0 or n=1, the program will return one_step_before directly without for loop


#Bottom-up approach(iterative version), a concise version with array
#Your runtime beats 100.00% of python submissions.
class Solution(object):
    def climbStairs(self, n):
        steps=[1,1]
        for i in range(2,n+1):
            steps.append(steps[i-1]+steps[i-2])
        return steps[n]


###########?????????????
#O(log(n)) solution with matrix multiplication
#I saw most solutions posted in discussion are DP with runtime O(n) and O(1) space which is accepted by OJ.
#The only O(log(n)) solution so far is lucastan's using Binet's formula.
#There actually is a matrix multiplication solution which also runs in O(log(n)). 
#It basically calculates fibonacci numbers by power of matrix ((0, 1), (1, 1)) ^ (n-1).
   public int climbStairs1(int n) {
    int[][] a = {{0, 1}, {1, 1}};
    int[][] m = pow(a, n - 1);
    return m[0][1] + m[1][1];
}

private int[][] pow(int[][] a, int n) {
    int[][] ret = {{1, 0}, {0, 1}};
    while (n > 0) {
        if ((n & 1) == 1) {
            ret = multiply(ret, a);
        }
        n >>= 1;
        a = multiply(a, a);
    }
    return ret;
}

private int[][] multiply(int[][] a, int[][] b) {
    int[][] c = new int[2][2];
    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 2; j++) {
            c[i][j] = a[i][0] * b[0][j] + a[i][1] * b[1][j];
        }
    }
    return c;
}








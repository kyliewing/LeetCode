#My solution, can be proved by Induction:
class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if 1<=n%4<=3:#Theorem: The first one who got the number that is multiple of 4 (i.e. n % 4== 0) will lost, otherwise he/she will win.
            return True
        else:
            return False
            

        
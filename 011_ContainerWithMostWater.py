#Two Pointers version
#Your runtime beats 84.29% of python submissions.
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i,j,max_area=0,len(height)-1,0
        while i<j:
            max_area=max(max_area,(j-i)*min(height[i],height[j]))
            if height[i]<height[j]:i+=1
            else: j-=1
        return max_area
            
        
            
        

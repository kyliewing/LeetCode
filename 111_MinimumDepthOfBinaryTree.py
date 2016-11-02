#"Tree" "DFS" "BFS"
#Given a binary tree, find its minimum depth.
#The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#Recursive version, DFS, O(N).
#Your runtime beats 92.97% of python submissions.
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0#Empty node
        if not root.left and not root.right: return 1 #Leaf node
        if not root.left or not root.right: return max(self.minDepth(root.left),self.minDepth(root.right))+1#Only one child
        return min(self.minDepth(root.left),self.minDepth(root.right))+1#Two children
        

#Iterative version, BFS, use queue, O(N).
#Your runtime beats 99.12% of python submissions.
from collections import deque
class Solution(object):
    def minDepth(self, root):
        if not root: return 0
        my_queue,h=deque([root]),1 
        while my_queue:  
            for i in range(len(my_queue)):  #Do not miss range()
                temp=my_queue.popleft()
                if not temp.left and not temp.right: #If meet the first leaf node, then return the current height
                    return h
                if temp.left: my_queue.append(temp.left)
                if temp.right: my_queue.append(temp.right)
            h+=1

#Recursive version, DFS, O(n)
#Your runtime beats 49.05% of python submissions.
class Solution(object):
    def minDepth(self, root):
        if not root: return 0
        left=self.minDepth(root.left) #Do not miss self.
        right=self.minDepth(root.right)
        if left==0 or right==0: return max(left,right)+1
        return min(left,right)+1
        

#Recursive version, DFS, O(n)
#Your runtime beats 82.72% of python submissions.
class Solution(object):
    def minDepth(self, root):
        if not root: return 0
        if root.left and root.right: return min(self.minDepth(root.left),self.minDepth(root.right))+1
        else: return max(self.minDepth(root.left),self.minDepth(root.right))+1
        
        
#Recursive version, DFS, O(n)
#Your runtime beats 82.72% of python submissions.
class Solution(object):
    def minDepth(self, root):
        if not root: return 0
        depths=map(self.minDepth,(root.left,root.right))
        return min(depths) or max(depths) #Notice the usage of "or"
        
        
        
        
                
        
                
        
        
                
        
        
        
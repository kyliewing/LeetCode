#"Tree" "DFS"
#Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#My recursive version, DFS, O(n).
#Your runtime beats 89.53% of python submissions.
class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root: return False
        if root.left==None and root.right==None: return sum==root.val #Leaf node
        if root.left==None: return self.hasPathSum(root.right,sum-root.val) #Only right child
        if root.right==None: return self.hasPathSum(root.left,sum-root.val) #Only left child 
        return self.hasPathSum(root.left,sum-root.val)  or self.hasPathSum(root.right,sum-root.val) #Two children



        
        
        
        
        
        
        
        
        
        
        
        

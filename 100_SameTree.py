#"Tree" "Depth-First Search"
#Given two binary trees, write a function to check if they are equal or not.
#Two binary trees are considered equal if they are structurally identical and the nodes have the same value.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#Your runtime beats 46.75% of python submissions.
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p==None and q==None: return True
        if (p==None)!=(q==None): return False
        if p and q:
            return (p.val==q.val) and (self.isSameTree(p.left,q.left)) and (self.isSameTree(p.right,q.right))
        
        
        

#Non-Recursive Version, usting Stack to do DFS:
#Your runtime beats 83.67% of python submissions.
class Solution(object):
    def isSameTree(self, p, q):
        stack=[(p,q)]  #Initialize a stack and append roots tuple
        while stack:
            pp,qq=stack.pop()  #Deal with the top tuple
            if pp==None and qq==None:#If both are None, then deal with the next tuple
                continue
            if pp==None or qq==None:#If only one is None, then p and q have different sturcture, return false
                return False
            if pp.val==qq.val:#If the sturcture is the same for now, check the value
                stack.append((pp.left,qq.left))#If the value is the same, push left and right children into stack. Notice do not miss extra () for tuple
                stack.append((pp.right,qq.right))
            else:
                return False
        return True
                
        
        
        
        
        
        
        
        
        
                
        
        
        
        
        
        
        
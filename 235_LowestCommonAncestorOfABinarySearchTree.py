
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#My Recursively Version (DFS): 
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        if root==None: return None
        if min(p.val,q.val)<=root.val<=max(p.val,q.val): return root.val
        else: 
            return self.lowestCommonAncestor(root.left,p,q) or self.lowestCommonAncestor(root.right,p,q)
            

#My Iterative Version (BFS):
class Solution(object):
    def lowestCommonAncestor(self,root,p,q):
        while root:
            if p.val<root.val>q.val:
                root=root.left
            elif p.val>root.val<q.val:
                root=root.right
            else:
                return root










        
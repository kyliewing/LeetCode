#My recursive version, DFS
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        #:type root: TreeNode
        #:rtype: TreeNode
        if not root: return root
        else:
            return self._helper(root)
    
    def _helper(self,node):
        if node==None: 
            return node
        if node.left==None and node.right==None:
            return node
        else:
            node.left,node.right=self._helper(node.right),self._helper(node.left)
            return node
            

#My iterative version, DFS
class Solution(object):
    def invertTree(self,root):
        if not root: return root
        my_stack=[root]
        while my_stack:
            temp=my_stack.pop()
            temp.left,temp.right=temp.right,temp.left
            if temp.left:
                my_stack.append(temp.left)
            if temp.right:
                my_stack.append(temp.right)
        return root


#My iterative version, BFS, One Time AC
class Solution(object):
    def invertTree(self,root):
        if not root: return root
        my_queue=[root]
        while my_queue:
            temp=my_queue.pop(0)
            temp.left,temp.right=temp.right,temp.left
            if temp.left:
                my_queue.append(temp.left)
            if temp.right:
                my_queue.append(temp.right)
        return root
            
        
        
        
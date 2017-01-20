#"Tree" "DFS" "BFS"
#Bonus points if you could solve it both recursively and iteratively.
#Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


#My Recursive Version:
class Solution(object):
    def isSymmetric(self, root):
        if root==None: return True#Notice to deal with the case where root is empty
        return self.helper(root.left,root.right)#Use the helper function to determine whether left and right are symmetric or not
    def helper(self,left,right):
        if left==None or right==None: return left==right  #One of the node is None
        if left.val!=right.val: return False #The values of left and right are not equal
        return self.helper(left.left,right.right) and self.helper(left.right,right.left) #then we need to decide left.left&right.right and left.right&right.left
        

#DFS (using stack) Iterative Version:
class Solution(object):
    def isSymmetric(self,root):
        if root==None: return True#When the root is empty
        stack=[(root.left,root.right)]
        while stack:
            left,right=stack.pop()
            if left==None and right==None:
                continue
            if left==None or right==None:
                return False
            if left.val!=right.val: return False
            else: 
                stack.append((left.left,right.right))
                stack.append((left.right,right.left))
        return True
                
#BFS(using queue) Iterative version:
class Solution(object):
    def isSymmetric(self,root):
        if root==None: return True
        queue=[(root.left,root.right)]
        while queue:
            left,right=queue.pop(0)
            if left==None and right==None: continue
            if left==None or right==None: return False
            if left.val!=right.val: return False
            else:
                queue.append((left.left,right.right))
                queue.append((left.right,right.left))
        return True
        
        
        
        
        
        
        
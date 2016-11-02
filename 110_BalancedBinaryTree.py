#"Tree" "DFS"
#Given a binary tree, determine if it is height-balanced.
#For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#My Recursive version, DFS, by using the helper function depth function, O(n^2).
#Your runtime beats 38.31% of python submissions.(One Time AC)
#For the current node root, calling depth() for its left and right children actually has to access all of its children, thus the complexity is O(N). We do this for each node in the tree, so the overall complexity of isBalanced will be O(N^2). This is a top down approach.
class Solution(object):
    def _depth(self,root):
        if not root: return 0
        return max(self._depth(root.left),self._depth(root.right))+1
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root: return True
        return self.isBalanced(root.left) and self.isBalanced(root.right) and max(self._depth(root.left),self._depth(root.right))-min(self._depth(root.left),self._depth(root.right))<=1
        
        
#My Recursive version, DFS, by using the helper function depth function.
#Your runtime beats 54.23% of python submissions.(One Time AC)
class Solution(object):
    def _depth(self,root):
        if not root: return 0
        return max(self._depth(root.left),self._depth(root.right))+1
    def isBalanced(self, root):
        if not root: return True
        return self.isBalanced(root.left) and self.isBalanced(root.right) and abs(self._depth(root.left)-self._depth(root.right))<=1
                 
        
#My Recursive version, DFS, O(n)(Each node is visited only once).
#Your runtime beats 92.82% of python submissions.(One Time AC)
class Solution(object):
    def _dfsHeight(self,root):
        if not root: return 0
        left_height=self._dfsHeight(root.left)
        right_height=self._dfsHeight(root.right)
        if left_height==-1: return -1  #It menas the left sub tree is not balanced
        if right_height==-1: return -1 #It means the right sub tree is not balanced
        if abs(left_height-right_height)>1: return -1 #It means the current node is not balancde
        return max(left_height,right_height)+1 #It means the tree is balancde so far, so we return the height(non-negative)
    def isBalanced(self, root):
        return self._dfsHeight(root)!=-1  #"-1" represents not balanced
                 

####?########################################???????
class Solution(object):
    def isBalanced(self, root):
        stack, node, last, depths = [], root, None, {}
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack[-1]
                if not node.right or last == node.right:
                    node = stack.pop()
                    left, right  = depths.get(node.left, 0), depths.get(node.right, 0)
                    if abs(left - right) > 1: return False
                    depths[node] = 1 + max(left, right)
                    last = node
                    node = None
                else:
                    node = node.right
        return True

        
        
        
        
        
        
        
        
        
        
        
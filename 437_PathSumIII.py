"""
Each time find all the path start from current node
Then move start node to the child and repeat.
Time Complexity should be O(N^2) for the worst case and O(NlogN) for balanced binary Tree.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#Naive recursion, start from every node. TLE.
class Solution(object):
    def pathSum(self, root, sum):

        #:type root: TreeNode
        #:type sum: int
        #:rtype: int
        if root==None: return 0
        path=[]
        return self.findPath(root,sum,path)+self.pathSum(root.left,sum)+self.pathSum(root.right,sum)
        
    def findPath(self,root,sum,path):
        res=0
        if root==None:
            return res
        if root.val==sum:
            res+=1
            #print path+[root.val]
        res+=self.findPath(root.left,sum-root.val,path+[root.val])
        res+=self.findPath(root.right,sum-root.val,path+[root.val])
        return res

#DFS from root, maintain the path, trackback the path to find sum at every node. O(nlogn), n for n nodes, logn for trackback.
class Solution(object):
    def pathSum(self, root, sum):
        #:type root: TreeNode
        #:type sum: int
        #:rtype: int
        if root==None: return 0
        path=[]
        return self.findPath(root,sum,path)
        
    def findPath(self,root,sum,path):
        res=0
        if root==None:
            return 0
        #if root.val==sum:
        #    res+=1
            #print path+[root.val]
        temp_path=path+[root.val]
        temp_sum=0
        for i in range(len(temp_path)-1,-1,-1):
            temp_sum+=temp_path[i]
            if temp_sum==sum:
                #print temp_path[i:]
                res+=1
        res+=self.findPath(root.left,sum,path+[root.val])
        res+=self.findPath(root.right,sum,path+[root.val])
        return res
        
        
        
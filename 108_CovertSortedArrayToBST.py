# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#One time AC.
class Solution(object):
    def sortedArrayToBST(self, nums):
        #:type nums: List[int]
        #:rtype: TreeNode
        nums_length=len(nums)
        if nums_length==0: return None
        elif nums_length==1: return TreeNode(nums[0])
        else:
            mid=(0+nums_length-1)/2
            root_node=TreeNode(nums[mid])
            root_node.left=self.sortedArrayToBST(nums[:mid])
            root_node.right=self.sortedArrayToBST(nums[mid+1:])
            return root_node
           
class Solution:
    # @param num, a list of integers
    # @return a tree node
    def sortedArrayToBST(self, num):
        if not num:
            return None
        mid = len(num) // 2
        
        root = TreeNode(num[mid])
        root.left = self.sortedArrayToBST(num[:mid])
        root.right = self.sortedArrayToBST(num[mid+1:])
        
        return root
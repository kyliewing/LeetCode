#We can't really delete the node, but we can kinda achieve the same effect by instead removing the next node after copying its data into the node that we were asked to delete.
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        if node and node.next:
            node.val=node.next.val
            node.next=node.next.next
        
        
        
        
        
        
        
        
        
        
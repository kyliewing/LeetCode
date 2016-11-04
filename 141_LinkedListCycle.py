#"Linked List" "Two Pointers"
#Given a linked list, determine if it has a cycle in it.
#Follow up: Can you solve it without using extra space?

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#################!!!!!!!!!!
'''
class Solution(object):
    def hasCycle(self, head):
'''

#Two Pointers Version
#Your runtime beats 66.89% of python submissions.
#Use two pointers, walker and runner. walker moves step by step. runner moves two steps at time.
#if the Linked List has a cycle walker and runner will meet at some point.
class Solution(object):
    def hasCycle(self, head):
        if not head: return False
        walker=runner=head
        while runner.next!=None and runner.next.next!=None:
            walker=walker.next
            runner=runner.next.next
            if walker==runner: return True
        return False
        
        
        
#Two Pointers Version
#Your runtime beats 41.38% of python submissions.
class Solution(object):
    def hasCycle(self, head):
        try:
            walker=head
            runner=head.next
            while walker is not runner:
                walker=walker.next
                runner=runner.next.next
            return True
        except:
            return False
        
        
        
#The program gives every visited node a sign by pointing next to the node itself.
#Your runtime beats 35.26% of python submissions.
class Solution(object):
    def hasCycle(self, head):
        if head==None or head.next==None: return False
        if head.next==head: return True
        next_node=head.next
        head.next=head
        return self.hasCycle(next_node)
        
        
        
        
        
        
        
        
        
        
        
               
        
        
        
        
        
        
        
        
               
        
        
        
        
        
        
        
        
        
        
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#My in-place solution, One Time AC.
class Solution(object):
    def oddEvenList(self, head):
        #:type head: ListNode
        #:rtype: ListNode
        if not head or not head.next: return head
        odd,odd_temp,even,even_temp=head,head,head.next,head.next
        while odd_temp.next and odd_temp.next.next:
            odd_temp.next=odd_temp.next.next
            odd_temp=odd_temp.next
            even_temp.next=even_temp.next.next
            even_temp=even_temp.next
        odd_temp.next=even
        return odd
        
        
        
        
        
 
        
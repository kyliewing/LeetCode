# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#My solution, One Time AC.
class Solution(object):
    def removeElements(self, head, val):
        #:type head: ListNode
        #:type val: int
        #:rtype: ListNode
        dummy=pre=ListNode(0)
        pre.next=head
        temp=head
        while temp:
            if temp.val==val:
                temp=temp.next
                pre.next=temp
            else:
                pre=pre.next
                temp=temp.next
        return dummy.next

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#My Iterative version:
class Solution(object):
    def reverseList(self, head):
        temp,pre=head,None
        while temp:
            pre,temp.next,temp=temp,pre,temp.next
        return pre


        
#My Iterative version:
class Solution(object):
    def reverseList(self, head):
        temp,pre=head,None
        while temp:
            cur=temp
            temp=temp.next
            cur.next=pre
            pre=cur
        return pre

        
#Recursive version:
class Solution(object):
    def reverseList(self, head):
        return self._reverse(head,None)
        
    def _reverse(self,head,pre):
        if not head: return pre
        temp=head.next
        head.next=pre
        return self._reverse(temp,head)
     
        
        
        
        
        
        
        
        
        
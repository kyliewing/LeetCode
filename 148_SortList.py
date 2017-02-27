# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#Merge sort version. O(nlogn)time, O(1)space
class Solution(object):
    def sortList(self, head):
        #:type head: ListNode
        #:rtype: ListNode
        if not head or not head.next: return head
        #split the list into two halves
        pre=slow=fast=head
        while fast and fast.next: #notice this condition
            pre=slow
            slow=slow.next
            fast=fast.next.next
        pre.next=None #add a None node at the end of left half list
        #sort the two halves    
        l1=self.sortList(head)
        l2=self.sortList(slow)
        #merge the two halves
        return self.merge(l1,l2)
    
    #merge two sorted list
    def merge(self,l1,l2):
        temp=dummy=ListNode(0)
        while l1 and l2:
            if l1.val<l2.val:
                temp.next=l1
                temp,l1=temp.next,l1.next
            else:
                temp.next=l2
                temp,l2=temp.next,l2.next
        if l1:
            temp.next=l1
        if l2:
            temp.next=l2
        return dummy.next
                
            
            
            
            
            
            
            
            
        
        
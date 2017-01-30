
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#My reverse 2nd half linked list version.
class Solution(object):
    def isPalindrome(self, head):
        temp,count=head,0
        while temp: #count the number of nodes in head
            count+=1
            temp=temp.next
        temp,pre=head,None
        for _ in range(count/2): temp=temp.next#from count/2 step beyond head
        while temp:#reverse 2nd half list
            cur=temp
            temp=temp.next
            cur.next=pre
            pre=cur
        temp=head
        while pre:#compare reversed 2nd half list with 1st half list
            if pre.val!=temp.val: return False
            pre,temp=pre.next,temp.next
        return True
            
        
        
        
            
        
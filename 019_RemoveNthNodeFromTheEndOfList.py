#Your runtime beats 7.16% of python submissions.
#Given a linked list, remove the nth node from the end of list and return its head.
#Given n will always be vaild, try to do this in one pass
#class ListNode(object):
#    def __init__(self,x):
#        self.val=x
#        self.next=None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        Hhead=ListNode(1)#Create a new node and append infront of the head
        Hhead.next=head
        temp=head
        former=Hhead
        if head.next==None:#Consider the case where there is only one element in the linked list
            return None
        while True: #It's "True" not "true", and it's "False" not "false"
            tail=temp
            for i in range(n):
                tail=tail.next
            if tail==None:
                break
            temp=temp.next
            former=former.next
        if temp==head: #It's "==" not "="
            head=head.next
            return head
        else:
            former.next=former.next.next #Delete temp
            return head
            
            
    
            
        
        
        
        
#Your runtime beats 32.00% of python submissions.
#Given a linked list, swap every two adjacent nodes and return its head.
#Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
    def swapPairs(self, head):
        if head==None or head.next==None:#For 1 or 2 nodes
            return head
        temp=head
        head=temp.next    #Change of Head
        while True:
            first=temp    #Four nodes are a group
            temp=temp.next
            second=temp
            third=None
            fourth=None
            
            if temp.next!=None:
                temp=temp.next
                third=temp
                if temp.next!=None:
                    temp=temp.next
                    fourth=temp
                    
            second.next=first  
            if fourth:   #If the remaining nodes are more than or equal to four
                first.next=fourth
                temp=third
                continue
            elif third: #If the remaining nodes are three
                first.next=third
                third.next=None
                break
            else:      #If the remaining nodes are two
                first.next=None
                break
        return head
        
                
                
                
                
                
            
            
            
        
        
#"Linked List" "Recursion"
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
        
                
#Your runtime beats 57.55% of python submissions.
#Recursively version:
class Solution(object):
    def swapPairs(self, head):
        if head==None or head.next==None:#For 1 or 2 nodes
            return head
        second=head.next               
        head.next=self.swapPairs(second.next)#Call itself recursively Notice the order between this line and the next line, otherwise the recursion will be infinite
        second.next=head#Swap the first node and the second node
        return second
        
                
                
#Your runtime beats 40.52% of python submissions.
#Iteratively version 1:
class Solution(object):
    def swapPairs(self, head):
        dummy=p1=ListNode(0)        #Initialize a dummy node
        dummy.next=head             #Connect the dummy node to head
        try:                        #Try to do the loop
            while True:
                p0,p1,p2=p1,p1.next,p1.next.next  #deal with previous node, first node and second node
                p0.next,p1.next,p2.next=p2,p2.next,p1 #Connect to the next node and reassign p1 to prepare the next loop
        except:
            return dummy.next       #If try fails, then we only left one node or zero node, where p1 already pointed to the last one or zero node
                
                           
#Your runtime beats 57.55% of python submissions.
#Iteratively version 2:
class Solution(object):
    def swapPairs(self, head):
        dummy=pre=ListNode(0)        #Initialize a dummy node
        dummy.next=head             #Connect the dummy node to head
        while head and head.next:
            first,second=head,head.next
            pre.next,head,first.next,second.next,pre=second,second.next,second.next,first,first
        return dummy.next
                
                
        
                
                
                
                
                
            
            
            
        
                    
        
                        
                
                
                
                
            
            
            
        
        
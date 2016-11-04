#"Linked List" "Math"
#You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#My solution:
#Your runtime beats 99.47% of python submissions.
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        if l1==None or l2==None: return l1 or l2
        l3=ListNode(0)
        temp1,temp2,temp3,crr=l1,l2,l3,0#Do not miss to define and initialize crr
        while temp1 or temp2 or crr:
            temp3.val+=1 if crr else 0
            if temp1:
                temp3.val+=temp1.val
                temp1=temp1.next
            if temp2:
                temp3.val+=temp2.val
                temp2=temp2.next
            crr=1 if temp3.val>=10 else 0
            temp3.val%=10
            if temp1 or temp2 or crr: #Do not forget to check before create the new node in l3
                temp3.next=ListNode(0)
                temp3=temp3.next
        return l3
            
            
#More concise version
#Your runtime beats 94.78% of python submissions.
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        l3=temp3=ListNode(0)
        carry=0
        while l1 or l2 or carry:
            v1=v2=0
            if l1:
                v1=l1.val
                l1=l1.next
            if l2:
                v2=l2.val
                l2=l2.next
            carry,val=divmod(v1+v2+carry,10) #Notice the usage of divmod
            temp3.next=ListNode(val)
            temp3=temp3.next
        return l3.next
            
            
            
            
            
            
            
            
            
            
            
            
            
                   
            
            
            
            
            
            
            
            
            
        
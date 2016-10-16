#Your runtime beats 49.72% of python submissions. (One Time AC)
#Need to confirm ascending order or descending order
#Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.      

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        temp1=l1
        temp2=l2
        if l2==None:      ##Need to check if l1 or l2 is None
            return l1
        elif l1==None and l2!=None:
            return l2
        if l1.val<=l2.val:
            res_head=l1
            temp1=temp1.next
        else:
            res_head=l2
            temp2=temp2.next
        temp_res=res_head
        while temp1 and temp2:
            if temp1.val<=temp2.val:
                temp_res.next=temp1
                temp1=temp1.next
                temp_res=temp_res.next
            else:
                temp_res.next=temp2
                temp2=temp2.next
                temp_res=temp_res.next
        if temp1!=None:
            while temp1:
                temp_res.next=temp1
                temp1=temp1.next
                temp_res=temp_res.next
        elif temp2!=None:
            while temp2:
                temp_res.next=temp2
                temp2=temp2.next
                temp_res=temp_res.next
        return res_head
                
        
                
                
                
        
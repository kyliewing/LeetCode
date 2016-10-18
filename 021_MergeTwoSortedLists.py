#"Linked List" "Recursion"
#Your runtime beats 49.72% of python submissions. (One Time AC)
#Need to confirm ascending order or descending order
#Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.      

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#My solution is not clean, and it's not the best solution
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


#Your runtime beats 79.48% of python submissions.
#Iteratively version:
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        dummy=cur=ListNode(0)  #A dummy Node
        while l1 and l2:       #While two lists are not empty
            if l1.val<l2.val:  #Cur point to the smaller one
                cur.next=l1
                l1=l1.next
            else:
                cur.next=l2
                l2=l2.next
            cur=cur.next       #Cur move one step
        cur.next=l1 or l2      #Cur point to the not empty one
        return dummy.next      #Return dummy.next
        
        
        
#Your runtime beats 49.72% of python submissions.
#Iteratively version(In place):
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        dummy=cur=ListNode(0)  #A dummy Node
        cur.next=l2            #Modify the l2 and ready to return l2
        while l1 and l2:       #While two lists are not empty
            if l2.val<l1.val:  #If l2<l1, just move l2 one step
                l2=l2.next
            else:              #If l1<l2, we need to insert one l1 node into the l2 chain
                cur.next=l1
                temp=l1.next
                l1.next=l2
                l1=temp
            cur=cur.next       #Cur move one step
        cur.next=l1 or l2      #Cur point to the not empty one
        return dummy.next      #Return dummy.next
                
        
#Your runtime beats 79.48% of python submissions.
#Recursively version:
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        if None in (l1,l2): #If one of the list is None, return the other list
            return l1 or l2
        if l1.val<l2.val:   #Return the pointer whose value is smaller
            l1.next=self.mergeTwoLists(l1.next,l2) #The recursively call itself 
            return l1
        else:
            l2.next=self.mergeTwoLists(l1,l2.next)
            return l2
        
                
        


                
        
                
                
                
        
#"Linked List" "Two pointers"
#Given a sorted linked list, delete all duplicates such that each element appear only once.

#Two pointers version:
#Your runtime beats 87.23% of python submissions.
class Solution(object):
    def deleteDuplicates(self, head):
        if not head: return head        #If the list is empty
        slow=fast=head                  #Initialize two pointers: slow and fast
        while fast:
            while fast and slow.val==fast.val: #Move fast
                fast=fast.next
            slow.next=fast              #slow pointe to fast
            slow=slow.next 
        return head
        

#Iterative version, one pointer:
#Your runtime beats 81.12% of python submissions.
class Solution(object):
    def deleteDuplicates(self, head):
        temp=head
        while temp:
            if temp.next==None: break
            if temp.val==temp.next.val: #If temp.val equals to temp.next.val
                temp.next=temp.next.next #Temp point to the next next one
            else:
                temp=temp.next          #not equal, temp move to temp.next
        return head
        
            
#Iterative version, one pointer:
#Your runtime beats 44.95% of python submissions.
class Solution(object):
    def deleteDuplicates(self, head):
        temp=head
        while temp and temp.next:
            if temp.val==temp.next.val:
                temp.next=temp.next.next
            else:
                temp=temp.next
        return head


#Two while version:
#Your runtime beats 65.43% of python submissions.
class Solution(object):
    def deleteDuplicates(self, head):
        temp=head
        while temp:
            while temp.next and temp.val==temp.next.val:
                temp.next=temp.next.next
            temp=temp.next
        return head
        
            

       
        

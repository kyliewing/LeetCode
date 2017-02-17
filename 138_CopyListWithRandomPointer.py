# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

#Hash_Table Version:
#Each tuple of the hash table is a node from the original list and a node from the copy list
class Solution(object):
    def copyRandomList(self, head):
        #:type head: RandomListNode
        #:rtype: RandomListNode
        my_hash={}
        my_hash[None]=None  #Deal with the situation where head is None
        temp=head
        while temp:  #put each tuple nodes into the hash table
            my_hash[temp]=RandomListNode(temp.label)
            temp=temp.next
        temp=head
        while temp:
            my_hash[temp].next=my_hash[temp.next]
            my_hash[temp].random=my_hash[temp.random]
            temp=temp.next
        return my_hash[head]
            
#None hash_table, Three Scans version:
class Solution(object):
    def copyRandomList(self, head):
        if not head: return None
        temp=head
        while temp: #First scan, insert a new node after every original node
            next_node=temp.next
            temp.next=RandomListNode(temp.label)
            temp.next.next=next_node
            temp=next_node
        temp=head 
        while temp: #Second scan, assign random node to each new node
            new_temp=temp.next
            new_temp.random=temp.random.next if temp.random else None  #note the situation when random is None
            temp=temp.next.next
        temp=head
        new_head=temp.next
        while temp: #Third scan, split the list to original list and copy list
            next_node=temp.next
            temp.next=temp.next.next
            next_node.next=next_node.next.next if next_node.next else None #note the situation when new node's next is None
            temp=temp.next
        return new_head
            
            
        
        
        
        
        
            
            
            
            
            
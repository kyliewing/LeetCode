# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#My O(n) solution, need to know the lenght of A nad B
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        tempA,tempB,countA,countB=headA,headB,0,0
        while tempA:
            countA+=1
            tempA=tempA.next
        while tempB:
            countB+=1
            tempB=tempB.next
        diff=abs(countA-countB)
        tempA,tempB=headA,headB
        if countA<countB: 
            for _ in range(diff):
                tempB=tempB.next
        elif countB<countA:
            for _ in range(diff):
                tempA=tempA.next
        while tempB:
            if tempB==tempA:
                return tempA
            tempB=tempB.next
            tempA=tempA.next
        return None


        
#A smater O(n) solution, do not need to know the length of A and B
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        tempA,tempB=headA,headB
        if tempA==None or tempB==None: return None
        while tempA!=tempB:
            tempA=headB if tempA==None else tempA.next
            tempB=headA if tempB==None else tempB.next
        return tempA 
        
        
        
        
        
        
        
            
        
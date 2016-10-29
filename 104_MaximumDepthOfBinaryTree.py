#"Tree" "DFS" "BFS"
#Given a binary tree, find its maximum depth.
#The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#My Recursive Version(One Time AC):
#Your runtime beats 77.98% of python submissions.
class Solution(object):
    def maxDepth(self, root):
        if root==None: return 0
        return max(self.maxDepth(root.left),self.maxDepth(root.right))+1
        

#BFS level traversal(Queue), Iterative Version:
#Your runtime beats 99.68% of python submissions.
#Need to import collectioins module if we want to use deuqe structure
class Solution(object):
    def maxDepth(self, root):
    	import collections
        if not root: return 0  #If root is null
        my_queue=collections.deque()#Initialize queue and append root
        my_queue.append(root)
        h=0
        while my_queue: #While the level is not empty
            next_level=collections.deque() #Create a new queue for the next level
            while my_queue:#Delete element one by one and append its children into next level
                temp=my_queue.popleft()
                if temp.left: next_level.append(temp.left)
                if temp.right: next_level.append(temp.right)
            my_queue=next_level#Deal with the next level 
            h+=1#Level plus one
        return h
            
        
        
#BFS level traversal(Stack), similar to using Queue, Iterative Version:
#Your runtime beats 86.48% of python submissions.
class Solution(object):
    def maxDepth(self, root):
        if not root: return 0  #If root is null
        my_stack=[root]#Initialize stack and append root
        h=0
        while my_stack: #While the level is not empty
            next_level=[] #Create a new stack for the next level
            while my_stack:#Delete element one by one and append its children into next level
                temp=my_stack.pop()
                if temp.left: next_level.append(temp.left)
                if temp.right: next_level.append(temp.right)
            my_stack=next_level#Deal with the next level 
            h+=1#Level plus one
        return h
            
        

#BFS, level traversal, Only one queue, iterative version:
#Your runtime beats 77.98% of python submissions.
class Solution(object):
    def maxDepth(self, root): #The idea is that when we do BFS level traversal, the depth of the last node should be the maxinum depth of the tree
    	import collections
    	if not root: return 0
    	my_queue=collections.deque([(root,1)])  #Initialize it as a queue contains tuples as elements, the second number is the level
    	while my_queue:
    	    temp,val=my_queue.popleft()  #Pop tuple
    	    if temp.left: my_queue.append((temp.left,val+1)) #Append tuple
    	    if temp.right: my_queue.append((temp.right,val+1))
    	return val
    	
        
                    
        
        
                
       
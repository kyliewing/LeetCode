#"Tree" "BFS"
#Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).
#return its level order traversal as: [[3],[9,20],[15,7]](Null is missed)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#Iterative version, use queue.
#Your runtime beats 95.35% of python submissions.
from collections import deque  #Remember to import deque from collections
class Solution(object):
    def levelOrder(self, root):#The idea is using queue to do level traversal, maintain the result list at the same time
        if not root: return []
        my_queue=deque([root])#Notice the [] braket
        my_list=[root.val] #The first list element
        res=[]
        while my_queue:#While there is a non empty level
            res.append(my_list)#Append the list of next level
            new_queue,new_list=deque(),[]#Empty deque and list for the next level
            while my_queue:#Deal with each element in queue iteratively
                temp=my_queue.popleft()
                if temp.left: #Update queue and list 
                    new_queue.append(temp.left)
                    new_list.append(temp.left.val)
                if temp.right: 
                    new_queue.append(temp.right)
                    new_list.append(temp.right.val)
            my_queue=new_queue
            my_list=new_list
        return res
                
                

#My Iterative version, use queue, a simpler version.
#Your runtime beats 90.49% of python submissions.
from collections import deque  #Remember to import deque from collections
class Solution(object):
    def levelOrder(self, root):#The idea is using queue to do level traversal, maintain the result list at the same time
        if not root: return []
        my_queue=deque([root])#Notice the [] braket
        res=[]
        while my_queue:#While there is a non empty level
            new_queue,new_list=deque(),[]#Empty deque and list for the next level
            while my_queue:#Deal with each element in queue iteratively
                temp=my_queue.popleft()
                new_list.append(temp.val)
                if temp.left: #Update queue 
                    new_queue.append(temp.left)
                if temp.right: 
                    new_queue.append(temp.right)
            my_queue=new_queue
            res.append(new_list)
        return res
                
                

#My Iterative version 2, use queue, a simpler version.
#Your runtime beats 90.49% of python submissions.
from collections import deque  #Remember to import deque from collections
class Solution(object):
    def levelOrder(self, root):#The idea is using queue to do level traversal, maintain the result list at the same time
        if not root: return []
        my_queue,res=deque([root]),[]#Notice the [] braket
        while my_queue:#While there is a non empty level
            res.append(list(my_queue))         #Notice to convert deque object to list object by using list()
            new_queue=deque()#Empty deque and list for the next level
            while my_queue:#Deal with each element in queue iteratively
                temp=my_queue.popleft()
                if temp.left: #Update queue 
                    new_queue.append(temp.left)
                if temp.right: 
                    new_queue.append(temp.right)
            my_queue=new_queue
        return [[x.val for x in level] for level in res]#Use the property of python list comprehension
                
                
        
#Iterative version using python list comprehension: 
#Your runtime beats 88.22% of python submissions.
class Solution(object):
    def levelOrder(self, root):#The idea is append level as a list every time
        res,level=[],[root]
        while root and level: #Notice root condition
            res.append([node.val for node in level])#Append a new level
            lr_pair=[(node.left,node.right) for node in level]#For children of the current level
            level=[leaf for lr in lr_pair for leaf in lr if leaf]#New level are the leaves that are not empty, suing python list comprehension
        return res
        
                
                
#Iterative version 2 using python list comprehension: 
#Your runtime beats 98.16% of python submissions.
class Solution(object):
    def levelOrder(self, root):#The idea is append level as a list every time
        res,level=[],[root]
        while root and level: #Notice root condition
            res.append([node.val for node in level])#Append a new level
            level=[ kid for node in level for kid in (node.left, node.right) if kid]#New level are the leaves that are not empty, suing python list comprehension
        return res
        
                
                
 
#Iterative version using list no queue: 
#Your runtime beats 92.97% of python submissions.
class Solution(object):
    def levelOrder(self, root):
        if not root: return []
        res=[[root]]
        for level in res: #Notice the elements in res is changing
            new_list=[]
            for node in level:
                if node.left: new_list.append(node.left)
                if node.right: new_list.append(node.right)
            if new_list: res.append(new_list) #Notice to check if new_list is empty or not
        return [[node.val for node in level] for level in res]
        
        
###Recursive Version, using hasing table, python dictionary.
#Your runtime beats 53.19% of python submissions.
class Solution(object):
    def _level(self,root,level,dict_levels):
        if not root: return                        #If the node is none, just return nothing and terminate the recursion
        dict_levels[level]=dict_levels.get(level,[])+[root.val]#Append value to the corresponding level by using hasing table
        self._level(root.left,level+1,dict_levels)  #Must use self. here
        self._level(root.right,level+1,dict_levels)
    def levelOrder(self, root):
        d={}
        self._level(root,0,d)#Must use self. here
        return d.values()
        
        
        
    
        
        
        
        
        

                
                
        
        
        
        
        
        
        
        
        
        
        
        

        
        
        
        
        
        
        
        
        
        
        
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
                
        
        
        
        
        
        
        
        
        
        
        
                
        
        
        
        
        
        
        
        
        
        
        
        
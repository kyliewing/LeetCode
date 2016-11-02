#"Tree" "BFS"
#Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).
#For example:Given binary tree [3,9,20,null,null,15,7], return its bottom-up level order traversal as: [[15,7],[9,20],[3]]

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#Iterative version, using QUEUE, BFS
#Your runtime beats 76.49% of python submissions.(One Time AC)
from collections import deque    #Need to import
class Solution(object):
    def levelOrderBottom(self, root):
        if not root: return []
        my_queue,res=deque([root]),[]
        while my_queue:
            res.append(list(my_queue))  #Need to covert queue to list
            new_queue=deque()
            while my_queue:
                temp=my_queue.popleft()
                if temp.left: new_queue.append(temp.left)
                if temp.right: new_queue.append(temp.right)
            my_queue=new_queue
        return [[node.val for node in level] for level in res[::-1]] #Notice deal with res reversily
            
                

#Iterative version, using only List no QUEUE, BFS
#Your runtime beats 90.42% of python submissions.(One Time AC)
class Solution(object):
    def levelOrderBottom(self, root):
        if not root: return []
        my_list,res=[root],[]
        while my_list:
            res.append(my_list)
            new_list=[]
            for node in my_list:
                if node.left: new_list.append(node.left)
                if node.right: new_list.append(node.right)
            my_list=new_list
        return [[node.val for node in level] for level in res[::-1]]
        
            
                
#Iterative version, using python list comprehension.
#Your runtime beats 87.34% of python submissions. (One Time AC)
class Solution(object):
    def levelOrderBottom(self, root):
        res,level=[],[root]
        while root and level:
            res.append([node.val for node in level])
            level=[kid for node in level for kid in (node.left,node.right) if kid]
        return res[::-1]
        
        
            
#Recursive version, using hashing table, python dictionary.
#Your runtime beats 64.56% of python submissions. (One Time AC)
class Solution(object):
    def _level(self,root,level,dict_levels):
        if not root: return
        dict_levels[level]=dict_levels.get(level,[])+[root.val]
        self._level(root.left,level+1,dict_levels)
        self._level(root.right,level+1,dict_levels)
    def levelOrderBottom(self, root):
        d={}
        self._level(root,0,d)
        return d.values()[::-1]
        
        
        
#Recursive version, using list only
#Your runtime beats 34.18% of python submissions.
class Solution(object):
    def _level(self,root,level,res):
        if root:
            if len(res)<level+1:
                res.insert(0,[])
            res[-(level+1)].append(root.val)
            self._level(root.left,level+1,res)
            self._level(root.right,level+1,res)
        
    def levelOrderBottom(self, root):
        res=[]
        self._level(root,0,res)
        return res
        
        
        
#Iterative version, using stack, DFS, preorder traversal
#Your runtime beats 34.18% of python submissions.
class Solution(object):
    def levelOrderBottom(self, root):
        stack,res=[(root,0)],[]
        while stack:
            node,level=stack.pop()
            if node:  #Need to check
                if len(res)<level+1:
                    res.insert(0,[])
                res[-(level+1)].append(node.val)
                stack.append((node.right,level+1))
                stack.append((node.left,level+1))
        return res
        
        
        
#Iterative version, using queue, BFS, levelorder traversal
#Your runtime beats 90.42% of python submissions.
from collections import deque
class Solution(object):
    def levelOrderBottom(self, root):
        queue,res=deque([(root,0)]),[]
        while queue:
            node,level=queue.popleft()
            if node:
                if len(res)<level+1:
                    res.insert(0,[])
                res[-(level+1)].append(node.val)
                queue.append((node.left,level+1))
                queue.append((node.right,level+1))
        return res
        
#Iterative version, using list only, No Reversion.
#Your runtime beats 64.56% of python submissions.
class Solution(object):
    def levelOrderBottom(self, root):
        level,res=[root],[]
        while root and level:
            res.insert(0,[node.val for node in level])
            level=[kid for node in level for kid in (node.left,node.right) if kid]
        return res
        
        
#############################################
#Iterative version, using queue, No Reversion.
#Your runtime beats 76.49% of python submissions.
from collections import deque
class Solution(object):
    def levelOrderBottom(self, root):
        if not root: return []
        res,my_queue=deque(),deque([root])
        while my_queue:
            new_list=[]
            for i in range(len(my_queue)):  #This line is different from "while my_queue:", because len(my_queue) is one time static number
                temp=my_queue.popleft()
                new_list.append(temp.val)#put the values of nodes in this level of my_queue into new list
                if temp.left: my_queue.append(temp.left)
                if temp.right: my_queue.append(temp.right)
            res.appendleft(new_list)   #The use of appendleft
        return list(res)
        
        
###############################################
#Recursive version, using list, No Reversion.
#Your runtime beats 96.56% of python submissions.
class Solution(object):
    def levelOrderBottom(self, root):
        if not root: return []
        result=[]
        def _level(result,prev):
            if not prev: return  #Need to check prev
            temp,next_level=[],[]
            for node in prev:
                temp.append(node.val)
                if node.left: next_level.append(node.left)
                if node.right: next_level.append(node.right)
            _level(result,next_level)  #Recursion before append the current level to result, so that we can append bottomup
            result.append(temp)
        _level(result,[root])
        return result
                
            
        
        
            
                
                
                
                
                
                
        
                    
                
                
                
                
                
                
        
               
            
                
                
                
                
                
                
        
                
            
                
                
                
                
                
                
        
                   
                
                
                
                
                
                
        
                    
                
                
                
                
                
                
        
                   
                
                
                
                
                
                
        
                        
                
                
                
                
                
        
                        
                
                
                
                
        
                        
                
                
                
                
        
        
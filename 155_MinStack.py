class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack_list=[]
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        cur_min=self.getMin()
        if cur_min==None or x<cur_min:
            cur_min=x
        self.stack_list.append((x,cur_min))
        
        

    def pop(self):
        """
        :rtype: void
        """
        if self.stack_list:
            self.stack_list.pop()
        

    def top(self):
        """
        :rtype: int
        """
        if self.stack_list:
            return self.stack_list[-1][0]
        else:
            return None
        

    def getMin(self):
        """
        :rtype: int
        """
        if self.stack_list:
            return self.stack_list[-1][1]
        else:
            return None
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
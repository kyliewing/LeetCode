#My solution, One Time AC.
class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.my_queue=[]

    def push(self, x):
        """I
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.my_queue.append(x)
        

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        queue_length=len(self.my_queue)
        temp_stack=[]
        for i in range(queue_length-1):
            temp_stack.append(self.my_queue.pop())
        top_element=self.my_queue.pop()
        for i in range(queue_length-1):
            self.my_queue.append(temp_stack.pop())
        return top_element
        

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        queue_length=len(self.my_queue)
        temp_stack=[]
        for i in range(queue_length-1):
            temp_stack.append(self.my_queue.pop())
        top_element=self.my_queue[-1]
        for i in range(queue_length-1):
            self.my_queue.append(temp_stack.pop())
        return top_element
        

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return len(self.my_queue)==0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()




#Using two stacks version.
class MyQueue(object):

    def __init__(self):
        #Initialize your data structure here.
        #using to stacks to accomplish queue
        self.queue_stack=[]#this is the queue stack
        self.help_stack=[]#this is the hlper stack
    
    def push(self, x):
        #Push element x to the back of queue.
        #:type x: int
        #:rtype: void
        if self.queue_stack:
            self.queue_stack.append(x)
        else:
            while self.help_stack:
                self.queue_stack.append(self.help_stack.pop())
            self.queue_stack.append(x)

    def pop(self):

        #Removes the element from in front of queue and returns that element.
        #:rtype: int
 
        top_element=self.peek()
        self.help_stack.pop()
        return top_element


    def peek(self):
    
        #Get the front element.
        #:rtype: int
    
        if not self.help_stack:
            while self.queue_stack:
                self.help_stack.append(self.queue_stack.pop())
        return self.help_stack[-1]
        

    def empty(self):

        #Returns whether the queue is empty.
        #:rtype: bool
  
        return (not self.queue_stack) and (not self.help_stack)
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()


# 用栈模拟队列的操作

class MyQueue(object):
    def __init__(self):
        """
        in 负责 push
        out 负责 pop
        """
        self.stack_in = []
        self.stack_out = []


    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack_in.append(x)


    def pop(self):
        """
        :rtype: int
        """
        if self.empty():
            return None
        
        if self.stack_out:
            return self.stack_out.pop()
        else:
            for i in range(len(self.stack_in)):
                self.stack_out.append(self.stack_in.pop())
            return self.stack_out.pop()

    def peek(self):
        """
        Get the front element
        :rtype: int
        """
        ans = self.pop()
        self.stack_out.append(ans)
        return ans
        

    def empty(self):
        """
        :rtype: bool
        只要in或者out有元素,说明队列不为空
        """
        return not (self.stack_in or self.stack_out)


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
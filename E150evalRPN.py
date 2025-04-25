class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        def div(x,y):
            return int(x/y) if x*y > 0 else -(abs(x)//abs(y))
        
        stack = []
        for item in tokens:
            if item.isdigit() or (item.startswith("-") and item[1:].isdigit()):
                stack.append(item)
            elif item == "+":
                b = int(stack.pop())
                a = int(stack.pop())
                stack.append(a + b)
            elif item == "-":
                b = int(stack.pop())
                a = int(stack.pop())
                stack.append(a - b)              
            elif item == "*":
                b = int(stack.pop())
                a = int(stack.pop())
                stack.append(a * b)
            elif item == "/":
                b = int(stack.pop())
                a = int(stack.pop())
                stack.append(div(a,b))

        return int(stack[-1]) if stack else 0
        
EXM = Solution()
tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]

print(EXM.evalRPN(tokens))
value = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]

from typing import List

class Stack:
    def __init__(self, length):
        self.stack = [0] * length
        self._i = 0
        
    def push(self, value):
        self.stack[self._i] = value
        self._i += 1

    def pop(self):
        value = self.stack[self._i-1]
        self._i -= 1
        return value

    def eval(self, char):
        n1 = self.pop()
        n2 = self.pop()
        if char == "+":
            print(n1,n2)
            self.push(n2 + n1)
        elif char == "-":
            self.push(n2 - n1)
        elif char == "*":
            self.push(n2 * n1)
        else:
            self.push(int(n2/n1))

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = Stack(len(tokens))
        for token in tokens:
            if token in "+-*/":
                stack.eval(token)
            else:
                stack.push(int(token))
            print(stack.stack)
            
        return stack.pop()

if __name__ == "__main__":
    print(Solution().evalRPN(value))
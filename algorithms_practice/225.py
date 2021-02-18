"""Implement Stack with Queue
"""
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s1 = []
        

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.s1.append(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.s1.pop()

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.s1[-1]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return not self.s1

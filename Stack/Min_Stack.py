class MinStack(object):

    def __init__(self):
        self.main_stack = []
        self.min_stack = []

    def push(self, val):
        self.main_stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self):
        if self.main_stack[-1] == self.min_stack[-1]:
            self.min_stack.pop()
        self.main_stack.pop()

    def top(self):
        return self.main_stack[-1]

    def getMin(self):
        return self.min_stack[-1]
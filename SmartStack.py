"""
How would you design a stack which, in addition to push and pop, also has a function min which
returns the minimum element?  Push, pop and min should all operate in O(1) time.
T. Melano
"""

class SmartStack:
    def __init__(self):
        self.stack= []
        self.min = []

    def push(self,x):
        self.stack.append(x)
        if len(self.min) != 0:
            if x <= self.stack_min():
                self.min.append(x)
        else:
            self.min.append(x)

    def pop(self):
        if len(self.stack) != 0:
            x = self.stack.pop()
            if x == self.stack_min():
                self.min.pop()
            return x
        else:
            print "Stack is empty, no longer pop-able"

    def stack_min(self):
        if len(self.min) != 0:
            return self.min[-1]

def test1():
    print "Push elements to the stack"
    list = range(10)
    stack = SmartStack()
    for i in list:
        stack.push(i)
    print "Print stack and stack minimum"
    print stack.stack
    print stack.stack_min()
    print "Push -1 to stack, print stack and stack minimum"
    stack.push(-1)
    print stack.stack
    print stack.stack_min()
    print "Pop from stack, print stack and stack minimum"
    print stack.pop()
    print stack.stack
    print stack.stack_min()

def test2():
    stack = SmartStack()
    stack.push(1)
    stack.push(1)
    print "Print stack and stack minimum"
    print stack.stack
    print stack.stack_min()
    print "Pop from stack, print stack and stack minimum"
    print stack.pop()
    print stack.stack
    print stack.stack_min()

def test3():
    stack = SmartStack()
    stack.push(-1)
    stack.push(1)
    stack.push(1)
    print "Print stack and stack minimum"
    print stack.stack
    print stack.stack_min()
    print "Pop from stack, print stack and stack minimum"
    print stack.pop()
    print stack.stack
    print stack.stack_min()
    print "Pop from stack, print stack and stack minimum"
    print stack.pop()
    print stack.stack
    print stack.stack_min()
    print "Pop from stack, print stack and stack minimum"
    print stack.pop()
    print stack.stack
    print stack.stack_min()
    print "Pop from stack, print stack and stack minimum"
    print stack.pop()
    print stack.stack
    print stack.stack_min()

def main():
    print "Running test1"
    test1()
    print "Running test2"
    test2()
    print "Running test3"
    test3()

if __name__ == "__main__":
    main()

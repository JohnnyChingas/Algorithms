print "Implement a stack using a list, append and pop"
star = '*'
print star*10
stack = [3,4,5]
print "stack = ",stack
print "append 6 and 7"
stack.append(6)
stack.append(7)
print "stack = ",stack
print "pop from stack"
print "stack.pop() = ",stack.pop()
print "stack.pop() = ",stack.pop()
print "stack.pop() = ",stack.pop()
print "stack = ",stack
print star*10
print "Implement a queue using a list, append and pop"
print "from collections import deque"
from collections import deque
queue = deque(["Eric","John","Michael"])
print "queue = deque([""Eric"",""John"",""Michael""])"
queue.append("Terry")
queue.append("Graham")
print "append Terry and Graham"
print "queue =",queue
print "queue.popleft() =",queue.popleft()
print "queue.popleft() =",queue.popleft()
print "queue.popleft() =",queue.popleft()
print "queue =",queue

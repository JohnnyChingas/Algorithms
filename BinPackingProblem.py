from random import random

class Node:
    def __init__(self,space = 1.):
        self.space = space
        self.left, self.right = None, None
        

def main():
    root = Node

    binCount = 0
    n = 100
    w = []
    for i in xrange(n):
        w.append(random())

    for i in xrange(n):
        weight = w[i]
        node = root
        minDiff = 1
        minNode = Node
        while node!=null:
            if node.space > weight: #There is enough space for weight
                if minDiff > diff:
                    minDiff = diff
                    minNode = node
                    node = node.left
            else:
                node = node.right
        if minNode == None:
            binCount += 1
            node = Node
            node.space = node.space - weight
            




if __name__ == "__main__":
    main()
    

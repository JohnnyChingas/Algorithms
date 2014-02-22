# Some linked list operations
# T. Melano

class Node:
    
    def __init__(self, data = None):
        # Node initiator
        # @param data is any object contained in the node
        self.data = data
        self.next = None

    def insert(self, data):
        # Add nodes to linked list
        # @param data for new node added to linked list
        if self.next == None:
            self.next = Node(data)
        else:
            self.next.insert(data)

    def traverse(self):
        # Traverse and print linked list
        print self.data
        if self.next != None:
            self.next.traverse()

    def reverse(self):
        # Reverse linked list
        last = None
        head = self
        while head != None:
            next = head.next
            head.next = last
            last = head
            head = next
        return last
    
    #Write function that reverses a linked list using recursion


def main():
    list = [1,2,3,4,5]
    head = Node(0)
    for elem in list:
        head.insert(elem)
    print "Print list"
    head.traverse()
    
    print "Reversing list"
    head = head.reverse()
    head.traverse()

    print "Reversing list"
    head = head.reverse()
    head.traverse()

if __name__ == "__main__":
    main()

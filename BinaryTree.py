# Binary Search Tree
# T. Melano

class Node:
    """
    Tree node: left, right and data
    """
    
    def __init__(self, data):
        #Node initiator
        #@param data node data object
        self.left = None
        self.right = None
        self.data = data


    def insert(self, data):
        """
        Insert new node with data
        @param insert node with data object
        """
        if data < self.data:
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.insert(data)
        else:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.insert(data)
        
    def search(self, data):
        """
        Search tree for data
        @param data object
        """
        if data < self.data:
            if self.left is None:
                return None
            return self.left.search(data)
        elif data > self.data:
            if self.right is None:
                return None
            return self.right.search(data)
        else:
            return self.data

def main():
    root = Node(8)
    data_list = [3,10,1,6,4,7,14,13]
    for d in data_list:
        root.insert(d)
    print root.search(14)
    print root.search(1)
    print root.search(7)
    print root.search(9)
    print root.search(None)


if __name__ == '__main__':
    main()

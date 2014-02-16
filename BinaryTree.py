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
        
    def search(self, data, parent = None):
        """
        Search tree for data
        @param data object
        returns object containing data
        """
        if data < self.data:
            if self.left is None:
                return None, None
            return self.left.search(data, self)
        elif data > self.data:
            if self.right is None:
                return None
            return self.right.search(data, self)
        else:
            return self, parent

    def min(self):
        if self.left is not None:
            return self.left.min() 
        else:
            return self
                
    def max(self):
        if self.right is not None:
            return self.right.max()
        else:
            return self

    def traverse(self):
        if self.left is not None:
            self.left.traverse()
        print self.data
        if self.right is not None:
            self.right.traverse()

    def parent(self,data):
        # write this
        return true
    
    def delete(self, data):
        headNode,parent = self.search(data)
        if headNode.left and headNode.right:
            succesor = headNode.right.min()
            succesor,parent = self.search(succesor.data)
            headNode.data = succesor.data
            if parent.left != None:
                if parent.left.data == succesor.data:
                    parent.left = None
            elif parent.right != None:
                if parent.right.data == succesor.data:
                    parent.right = None
            del succesor
        else:
            headNode.data = headNode.left.data or headNode.right.data
            headNode.left, headNode.right = None, None

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
    print root.min()
    print root.max()

    root.traverse()
    delete_node = 14
    print "deleting node ",delete_node
    root.delete(delete_node)
    root.traverse()


if __name__ == '__main__':
    main()

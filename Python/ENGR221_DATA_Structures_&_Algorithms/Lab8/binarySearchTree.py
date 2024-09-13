

class BinarySearchTree:
    """ DESCRIBE THE BST CLASS HERE """

    def __init__(self):
        self.__root = None # The root Node of this BST

    def insert(self, insertKey, insertValue):
        """ Inserts the given key and value into the BST.
            Inputs:
                - insertKey: (any) The key to insert
                - insertValue: (any) The value to insert
            Returns: None
        """
        # Update the root to include the inserted node
        self.__root = self.__insertHelp(self.__root, insertKey, insertValue)
    
    def __insertHelp(self, node, insertKey, insertValue):
        """ A recursive helper method to insert a new node 
            with the given key and value into the BST.
            Inputs:
                - node: (Node) The root of the subtree to insert into
                - insertKey: (any) The key to insert
                - insertvalue: (any) The value to insert
            Returns: The node to insert """
        # Base case - Insert the node as a leaf in the appropriate location
        if insertKey == None or insertValue == None:
            return node
        if node == None:
            return self.__Node(insertKey, insertValue)
        # Insert the key into the left subtree if it is less than the current key
        elif insertKey < node.key:
            node.left = self.__insertHelp(node.left, insertKey, insertValue)
        # Insert the key into the right subtree if it is greater than the current key
        elif insertKey > node.key:
            node.right = self.__insertHelp(node.right, insertKey, insertValue)
        # Return the node with the node inserted
        return node

    def isEmpty(self):
        """ Checks to see if the tree has a root using a conditional statement,
        Inputs: None

        Returns: a boolean True if empty, False if not. """

        # if the root is None, returns True
        if self.__root == None:
            return True
        else:
            return False
    
    def getRoot(self):
        """ Uses the self.root to grab the root of the tree
        Inputs: None
        
        Returns: The key of the root Node"""

        # simply put, call the root attribute
        return self.__root

    def search(self, goalKey):
        """ Searches through the BST for the given key, goalKey
        Inputs: 
                - goalKey: (any) The key that is being searched
        
        Returns: Node of the goalKey"""

        #call the searchHelp method, using the root as a base
        return self.__searchHelp(self.__root, goalKey)
        

    def __searchHelp(self, node, goalKey):
        """ A recursive helper method to search for a given key
            within the BST
            Inputs: 
                - node: (Node) The root node of the subtree being searched
                - goalKey: (any/int) The key to search for 
            Returns: The Node with the given key, goalKey"""
        # Base case - if the node being searched is None, return a None type
        if node == None:
            return None
        # Search the left subtree if the goalKey is less than the current key
        elif goalKey < node.key:
            return self.__searchHelp(node.left, goalKey)
        # Search the right subtree if the goalKey is greater than the current key
        elif goalKey > node.key:
            return self.__searchHelp(node.right, goalKey)
        # return the Node of the given key, goalKey
        return node
        

    def lookup(self, goal):
        """ Get the value of given key, using the searchHelp method
            Inputs: 
                - goal: (any) the Key whose value to return
            Returns: the Value of the goal key"""
        # Uses the searchHelp method, but this time signify that we want to return
        # the value Attribute of the Node
        return self.__searchHelp(self.__root, goal).value

    def findSuccessor(self, subtreeRoot):

        """ Finds the successor of a given subtree
            Input: 
                - subtreeRoot: (any) the key of the root
            Returns: the successor
        """
        
        #call the findSuccessorHelp method
        return self.__findSuccessorHelp(subtreeRoot)
    
    def __findSuccessorHelp(self, node):
        """ A recursive helper method to find the smallest key in the tree
            Inputs: 
                - node: (Node) The root node of the subtree to find the successor for
            
            Returns: The node with the smallest key, or the successor """
        
        # create successor variable to hold the Node of the roots successor
        successor = None
        # Base case: if the node has no left child, set the successor to be node 
        if node.left == None:
            successor = node
        # otherwise call the helper method again until base case is reached
        elif node.left != None:
            return self.__findSuccessorHelp(node.left)
        #return the successor
        return successor

    
    def delete(self, deleteKey):
        """ Deletes a key from the BST
            Inputs: 
                - deleteKey: (any) the key being deleted
            
             Returns:  none, but will update root once the key is deleted
            
        """
        # search the BST for the deleteKey, if found call the helper function and
        # assign the root to its return
        if self.search(deleteKey):
            self.__root = self.__deleteHelp(self.__root, deleteKey)
        # if not found raise an exception
        else:
            raise Exception("Key not in tree.")
    
    def __deleteHelp(self, node, deleteKey):
        """ A recursive helper method to delete a node with the given
            key from the BST
            Inputs: 
                - node: (Node) the root node of the subtree to delete from
                - deleteKey: (any) the key to delete
            Returns: the updated node with the specified node deleted """
        
        # Delete from the left subtree if deleteKey is less than node.key
        if node.key > deleteKey:
            node.left = self.__deleteHelp(node.left, deleteKey)
            return node
        # Alternatively delete from right subtree if deleteKey is greater than node.key
        elif node.key < deleteKey:
            node.right = self.__deleteHelp(node.right, deleteKey)
            return node
        
        # if the node has no left child, return the right child
        if node.left is None:
            return node.right
        
        # if the node has no right child, return the left child
        elif node.right is None:
            return node.left
        
        # if the node has two children, start with finding successor
        else:
            successor = self.__findSuccessorHelp(node.right)
            # replace the node key and value with its successors' key and value
            node.key = successor.key
            node.value = successor.value
        
        # Delete the successor node from its original position
            node.right = self.__deleteHelp(node.right, successor.key)
           
            # Update parent's reference to the successor node 
            return node
        

    def traverse(self) -> None:
        """ Traverse the BST to print out each node from left to right
            using the helper method to traverse """
        self.__traverseHelp(self.__root)

    def __traverseHelp(self, node) -> None:
        """ A recursive helper method which visits each node in the tree,
            in ascending order. We would want to use a depth-first method 
            to best complete this task
            
            Inputs:
                - node: (Node) the root node of the subtree we want to traverse
                
            Returns: none
        """
        # if the node is populated, recursively call the left children to its leaf nodes
        # then print the root, then recursively call the right children to its leaf nodes 
        if node != None:
            self.__traverseHelp(node.left)
            print(node)
            self.__traverseHelp(node.right)

    def __str__(self) -> str:
        """ Represent the tree as a string. Formats as 
            {(rootkey, rootval), {leftsubtree}, {rightsubtree}} """
        return self.__strHelp("", self.__root)
    
    def __strHelp(self, return_string, node) -> str:
        """ A recursive helper method to format the tree as a string. 
            Input: 
                - return_string: (string) Accumulates the final string to output
                - node: (Node) The current node to format
            Returns: A formatted string for this node. """
        # Base case - Represent an empty branch as "None"
        if node == None:
            return "None"
        # Recursively build the string to return
        # Note, this is equivalent to
        #   return "{" + node + ", " + \
        #                self.strHelp(return_string, node.left) + ", " + \
        #                self.strHelp(return_string, node.right) + "}"
        return "{{{}, {}, {}}}".format(node, 
                                       self.__strHelp(return_string, node.left), 
                                       self.__strHelp(return_string, node.right))
            

    ##############
    # NODE CLASS #
    ##############

    class __Node:
        """ Implementation of a node in a BST. Note that it is 
            private, so it cannot be accessed outside of a BST """

        def __init__(self, key, value, left=None, right=None):
            self.key = key         # The key of the root node of this tree
            self.value = value     # The value held by the root node of this tree
            self.left = left       # Points to the root of the left subtree
            self.right = right     # Points to the root of the right subtree

        def __str__(self):
            """ Represent the node as a string.
                Formats as "{key, value}" """
            return "({}, {})".format(self.key, self.value)
        
if __name__ == "__main__":
    bst = BinarySearchTree()

    bst.insert(7, "seven")
    bst.insert(5, "five")
    bst.insert(8, "eight")
    bst.insert(3, "three")
    bst.insert(1, "one")
    bst.insert(10, "ten")
    bst.insert(20, "twenty")
    bst.insert(6, "six")
    bst.insert(2, "two")
    bst.insert(4, "four")
    bst.insert(9, "nine")
    print(bst.__str__())
    print(bst.traverse())
    pass

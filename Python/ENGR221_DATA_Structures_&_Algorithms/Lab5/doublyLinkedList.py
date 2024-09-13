###############################################
#   Title:          doublyLinkedList.py
#   Name:           Ryan L. (zano)
#   Description:    Implementation of a doubly linked list
###############################################

from .doubleNode import DoubleNode 

class DoublyLinkedList():

    def __init__(self): #constructor
        self.__firstNode = None
        self.__lastNode = None 

    def isEmpty(self): #checks if list is empty
        return (self.__firstNode == None and self.__lastNode == None)

    def first(self): #returns the first value in the list
        if self.isEmpty():
            raise Exception("Error: Cannot get first value from empty list")
        return self.__firstNode.getValue()
    
    def getFirstNode(self): #returns the first node in the list
        return self.__firstNode

    def getLastNode(self): #returns the last node in the list
        return self.__lastNode
    
    def setFirstNode(self, node): #sets the first node in the list
        self.__firstNode = node

    def setLastNode(self, node): #sets the last node in the list
        self.__lastNode = node

    def find(self, value): #finds a value in the list
        node = self.getFirstNode()
        while node != None:
            # If this node has the given value, return it
            if node.getValue() == value:
                return node 
            # Otherwise, grab the next node to check
            node = node.getNextNode()
        # If the value was not found, return None
        return None

    def insertFront(self, value): #inserts a value at the front of the list
        node = DoubleNode(value, self.__firstNode, None)

        if self.isEmpty():
            self.setLastNode(node)

        if self.__firstNode != None:
           self.__firstNode.setPreviousNode(node) 
        
        self.setFirstNode(node)
        


    def insertBack(self, value): #inserts a value at the back of the list
        node = DoubleNode(value, None, self.__lastNode)
        if self.isEmpty():
            self.setFirstNode(node)

        if self.__lastNode != None:
           self.__lastNode.setNextNode(node) 
        
        self.setLastNode(node)

    def insertAfter(self, value_to_add, after_value) -> None: #inserts a value after a given value
        if self.isEmpty():
            raise Exception("Error: cannot insertAfter in empty list")
        newNode = DoubleNode(value_to_add)
        node = self.getFirstNode()
        while node.getValue() != after_value:
            node = node.getNextNode()

        if node.isLast():
            newNode.setPreviousNode(node)
            node.setNextNode(newNode)
            self.setLastNode(newNode)

        newNode.setPreviousNode(node)
        newNode.setNextNode(node.getNextNode())
        node.getNextNode().setPreviousNode(newNode)
        node.setNextNode(newNode)
    
    def deleteFirstNode(self): #deletes the first node in the list and returns its value
        if self.isEmpty():
            raise Exception("nuh uh") #breaks if empty
        
        r_val = self.getFirstNode().getValue()

        if not(self.getFirstNode().isLast()):
            self.setFirstNode(self.getFirstNode().getNextNode())
            self.getFirstNode().setPreviousNode(None)
            
        else:
            self.setFirstNode(None)

        return r_val

    def deleteLastNode(self):   #deletes the last node in the list and returns its value
        if self.isEmpty():
            raise Exception("Error: Cannot delete node from empty list") #breaks if empty
        
        del_node = self.getLastNode()

        if del_node.isFirst():
            self.setLastNode(None)
            

        else:
            self.setLastNode(self.getLastNode().getPreviousNode())
            self.getLastNode().setNextNode(None)
        return del_node.getValue()
        
    
    def deleteValue(self, value): #deletes a value from the list and returns it
        if self.isEmpty():
            raise Exception("Error: Cannot delete from empty list")
        
        del_node = self.getFirstNode()

        while del_node.getValue() != value:
            del_node = del_node.getNextNode()
        
        del_node.getPreviousNode().setNextNode(del_node.getNextNode())
        del_node.getNextNode().setPreviousNode(del_node.getPreviousNode())

        return del_node.getValue()
        
        

    def forwardTraverse(self): #prints the list from the first node to the last node
        if self.isEmpty():
            raise Exception("Error: cannot print empty list")
        
        r_list = []
        node = self.getFirstNode()

        while not (node.isLast()):
            r_list.append(node.getValue())
            node = node.getNextNode()
        r_list.append(self.getLastNode().getValue())

        for i in r_list:
            print(i)


    def reverseTraverse(self): #prints the list from the last node to the first node
        if self.isEmpty():
            raise Exception("Error: Cannot print empty list in reverse order")
        
        r_list = []
        node = self.getLastNode()

        while not(node.isFirst()):
            r_list.append(node.getValue())
            node = node.getPreviousNode()
        r_list.append(self.getFirstNode().getValue())

        for i in r_list:
            print(i)

    def __len__(self): #length attribute of the list
        l = 0
        # Traverse down the list starting with the first node
        node = self.getFirstNode() 
        # Stop when we reach the end of the list
        while node != None:
            # Increment the counter for each node we find
            l += 1
            # Update node to be the next node
            node = node.getNextNode()
        # Return the counter
        return l
    
    def __str__(self): #toString 
        if self.isEmpty():
            raise Exception("Error: Cannot delete from empty list")
        
        r_list = []
        node = self.getFirstNode()

        while node.getNextNode() != None:
            r_list.append(node.getValue())
            node = node.getNextNode()

        return "["+ "".join(str(i) + " <-> " for i in r_list)+ str(self.getLastNode().getValue()) + "]"
    
if __name__ == "__main__":
    pass
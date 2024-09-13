###############################################
#   Title:          Lab5/doubleNode.py
#   Name:           Ryan L. (zano)
#   Description:    Implementation of a double node for a doubly linked list
###############################################

class DoubleNode():

    def __init__(self, value, next=None, previous=None): #constructor
        self.__value = value
        self.__nextNode = next
        self.__previousNode = previous 

    #####
    # Methods
    #####
        
    def isFirst(self) -> bool:
        return self.__previousNode == None
        
    def isLast(self) -> bool:
        return self.__nextNode == None

    #####
    # Getters
    #####

    def getValue(self):
        return self.__value
    
    def getNextNode(self):
        return self.__nextNode

    def getPreviousNode(self):
        return self.__previousNode

    #####
    # Setters
    #####

    def setValue(self, new_value) -> None:
        self.__value = new_value

    def setNextNode(self, new_next) -> None:
        self.__nextNode = new_next

    def setPreviousNode(self, new_previous) -> None:
        self.__previousNode = new_previous

    #####
    # Helpers
    #####

    def __checkValidNode(self, node) -> bool:
        if type(node) != DoubleNode and node != None:
            raise Exception("Error: Input must be a valid DoubleNode or None")
        return True
    
    def __str__(self):
        return str(self.__value)

if __name__ == "__main__":
    pass
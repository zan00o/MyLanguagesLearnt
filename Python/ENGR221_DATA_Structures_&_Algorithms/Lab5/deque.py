###############################################
#   Title:          Lab5/deque.py
#   Name:           Ryan L. (zano)
#   Description:    Implementation of a deque using a doubly linked list
###############################################

from .doublyLinkedList import DoublyLinkedList

class Deque():

    def __init__(self): #constructor
        self.__values = DoublyLinkedList()

    ####
    # Helper Methods
    ####

    def isEmpty(self): #returns if list is empty
        return self.__values.isEmpty()
    
    def __len__(self): #length attribute
        return len(self.__values)
    
    def __str__(self): #string representation
        return str(self.__values)
    
    ####
    # Deque Methods
    ####
    
    def peekLeft(self): #returns the first value in the list without removing it
        return self.__values.first()

    def peekRight(self): #returns the last value in the list without removing it
        return self.__values.getLastNode().getValue()

    def insertLeft(self, value): #inserts a value at the front of the list
        self.__values.insertFront(value)
        
    def insertRight(self, value): #inserts a value at the back of the list
        self.__values.insertBack(value)

    def removeLeft(self): #removes the first value in the list and returns it
        return self.__values.deleteFirstNode()

    def removeRight(self): # removes the last value in the list and returns it
        return self.__values.deleteLastNode()
    
if __name__ == "__main__":
    pass
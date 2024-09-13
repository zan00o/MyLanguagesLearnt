"""
Author: Zan00o
Filename: set.py
Description: 

Sets are another type of data structure with the following properties:
    a) All items in the set are unique (i.e., no duplicates)
    b) Sets are unordered (similar to arrays)
    c) Sets are unindexed (unlike arrays)

"""


class MySet():

    def __init__(self, values):
        
        self.__s = values #the set
        self.__size = len(values) #__size of the set

        #remove duplicates
        """
        for i in self.__s:
            #if the value appears more than once
            if self.__s.count(i) > 1:
                #remove the first instance of the value
                self.__s.remove(i)
        """
        for i in self.__s:
            while i in self.__s and self.__s.count(i) > 1:
                self.__s.remove(i)
                self.__size -= 1

    def size (self) -> int: #return the size of the set
        return self.__size
    
    def vals(self) -> list: #return the set as a list
        return self.__s

    def search(self, v) -> bool: #search for a value in the set

        if v in self.__s: #if the value is in the set
            return True #return True
            
        return False        #if the value is not in the set, return False
        
    def insert(self, v) -> None: #insert a value into the set
        if v not in self.__s: #if the value is not in the set
            self.__size += 1
            self.__s.append(v)  #add the value to the set

    def delete(self, v) -> bool:    #delete a value from the set

        if (self.search(v) == False): #if the value is not in the set
            return False            #return False
        
        #if the value is in the set
        self.__size -= 1   #decrement the __size of the set
        self.__s.remove(v) #remove the value 
        
        
    
    def traverse(self):
        
        for i in self.__s: 
            print(f"{i}") #print each value in the set
        
    
    """
    def traverse(self) -> list: #return the set as a list
        return self.__s

    """

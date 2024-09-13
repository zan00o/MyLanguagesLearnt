"""
###############################################
#   Title:          MyHashMap.py
#   Name:           Ryan L. (zano)
#   Description:     Implement a hashmap
###############################################
Adapted from UCSD CSE12
"""

class MyHashMap:
    def __init__(self, load_factor=0.75,
                       initial_capacity=16):
        self.load_factor = load_factor 
        self.capacity = initial_capacity 
        self.size = 0
        self.buckets = [[] for _ in range(self.capacity)]

    """
    Resizes the self.buckets array when the load_factor is reached. """
    def resize(self):
        # Double the number of buckets
        self.capacity *= 2 
        # Create a new set of buckets that's twice as big as the old one
        old_buckets = self.buckets
        self.buckets = [[] for _ in range(self.capacity)]
        # Add each key, value pair already in the MyHashMap to the new buckets
        for bucket in old_buckets:
            if bucket != []:
                for entry in bucket:
                    self.put(entry.getKey(), entry.getValue())
        # Update the self.buckets attribute with the new entries
        """
        # Double the number of buckets
        self.capacity *= 2 
        # Create a new set of buckets that's twice as big as the old one
        new_buckets = [[] for _ in range(self.capacity)]
        # Add each key, value pair already in the MyHashMap to the new buckets
        for bucket in self.buckets:
            if bucket != []:
                for entry in bucket:
                    self.put(entry.getKey(), entry.getValue())
        # Update the self.buckets attribute with the new entries
        self.buckets = new_buckets
        """

    """
    Adds the specified key, value pair to the MyHashMap if 
    the key is not already in the MyHashMap. If adding a new key would
    surpass the load_factor, resize the MyHashMap before adding the key.
    Return true if successfully added to the MyHashMap.
    Raise an exception if the key is None. """
    def put(self, key, value):
        keyHash = hash(key)
        # TODO: write your put implementation here
        if key == None:
            raise Exception ("Error: Key cannot be None")

        index = keyHash % self.capacity
        print(self.capacity, index)

        newEntry = self.MyHashMapEntry(key, value)

        
        if index >= 0 and index < self.capacity:
            if self.size > self.load_factor * self.capacity:
                self.resize()
            
            self.size += 1
            self.buckets[index].append(newEntry)
            return True
        
        return False


        """
        index = keyHash % self.capacity

        bucket = self.buckets[index]

        for entry in bucket:
            if entry.getKey() == key:
                entry.setValue(value)
                return True
        
        bucket.append(self.MyHashMapEntry(key, value))
        """

    """
    Replaces the value that maps to the given key if it is present.
    Input: key is the key whose mapped value is being replaced.
           newValue is the value to replace the existing value with.
    Return true if the key was in this MyHashMap and replaced successfully.
    Raise an exception if the key is None. """
    def replace(self, key, newValue):
        # TODO: write your replace implementation here
        if key == None:
            raise Exception ("Error: Key cannot be None")
        
        hashKey = hash(key)
        index = hashKey % self.capacity
        
        bucket = self.buckets[index]
        
        for entry in bucket:
            if entry.getKey() == key and entry.getValue() != []:
                entry.setValue(newValue)
                return True
            
        return False

        

    """
    Remove the entry corresponding to the given key.
    Return true if an entry for the given key was removed.
    Raise an exception if the key is None. """
    def remove(self, key):
        # TODO: write your remove implementation here
        if key == None:
            raise Exception ("Error: Key cannot be None")

        hashKey = hash(key)
        index = hashKey % self.capacity

        bucket = self.buckets[index]

        for entry in bucket:
            if entry.getKey() == key:
                bucket.remove(entry)
                self.size -= 1
                return True
        return False

        

    """
    Adds the key, value pair to the MyHashMap if it is not present.
    Otherwise, replace the existing value for that key with the given value.
    Raise an exception if the key is None. """
    def set(self, key, value) -> None:
        # TODO: Write your set implementation here
        if key == None:
            raise Exception ("Error: Key cannot be None")
        
        hashKey = hash(key)
        index = hashKey % self.capacity

        
        if self.containsKey(key) == True:
            self.replace(key, value)
        else:
            self.put(key, value)
        

    """
    Return the value of the specified key. If the key is not in the
    MyHashMap, return None.
    Raise an exception if the key is None. """
    def get(self, key) :
        # TODO: Write your get implementation here 
        if key == None:
            raise Exception ("Error: Key cannot be None")

        hashKey = hash(key)
        index = hashKey % self.capacity

        bucket = self.buckets[index]

        for entry in bucket:
            if entry.getKey() == key:
                return entry.getValue()
        return None
        

        
        
        

    """
    Return the number of key, value pairs in this MyHashMap. """
    def size(self) -> int:
        # TODO: Write your size implementation here 
        return self.size
    

    """
    Return true if the MyHashMap contains no elements, and 
    false otherwise. """
    def isEmpty(self):
        # TODO: Write your isEmpty implementation here
        if self.size == 0:
            return True
        else:
            return False
        

    """
    Return true if the specified key is in this MyHashMap. 
    Raise an exception if the key is None. """
    def containsKey(self, key):
        # TODO: Write your containsKey implementation here 
        if key == None:
            raise Exception ("Error: Key cannot be None")
        
        hashKey = hash(key)
        index = hashKey % self.capacity

        bucket = self.buckets[index]
        
        for entry in bucket:
            if entry.getKey() == key:
                return True
        return False
    


    """
    Return a list containing the keys of this MyHashMap. 
    If it is empty, return an empty list. """
    def keys(self):
        # TODO: Write your keys implementation here
        return [entry.getKey() for bucket in self.buckets for entry in bucket]
    

    class MyHashMapEntry:
        def __init__(self, key, value):
            self.key = key 
            self.value = value 

        def getKey(self):
            return self.key 
        
        def getValue(self):
            return self.value 
        
        def setValue(self, new_value):
            self.value = new_value 

if __name__ == "__main__":
    pass
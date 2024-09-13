import pytest

from myHashMap import MyHashMap

# Write your tests here

@pytest.fixture

#define empty hashmap for testing
def emptyList():
    return MyHashMap()

@pytest.fixture
#define populated hashmap for testing
def nonemptyList():
    newmap = MyHashMap()
    newmap.put(0,1)
    newmap.put(1,2)
    newmap.put(2,5)
    return newmap

@pytest.mark.put
#put functionality for MyHashMap
def test_put_on_empty(emptyList):
    #put 1 in the hashmap
    emptyList.put(1,1)
    #check if the value is 1
    assert emptyList.get(1) == 1

@pytest.mark.put
#put functionality for MyHashMap
def test_put_on_nonempty(nonemptyList):
    #put 3 in the hashmap
    nonemptyList.put(3,3)
    #check if the value is 3
    assert nonemptyList.get(3) == 3

@pytest.mark.replace
#replace functionality for MyHashMap
def test_replace_on_empty(emptyList):
    #replace 1 with 2 in the hashmap
    emptyList.replace(1,3)
    #check if the value is None
    assert emptyList.get(1) == None

@pytest.mark.replace
#replace functionality for MyHashMap
def test_replace_on_nonempty(nonemptyList):
    #replace 1 with 3 in the hashmap
    nonemptyList.replace(1,3)
    #check if the value is 3
    assert nonemptyList.get(1) == 3

@pytest.mark.remove
#remove functionality for MyHashMap
def test_remove_on_empty(emptyList):
    #remove 1 from the hashmap
    emptyList.remove(1)
    #check if the value is None
    assert emptyList.get(1) == None

@pytest.mark.remove
#remove functionality for MyHashMap
def test_remove_on_nonempty(nonemptyList):
    #remove 1 from the hashmap
    nonemptyList.remove(1)
    #check if the value is None
    nonemptyList.keys()
    assert nonemptyList.get(1) == None

@pytest.mark.set 
#set functionality for MyHashMap
def test_set_on_empty(emptyList):
    #set 1 in the hashmap
    emptyList.set(1,1)
    #check if the value is 1
    assert emptyList.get(1) == 1

@pytest.mark.set
#set functionality for MyHashMap
def test_set_on_nonempty(nonemptyList):
    #set 3 in the hashmap
    nonemptyList.set(3,3)
    #check if the value is 3
    assert nonemptyList.get(3) == 3

@pytest.mark.get
#get functionality for MyHashMap
def test_get_on_empty(emptyList):
    #check if the value is None
    assert emptyList.get(1) == None

@pytest.mark.get
#get functionality for MyHashMap
def test_get_on_nonempty(nonemptyList):
    #check if the value is 1
    assert nonemptyList.get(1) == 2

@pytest.mark.size
#size functionality for MyHashMap
def test_size_on_empty(emptyList):
    #should return 0
    assert emptyList.size == 0

@pytest.mark.size
#size functionality for MyHashMap
def test_size_on_nonempty(nonemptyList):
    #should return 3
    assert nonemptyList.size == 3


@pytest.mark.isEmpty
#isEmpty functionality for MyHashMap
def test_isempty_true(emptyList):
    #should return True
    assert emptyList.isEmpty()

@pytest.mark.isEmpty
#isEmpty functionality for MyHashMap
def test_isempty_false(nonemptyList):
    #should return False
    assert not nonemptyList.isEmpty()


@pytest.mark.containsKey
#containsKey functionality for MyHashMap
def test_containsKey_true(nonemptyList):
    #should return True
    assert nonemptyList.containsKey(1)

@pytest.mark.containsKey
#containsKey functionality for MyHashMap
def test_containsKey_false(nonemptyList):
    #should return False
    assert not nonemptyList.containsKey(3)

if __name__ == "__main__":
    breakpoint()
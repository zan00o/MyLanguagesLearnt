import pytest

from box import Box

# Write your tests here
@pytest.fixture
def defaultBox():
    return Box()

@pytest.mark.add
def test_add(defaultBox):
    nickname = "Pikachu"
    species = "Electric"
    assert defaultBox.add(nickname, species) == True

@pytest.mark.find
def test_find(defaultBox):
    nickname = "Pikachu"
    species = "Electric"
    defaultBox.add(nickname, species)
    assert defaultBox.find(nickname, species) != None

@pytest.mark.findAllNicknames
def test_findAllNicknames(defaultBox):
    assert defaultBox.findAllNicknames() != []

@pytest.mark.findEntryByNickname
def test_findEntryByNickname(defaultBox):
    nickname = "Pikachu"
    species = "Electric"
    defaultBox.add(nickname, species)
    assert defaultBox.findEntryByNickname(nickname) != None

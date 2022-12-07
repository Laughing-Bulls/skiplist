import math
import random

# TODO: Add documentation to each method

class SkipListNode:
  def __init__(self):
    self.after   = None
    self.before  = None
    self.above   = None
    self.below   = None
    self.value = None
    self.key     = None

class SkipList:
  def __init__(self):
    self.length = 0
    self.height = 0
    self.topLeftElement = None

    self.__insertTopLevel()
    self.__insertTopLevel()

  # insert/replace value
  def insertElement(self, key, value):
    foundElement = pointer = self.findElement(key, getValue=False)

    if foundElement.key == key:
      foundElement.value = value
      return foundElement.value

    element = self.__insertAfterAbove(pointer, None, key, value)
    count = 1
    while random.random() > 0.5:
      count = count + 1
      while pointer.above == None:
        pointer = pointer.before

      pointer = pointer.above
      element = self.__insertAfterAbove(pointer, element, key, value)


      if count == self.height:
        self.__insertTopLevel()

  def removeElement(self, key):
    foundElement = pointer = self.findElement(key, getValue=False)

    while pointer != None:
      pointer.before.after = pointer.after
      pointer.after.before = pointer.before
      pointer = pointer.above

    if foundElement.key == key:
      return foundElement.value
    else:
      return 'NOT_FOUND'

  def findElement(self, key, getValue=True):
    pointer = self.topLeftElement
    while pointer.below != None:
      pointer = pointer.below

      while pointer.after.key <= key:
        pointer = pointer.after

    if getValue:
      return pointer.value

    return pointer

  def closestKeyAfter(self, key):
    pass

  def closestKeyBefore(self, key):
    pass

  def size(self):
    print(self.length)

  def display(self):
    print('-' * 16)
    element = firstElementInLevel = self.topLeftElement
    level = self.height - 1

    while element != None:
      if element.key == -math.inf:
        print('\nLevel (', level, ')', end=' ')
      elif element.key == math.inf:
        print(element.key)
        firstElementInLevel = element = firstElementInLevel.below
        level = level - 1
        continue

      print('', element.key, '(', element.value, ')', end=' --- ')
      element = element.after
    print('-' * 16)

  def __insertTopLevel(self):
    self.height = self.height + 1
    self.topLeftElement = self.__insertAfterAbove(None, self.topLeftElement, -math.inf, -math.inf)
    self.topLeftElement.before = self.__insertAfterAbove(self.topLeftElement, self.topLeftElement.after, math.inf, math.inf)

  def __insertAfterAbove(self, after, above, key, value):
    node = SkipListNode()

    node.key    = key
    node.value  = value
    node.before = after
    node.below  = above

    if after != None:
      node.after = after.after
      after.after = node

    if above != None:
      node.above  = above.above
      above.above = node

    return node

def test_case(message, condition):
  print(message, '--- Result:', 'PASS' if condition else 'FAIL')

if __name__ == '__main__':
  skip_list = SkipList()

  test_case(
    'The size of the SkipList should be zero, skip_list.size() should return 0',
    skip_list.size() == 0
  )

  skip_list.insertElement(12, 234)
  skip_list.insertElement(17, 423)
  skip_list.insertElement(20, 352)
  skip_list.insertElement(25, 764)
  skip_list.insertElement(31, 366)
  skip_list.insertElement(38, 630)
  skip_list.insertElement(39, 819)
  skip_list.insertElement(42, 577)
  skip_list.insertElement(44, 903)
  skip_list.insertElement(50, 792)

  test_case(
    'The size of the SkipList, skip_list.size() should return 10',
    skip_list.size() == 10
  )

  test_case(
    'Find the value of an element with an existing key, skip_list.findElement(20) should return 352',
    skip_list.findElement(20) == 352
  )

  test_case(
    'Find the value of an with a non-existing key, skip_list.findElement(88) should return None',
    skip_list.findElement(88) == None
  )

  test_case(
    'Update element with an existing key, skip_list.insertElement(20) should return 200',
    skip_list.insertElement(39, 200) == 200
  )

  test_case(
    'Remove element with an existing key, skip_list.removeElement(12) should return 234',
    skip_list.removeElement(12) == 234
  )

  test_case(
    'Removing non-existing key, removeElement(66) should return NOT_FOUND',
    skip_list.removeElement(66) == 'NOT_FOUND'
  )

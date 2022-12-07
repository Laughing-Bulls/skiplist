import math
import random

# TODO: Add documentation to each method

class SkipListNode:
  def __init__(self):
    self.after  = None
    self.before = None
    self.above  = None
    self.below  = None
    self.value  = None
    self.key    = None

class SkipList:
  def __init__(self):
    self.elements_count = 0
    self.levels_count = 0
    self.topLeftElement = None

    self.__insertTopLevel()
    self.__insertTopLevel()

  # insert/replace value
  def insertElement(self, key, value):
    foundElement = pointer = self.__locateKey(key)

    if foundElement.key == key:
      foundElement.value = value
      return foundElement.value

    self.elements_count = self.elements_count + 1
    element = self.__insertAfterAbove(pointer, None, key, value)
    count = 1
    while random.random() > 0.5:
      count = count + 1
      while pointer.above == None:
        pointer = pointer.before

      pointer = pointer.above
      element = self.__insertAfterAbove(pointer, element, key, value)

      if count == self.levels_count:
        self.__insertTopLevel()

  def removeElement(self, key):
    foundElement = pointer = self.__locateKey(key)

    while pointer != None:
      pointer.before.after = pointer.after
      pointer.after.before = pointer.before
      pointer = pointer.above

    if foundElement.key == key:
      return foundElement.value
    else:
      return 'NOT_FOUND'

  def findElement(self, key):
    element = self.__locateKey(key, exact_match=True)

    return element.value if element else None

  def size(self):
    return self.elements_count


  def closestKeyAfter(self, key):
    return self.__locateClosestKey(key, 'after')

  def closestKeyBefore(self, key):
    return self.__locateClosestKey(key, 'before')

  def display(self):
    print('-' * 16)
    element = firstElementInLevel = self.topLeftElement
    level = self.levels_count - 1

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

  def __locateKey(self, key, exact_match=False):
    pointer = self.topLeftElement
    while pointer.below != None:
      pointer = pointer.below

      while pointer.after.key <= key:
        pointer = pointer.after

    return None if exact_match and pointer.key != key else pointer

  def __locateClosestKey(self, key, target):
    located_element = self.__locateKey(key, exact_match=True)

    if located_element:
      target_element = getattr(located_element, target)

      if target_element:
        return target_element.key
      else:
        return key
    else:
      return None

  def __insertTopLevel(self):
    self.levels_count = self.levels_count + 1
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

def test_case(message, actual, expacted):
  condition = actual == expacted
  print('PASS' if condition else 'FAIL', '--- Test Case:', message, expacted)

  if not condition:
    print('Failing value:', actual, '\n')

if __name__ == '__main__':
  skip_list = SkipList()

  test_case(
    'The size of the SkipList should be zero, skip_list.size() should return',
    skip_list.size(),
    0
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
    'The size of the SkipList, skip_list.size() should return',
    skip_list.size(),
    10
  )

  test_case(
    'Find the value of an element with an existing key, skip_list.findElement(20) should return',
    skip_list.findElement(20),
    352
  )

  test_case(
    'Find the value of an with a non-existing key, skip_list.findElement(88) should return',
    skip_list.findElement(88),
    None
  )

  test_case(
    'Update element with an existing key, skip_list.insertElement(20) should return',
    skip_list.insertElement(39, 200),
    200
  )

  test_case(
    'Remove element with an existing key, skip_list.removeElement(12) should return',
    skip_list.removeElement(12),
    234
  )

  test_case(
    'Removing non-existing key, removeElement(66) should return',
    skip_list.removeElement(66),
    'NOT_FOUND'
  )

  test_case(
    'Closest key after an element, closestKeyAfter(25) should return',
    skip_list.closestKeyAfter(25),
    31
  )

  test_case(
    'Closest key before an element, closestKeyBefore(25) should return',
    skip_list.closestKeyBefore(25),
    20
  )

  test_case(
    'Closest key of none existing key, closestKeyBefore(40) should return',
    skip_list.closestKeyBefore(40),
    None
  )

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

    if foundElement.key == key:
      return foundElement.value

  def removeElement(self, key):
    foundElement = pointer = self.findElement(key, getValue=False)

    while pointer != None:
      pointer.before.after = pointer.after
      pointer.after.before = pointer.before
      pointer = pointer.above

    if foundElement.key == key:
      # print('----', foundElement.key, key, foundElement.key == key, foundElement.element)
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

if __name__ == '__main__':
  spl = SkipList()
  spl.insertElement(12, 234)
  spl.insertElement(17, 423)
  spl.insertElement(20, 352)
  spl.insertElement(25, 764)
  spl.insertElement(31, 366)
  spl.insertElement(38, 630)
  spl.insertElement(39, 819)
  spl.insertElement(42, 577)
  spl.insertElement(44, 903)
  spl.insertElement(50, 792)
  spl.insertElement(55, 634)
  spl.display()

  rm = spl.removeElement(12)
  print('Remove key', rm)
  spl.display()

  rm = spl.removeElement(66)
  print('Remove key', rm)

  spl.insertElement(17, 999)
  spl.display()

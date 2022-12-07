import math
import random

# TODO: Add documentation to each method

class SkipListNode:
  def __init__(self):
    self.after   = None
    self.before  = None
    self.above   = None
    self.below   = None
    self.element = None
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
    pointer = self.findElement(key, getValue=False)
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
    pointer = self.findElement(key, getValue=False)

    while pointer != None:
      pointer.before.after = pointer.after
      pointer.after.before = pointer.before
      pointer = pointer.above

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

      print('', element.key, end=' --- ')
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
  spl.insertElement(12, '-')
  spl.insertElement(17, '-')
  spl.insertElement(20, '-')
  spl.insertElement(25, '-')
  spl.insertElement(31, '-')
  spl.insertElement(38, '-')
  spl.insertElement(39, '-')
  spl.insertElement(42, '-')
  spl.insertElement(44, '-')
  spl.insertElement(50, '-')
  spl.insertElement(55, '-')
  spl.display()

  spl.removeElement(12)
  spl.display()

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

    e0 = self.__insertAfterAbove(None, None, -math.inf, -math.inf)
    e1 = self.__insertAfterAbove(e0, None, math.inf, math.inf)
    e2 = self.__insertAfterAbove(None, e0, -math.inf, -math.inf)
    e3 = self.__insertAfterAbove(e2, e1, math.inf, math.inf)

    self.topLeftElement = e2

  # insert/replace value
  def insertElement(self, key, value):
    pointer = self.findElement(key)
    element = self.__insertAfterAbove(pointer, None, key, value)

    while random.random() > 0.5:
      while pointer and pointer.above == None:
        pointer = pointer.before

      if pointer:
        pointer = pointer.above
        element = self.__insertAfterAbove(pointer, element, key, value)


  def removeElement(self, key):
    pass

  def findElement(self, key):
    pointer = self.topLeftElement
    while pointer.below != None:
      pointer = pointer.below

      while pointer.after.key <= key:
        pointer = pointer.after

    return pointer

  def closestKeyAfter(self, key):
    pass

  def closestKeyBefore(self, key):
    pass

  def size(self):
    print(self.length)

  def display(self):
    start = self.topLeftElement

    element = start
    level = 0

    print('\nLevel (', level, ')', end=' ')

    while element != None:
      if element.key == math.inf:
        print('', element.key)

        element = start.below
        start = element
        level = level + 1
        print('\nLevel (', level, ')', end=' ')
      else:
        print('', element.key, end=' --- ')
        element = element.after

  def __insertAfterAbove(self, after, above, key, value):
    node = SkipListNode()

    node.key   = key
    node.value = value
    node.before = after
    node.below = above

    if after != None:
      node.after = after.after
      after.after = node

    if above != None:
      node.above  = above.above
      above.above = node

    return node

spl = SkipList()
spl.insertElement(1, '1')
spl.insertElement(2, '2')
spl.display()

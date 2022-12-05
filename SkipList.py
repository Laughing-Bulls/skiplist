import math

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
    self.levels = []
    self.levels.append(self.__insertLevelAbove(None, None))
    self.levels.append(self.__insertLevelAbove(self.levels[0][0], self.levels[0][1]))

    self.length = 0

  # insert/replace value
  def insertElement(key, value):
    pass

  def removeElement(self, key):
    pass

  def findElement(self, key):
    pointer = self.__topLeftElement()
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
    for level in self.levels:
      # TODO: Print level number
      print("Level --- \n")

      for element in level:
        # TODO: Formate printing elements in one line
        print(element.key)

  def __topLeftElement(self):
    lastLevel = len(self.levels) - 1
    return self.levels[lastLevel][0]

  def __insertLevelAbove(self, firstKey, LastKey):
    plusInfinity  = SkipListNode()
    minusInfinity = SkipListNode()

    minusInfinity.key = -math.inf
    minusInfinity.after   = plusInfinity
    minusInfinity.above   = firstKey

    plusInfinity.key = math.inf
    plusInfinity.before  = minusInfinity
    plusInfinity.above   = LastKey

    return [minusInfinity, plusInfinity]

spl = SkipList()
spl.display()

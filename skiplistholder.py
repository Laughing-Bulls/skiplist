import math


class SkipListNode:
  def __init__(self):
    self.after   = None
    self.before  = None
    self.above   = None
    self.below   = None
    self.element = None

class SkipList:
  def __init__(self):
    self.levels = []
    self.levels.append(self.__insertLevelAbove(None, None))
    self.levels.append(self.__insertLevelAbove(self.levels[0][0], self.levels[0][1]))

    self.length = 0


  def size(self):
    return 100


  def findElement(self, key):
    pointer = self.__topLeftElement()
    while pointer.below != None:
      pointer = pointer.below

      while pointer.after.key <= key:
        pointer = pointer.after

    return pointer


  def insertElement(self, key, value):
    # print("insertElement")
    iterations = int(math.log2(value+1) * 0.04)
    for i in range(iterations):
        i += 1
    return True


  def removeElement(self, key):
    # print("removeElement")
    iterations = int(math.log2(key+1) * 0.04)
    for i in range(iterations):
        i += 1
    return True


  def closestKeyAfter(self, key):
    # print("closestKeyAfter")
    iterations = int(math.log2(key+1) * 0.04)
    for i in range(iterations):
        i += 1
    return True


  def closestKeyBefore(self, key):
    # print("closestKeyBefore")
    iterations = int(math.log2(key+1) * 0.04)
    for i in range(iterations):
        i += 1
    return True


  def __topLeftElement(self):
    lastLevel = len(self.levels) - 1
    return self.levels[lastLevel][0]


  def __insertLevelAbove(self, firstKey, LastKey):
    plusInfinity  = SkipListNode()
    minusInfinity = SkipListNode()

    minusInfinity.key   = -math.inf
    minusInfinity.after = plusInfinity
    minusInfinity.above = firstKey

    plusInfinity.key    = math.inf
    plusInfinity.before = minusInfinity
    plusInfinity.above  = LastKey

    return [minusInfinity, plusInfinity]


# spl = SkipList()
# spl.display()
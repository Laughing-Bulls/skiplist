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
    self.S0 = self.__invertLevelAbove(None, None)
    self.S1 = self.__invertLevelAbove(self.S0[0], self.S0[1])

    self.length = 0

  # insert/replace value
  def insertElement(key, value):
    pass

  def removeElement(self, key):
    pass

  def findElement(self, key):
    pass

  def closestKeyAfter(self, key):
    pass

  def closestKeyBefore(self, key):
    pass

  def size(self):
    print(self.length)

  def display(self):
    pass

  def __invertLevelAbove(self, firstKey, LastKey):
    plusInfinity  = SkipListNode()
    minusInfinity = SkipListNode()

    minusInfinity.element = -math.inf
    minusInfinity.after   = plusInfinity
    minusInfinity.above   = firstKey

    plusInfinity.element = math.inf
    plusInfinity.before  = minusInfinity
    plusInfinity.above   = LastKey

    return [minusInfinity, plusInfinity]

spl = SkipList()
spl.size()

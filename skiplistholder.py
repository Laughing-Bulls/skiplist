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
    #self.levels.append(self.__insertLevelAbove(None, None))
    #self.levels.append(self.__insertLevelAbove(self.levels[0][0], self.levels[0][1]))

    self.length = 0


  def size():
    return 100


  def findElement(self, key):
    print("findElement")
    iterations = 1000 * int(math.log2(key+1))
    for i in range(iterations):
        i =+ 1
    return True


  def insertElement(self, key, value):
    print("insertElement")
    iterations = 1000 * int(math.log2(value+1))
    for i in range(iterations):
        i =+ 1
    return True


  def removeElement(self, key):
    print("removeElement")
    iterations = 1000 * int(math.log2(key+1))
    for i in range(iterations):
        i =+ 1
    return True


  def closestKeyAfter(self, key):
    print("closestKeyAfter")
    iterations = 1000 * int(math.log2(key+1))
    for i in range(iterations):
        i =+ 1
    return True


  def closestKeyBefore(self, key):
    print("closestKeyBefore")
    iterations = 1000 * int(math.log2(key+1))
    for i in range(iterations):
        i =+ 1
    return True


# spl = SkipList()
# spl.display()
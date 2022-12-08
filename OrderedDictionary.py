import math
import random

class DictionaryException(Exception):
    '''Ordered dictionary exception class'''
    pass

class DictionaryElement:
    '''Dictionary ADT element with extra pointer'''

    def __init__(self):
        self.after  = None
        self.above  = None
        self.before = None
        self.below  = None
        self.value  = None
        self.key    = None

class OrderedDictionary:
    '''A SkipList implimntation of a OrderedDictionary'''
    def __init__(self):
        self.elements_count = 0
        self.levels_count = 0
        self.topLeftElement = None

        self.__insertTopLevel()
        self.__insertTopLevel()

    def insertElement(self, key, value):
        '''Inserts new value for new key replaces value of existing one'''
        foundElement = pointer = self.__locateKey(key)

        if foundElement.key == key:
            old_value = foundElement.value
            foundElement.value = value
            return old_value

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
        ''' Removes the key and value '''
        foundElement = pointer = self.__locateKey(key)

        while pointer != None:
            pointer.before.after = pointer.after
            pointer.after.before = pointer.before
            pointer = pointer.above

        if foundElement.key == key:
            return foundElement.value
        else:
            raise DictionaryException('NOT_FOUND')

    def findElement(self, key):
        ''' Returns the value of a key '''
        element = self.__locateKey(key, exact_match=True)

        return element.value if element else None

    def size(self):
        ''' Returns the number of keys '''
        return self.elements_count

    def closestKeyAfter(self, key):
        ''' Returns the value of the smallest and greater or equal the input key '''
        return self.__locateClosestKey(key, 'after')

    def closestKeyBefore(self, key):
        ''' Returns the value of the greater and greater or equal the input key '''
        return self.__locateClosestKey(key, 'before')

    def display(self):
        ''' Prints the configurations of the SkipList '''
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

            is_inf = (target_element.value == math.inf or target_element.value == -math.inf)

            if target_element and not is_inf:
                return target_element.key

        return None

    def __insertTopLevel(self):
        self.levels_count = self.levels_count + 1
        self.topLeftElement = self.__insertAfterAbove(
            None, self.topLeftElement, -math.inf, -math.inf
        )
        self.topLeftElement.before = self.__insertAfterAbove(
            self.topLeftElement, self.topLeftElement.after, math.inf, math.inf
        )

    def __insertAfterAbove(self, after, above, key, value):
        node = DictionaryElement()

        node.key        = key
        node.value    = value
        node.before = after
        node.below    = above

        if after != None:
            node.after = after.after
            after.after = node

        if above != None:
            node.above    = above.above
            above.above = node

        return node

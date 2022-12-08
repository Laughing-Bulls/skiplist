import math
import random

class DictionaryException(Exception):
    pass

class DictionaryElement:
    def __init__(self):
        self.after    = None
        self.before = None
        self.above    = None
        self.below    = None
        self.value    = None
        self.key        = None

class OrderedDictionary:
    def __init__(self):
        self.elements_count = 0
        self.levels_count = 0
        self.topLeftElement = None

        self.__insertTopLevel()
        self.__insertTopLevel()

    '''
        Inserts new value for new key replaces value of existing one
    '''
    def insertElement(self, key, value):
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

    '''
        Removes the key and value
    '''
    def removeElement(self, key):
        foundElement = pointer = self.__locateKey(key)

        while pointer != None:
            pointer.before.after = pointer.after
            pointer.after.before = pointer.before
            pointer = pointer.above

        if foundElement.key == key:
            return foundElement.value
        else:
            raise DictionaryException('NOT_FOUND')

    '''
        Returns the value of a key
    '''
    def findElement(self, key):
        element = self.__locateKey(key, exact_match=True)

        return element.value if element else None

    '''
        Returns the number of keys
    '''
    def size(self):
        return self.elements_count

    '''
        Returns the value of the smallest and greater or equal the input key
    '''
    def closestKeyAfter(self, key):
        return self.__locateClosestKey(key, 'after')

    '''
        Returns the value of the greater and greater or equal the input key
    '''
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

            is_inf = (target_element.value == math.inf or target_element.value == -math.inf)

            if target_element and not is_inf:
                return target_element.key

        return None

    def __insertTopLevel(self):
        self.levels_count = self.levels_count + 1
        self.topLeftElement = self.__insertAfterAbove(None, self.topLeftElement, -math.inf, -math.inf)
        self.topLeftElement.before = self.__insertAfterAbove(self.topLeftElement, self.topLeftElement.after, math.inf, math.inf)

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

def test_case(message, actual, expacted):
    condition = actual == expacted
    print('PASS' if condition else 'FAIL', '--- Test Case:', message, expacted)

    if not condition:
        print('Failing value:', actual, '\n')

if __name__ == '__main__':
    skip_list = OrderedDictionary()

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
        'Update element with an existing key, skip_list.insertElement(39) should return',
        skip_list.insertElement(39, 200),
        819
    )

    # Need to catch exception
    # test_case(
    #     'Removing non-existing key, removeElement(66) should return',
    #     skip_list.removeElement(66),
    #     'NOT_FOUND'
    # )

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

    test_case(
        'Closest key after an element for last key, closestKeyBefore(12) should return',
        skip_list.closestKeyBefore(12),
        None
    )

    test_case(
        'Closest key after an element for last key, closestKeyAfter(50) should return',
        skip_list.closestKeyAfter(50),
        None
    )

    test_case(
        'Remove element with an existing key, skip_list.removeElement(12) should return',
        skip_list.removeElement(12),
        234
    )

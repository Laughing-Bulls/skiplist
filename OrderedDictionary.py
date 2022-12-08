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
        self.top_left_element = None

        self.__insert_top_level()
        self.__insert_top_level()

    def insertElement(self, key, value):
        '''Inserts new value for new key replaces value of existing one'''
        found_element = pointer = self.__locate_key(key)

        if found_element.key == key:
            old_value = found_element.value
            found_element.value = value
            return old_value

        self.elements_count = self.elements_count + 1
        element = self.__insert_after_above(pointer, None, key, value)
        count = 1
        while random.random() > 0.5:
            count = count + 1
            while pointer.above is None:
                pointer = pointer.before

            pointer = pointer.above
            element = self.__insert_after_above(pointer, element, key, value)

            if count == self.levels_count:
                self.__insert_top_level()

    def removeElement(self, key):
        ''' Removes the key and value '''
        found_element = pointer = self.__locate_key(key)

        while pointer is not None:
            pointer.before.after = pointer.after
            pointer.after.before = pointer.before
            pointer = pointer.above

        if found_element.key == key:
            return found_element.value
        else:
            raise DictionaryException('NOT_FOUND')

    def findElement(self, key):
        ''' Returns the value of a key '''
        element = self.__locate_key(key, exact_match=True)

        return element.value if element else None

    def size(self):
        ''' Returns the number of keys '''
        return self.elements_count

    def closestKeyAfter(self, key):
        ''' Returns the value of the smallest and greater or equal the input key '''
        return self.__locate_closest_key(key, 'after')

    def closestKeyBefore(self, key):
        ''' Returns the value of the greater and greater or equal the input key '''
        return self.__locate_closest_key(key, 'before')

    def display(self):
        ''' Prints the configurations of the SkipList '''
        print('-' * 16)
        element = first_element_in_level = self.top_left_element
        level = self.levels_count - 1

        while element is not None:
            if element.key == -math.inf:
                print('\nLevel (', level, ')', end=' ')
            elif element.key == math.inf:
                print(element.key)
                first_element_in_level = element = first_element_in_level.below
                level = level - 1
                continue

            print('', element.key, '(', element.value, ')', end=' --- ')
            element = element.after
        print('-' * 16)

    def __locate_key(self, key, exact_match=False):
        pointer = self.top_left_element
        while pointer.below is not None:
            pointer = pointer.below

            while pointer.after.key <= key:
                pointer = pointer.after

        return None if exact_match and pointer.key != key else pointer

    def __locate_closest_key(self, key, target):
        located_element = self.__locate_key(key, exact_match=True)

        if located_element:
            target_element = getattr(located_element, target)

            is_inf = (target_element.value == math.inf or target_element.value == -math.inf)

            if target_element and not is_inf:
                return target_element.key

        return None

    def __insert_top_level(self):
        self.levels_count = self.levels_count + 1
        self.top_left_element = self.__insert_after_above(
            None, self.top_left_element, -math.inf, -math.inf
        )
        self.top_left_element.before = self.__insert_after_above(
            self.top_left_element, self.top_left_element.after, math.inf, math.inf
        )

    def __insert_after_above(self, after, above, key, value):
        node = DictionaryElement()

        node.key        = key
        node.value    = value
        node.before = after
        node.below    = above

        if after is not None:
            node.after = after.after
            after.after = node

        if above is not None:
            node.above    = above.above
            above.above = node

        return node

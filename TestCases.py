from OrderedDictionary import OrderedDictionary

def test_case(message, actual, expacted):
    ''' Checks values and print PASS or FAILS'''
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
        'Find value of an element with an existing key, skip_list.findElement(20) should return',
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

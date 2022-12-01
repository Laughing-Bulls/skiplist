# This is a holder program


def size():
    return 100


def findElement(something):
    print("findElement")
    for i in range(10000):
        i = i * i
    print(len(something))
    print(type(something))
    return True


def insertElement(something):
    print("insertElement")
    for i in range(10000):
        i = i + i
    print(len(something))
    print(type(something))
    return True


def removeElement(something):
    print("removeElement")
    for i in range(10000):
        i = i ^ 3
    print(len(something))
    print(type(something))
    return True


def closestKeyAfter(something):
    print("closestKeyAfter")
    for i in range(10000):
        i = i / i
    print(len(something))
    print(type(something))
    return True


def closestKeyBefore(something):
    print("closestKeyBefore")
    for i in range(10000):
        i = i % i
    print(len(something))
    print(type(something))
    return True

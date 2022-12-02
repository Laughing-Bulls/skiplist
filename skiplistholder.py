# This is a holder program
import math


def size():
    return 100


def findElement(something):
    print("findElement")
    iterations = 100 * int(math.log2(len(something)))
    for i in range(iterations):
        i = i + i
        i = i ^ 3
        for j in range(iterations):
            j = int(j + i)
    print(len(something))
    print(type(something))
    return True


def insertElement(something):
    print("insertElement")
    iterations = 100 * int(math.log2(len(something)))
    for i in range(iterations):
        i = i + i
        i = i - 20
        i = i ^ 3
        for j in range(iterations):
            j = int(j + i)
    print(len(something))
    print(type(something))
    return True


def removeElement(something):
    print("removeElement")
    iterations = 100 * int(math.log2(len(something)))
    for i in range(iterations):
        i = i + i
        i = i * i
        i = i ^ 3
        for j in range(iterations):
            j = int(j + i)
    print(len(something))
    print(type(something))
    return True


def closestKeyAfter(something):
    print("closestKeyAfter")
    iterations = 100 * int(math.log2(len(something)))
    for i in range(iterations):
        i = i + i
        i = i ^ 3
        i = i / (i+1)
        for j in range(iterations):
            j = int(j + i)
    print(len(something))
    print(type(something))
    return True


def closestKeyBefore(something):
    print("closestKeyBefore")
    iterations = 100 * int(math.log2(len(something)))
    for i in range(iterations):
        i = i + i
        i = i ^ 3
        i = i % (i+1) + (i*2)
        for j in range(iterations):
            j = int(j + i)
    print(len(something))
    print(type(something))
    return True

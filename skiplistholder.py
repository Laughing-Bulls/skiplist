# This is a holder program
import math


def size():
    return 100


def findElement(something):
    print("findElement")
    iterations = 10 * int(math.log2(something+1))
    for i in range(iterations):
        i = i + i
        i = i ^ 3
        for j in range(iterations):
            j = int(j + i)
    return True


def insertElement(something, somethingelse):
    print("insertElement")
    iterations = 10 * int(math.log2(somethingelse+1))
    for i in range(iterations):
        i = i + i
        i = i - 20
        for j in range(iterations):
            j = int(i)
    return True


def removeElement(something):
    print("removeElement")
    iterations = 10 * int(math.log2(something+1))
    for i in range(iterations):
        i = i + i
        i = i * i
        i = i ^ 3
        for j in range(iterations):
            j = int(j + i)
    return True


def closestKeyAfter(something):
    print("closestKeyAfter")
    iterations = 10 * int(math.log2(something+1))
    for i in range(iterations):
        i = i + i
        i = i ^ 3
        i = i / (i+1)
        for j in range(iterations):
            j = int(j + i)
    return True


def closestKeyBefore(something):
    print("closestKeyBefore")
    iterations = 10 * int(math.log2(something+1))
    for i in range(iterations):
        i = i + i
        i = i ^ 3
        i = i % (i+1) + (i*2)
        for j in range(iterations):
            j = int(j + i)
    return True

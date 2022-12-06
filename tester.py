# This is the Python program to test skiplist.
import matplotlib.pyplot as plt
import numpy as np
import math
import random
import time
from SkipList import SkipList
# from SkipList import findElement, insertElement, removeElement, closestKeyAfter, closestKeyBefore


def generate_data(testsizes):
    # Make lists of random number tuples (key-value pairs)
    number_of_tests = len(testsizes)
    print(f"generate_data creates {number_of_tests} tests, with test sizes of {testsizes}")
    max_key_sizes = [i * 2 for i in testsizes]   # establish room for twice as many keys as entries
    inputlists = [[] for i in range(number_of_tests)]
    for i in range(number_of_tests):
        for j in range(testsizes[i]):
            key = random.randint(0, max_key_sizes[i])
            value = key + 1
            key_value = [key, value]
            inputlists[i].append(key_value)
    return inputlists


def run_tests(testsizes, inputlists, function_names):
    # Runs the functions passed on the key-value tuples passed to it
    times = np.zeros((len(function_names), len(inputlists)), dtype=object)  # this matrix will hold the times
    list_number = 0
    for list in inputlists:
        print(f"test list length: {len(list)}")
        sl = SkipList()  # instantiate new skip list object
        # fill the skiplist with odd number keys until it is half full
        for i in range(1, 2 * len(list), 2):
            sl.insertElement(i, 999)
        for key in list:
            function_number = 0
            for name in function_names:
                print(name)     # debugging print
                function = sl.__getattribute__(name)    # get the function from the list of names
                newkey = [key[0] + random.randint(0, 100), key[1]]  # different key-value pair for each function
                times[function_number][list_number] += measure_time(function, newkey)   # add elapsed time
                function_number += 1
        list_number += 1

    print_table(function_names, testsizes, times)
    graph_times(function_names, testsizes, times)
    return True


def measure_time(function, key_value):
    # Returns the time required to complete each function
    if function.__name__ == 'insertElement':
        key = [key_value[0], key_value[1]]  # pass key-value pair
    else:
        key = [key_value[0]]  # pass key only
    start = time.time()  # start timer
    returned = function(*key)       # run function
    print(f"returned: {returned}, key: {key}")     # debugging print
    end = time.time()    # end timer
    time_elapsed = end - start
    return time_elapsed


def print_table(functions, inputsizes, times):
    print()
    print(f"\nResults:")
    print(f"Number of Executions           ", inputsizes)
    for i in range(len(functions)):         # print each row of the output
        print(f"Function {functions[i]:20}:  ", end=" ")
        for j in range(len(times[i])):
            print(f"{times[i][j]:.5} ", end=" ")
        print()
    print()
    return True


def graph_times(functions, inputsizes, times):
    # Displays a graph of the test times
    plt.figure()
    for i in range(len(functions)):     # plot each function
        plt.plot(inputsizes, times[i], label=functions[i])

    # compute n * O(log n) time for comparison
    max_time = np.max(times)            # get maximum time for scaling
    max_test = np.max(inputsizes)       # get maximum value of inputsizes
    compare = [(((max_time + 0.1) / (max_test * math.log2(max_test))) * j * math.log2(j))
               for j in range(2, max_test, 10)]
    x2 = range(2, max_test, 10)
    plt.plot(x2, compare, color='black', label='n times O(log n)')  # plot nlog2(n) for comparison

    axis = plt.gca()
    plt.setp(axis.get_xticklabels(), rotation=25, horizontalalignment='right')
    axis.get_xaxis().set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))
    plt.xlabel("Number of Executions")
    plt.ylabel("Execution Time (seconds)")
    plt.title("Time to Execute Each Function x Times")
    plt.legend()
    plt.show()
    return True


# Press the green button to run the script.
if __name__ == '__main__':

    testsizes = [100, 500, 1000, 2500, 5000]      # This controls the sizes of the test data
    inputlists = generate_data(testsizes)           # This generates the key-value pairs

    function_names = ['findElement', 'insertElement', 'removeElement', 'closestKeyAfter', 'closestKeyBefore']
    run_tests(testsizes, inputlists, function_names)                # This tests the functions and graphs results

    print("That's all, Folks!")

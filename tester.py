# This is the Python program to test skiplist.
import matplotlib.pyplot as plt
import numpy as np
import math
import random
import time
from skiplistholder import findElement, insertElement, removeElement, closestKeyAfter, closestKeyBefore, size

"""STILL NEED TO:
    1.  Initialize skiplist
    2.  Refine the graphing function
    """

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


def run_tests(testsizes, inputlists, functions):
    # Runs the functions passed on the key-value tuples passed to it
    times = np.zeros((len(functions), len(inputlists)), dtype=object)  # this matrix will hold the times
    list_number = 0
    for list in inputlists:
        print(f"test list length: {len(list)}")
        # skiplist()   # initialize new skip list  ######################################
        # fill the skiplist with odd number keys until it is half full
        for i in range(1, 2 * len(list), 2):
            insertElement(i, 999)
        for key in list:
            function_number = 0
            for function in functions:
                times[function_number][list_number] += measure_time(function, key)   # add elapsed time
                function_number += 1
        list_number += 1

    print_table(functions, testsizes, times)
    # graph_times(functions, testsizes, times)
    return True


def measure_time(function, key_value):
    # Returns the time required to complete each function
    if function == insertElement:
        key = [key_value[0], key_value[1]]  # pass key-value pair
    else:
        key = [key_value[0]]  # pass key only
    start = time.time()  # start timer
    function(*key)       # run function
    end = time.time()    # end timer
    time_elapsed = end - start
    return time_elapsed


def print_table(functions, inputsizes, times):
    print()
    print(f"\nResults:")
    print(f"Number of Executions           ", inputsizes)
    for i in range(len(functions)):         # print each row of the output
        print(f"Function {functions[i].__name__:20}:  ", end=" ")
        for j in range(len(times[i])):
            print(f"{times[i][j]:.5} ", end=" ")
        print()
    print()
    return True


def graph_times(functions, inputsizes, times):
    # Displays a graph of the test times
    print(f"graph_times: {times}")

    x = []
    compare = []
    max_length = 0
    max_time = max(times)
    for i in range(inputsizes):
        x.append(inputsizes[i])
        max_length = max(max_length, inputsizes[i])
    y = times
    compare = [(((max_time + 0.1) / math.log2(max_length)) * math.log2(j)) for j in range(2, max_length, 10)]
    x2 = range(2, max_length, 10)
    print(f"x = {x}, y = {y}, max time = {max_time + 0.1}")                          # print output values
    plt.plot(x, y, color='blue', label='Function')      # plot the Graph
    plt.plot(x2, compare, color='red', label='O(log n)')  # plot log2(n) for comparison
    plt.title("Skiplist Time Function")
    plt.xlabel("Number of Elements")
    plt.ylabel("Execution Time (seconds)")
    axis = plt.gca()
    axis.get_xaxis().get_major_formatter().set_scientific(False)
    plt.legend()
    plt.show()
    time.sleep(2)   # Sleep for 2 seconds
    return True


# Press the green button to run the script.
if __name__ == '__main__':

    testsizes = [100, 200, 400, 800]      # This controls the sizes of the test data
    inputlists = generate_data(testsizes)           # This generates the key-value pairs

    functions = [findElement, insertElement, removeElement, closestKeyAfter, closestKeyBefore]
    run_tests(testsizes, inputlists, functions)                # This tests the functions and graphs results

    print("That's all, Folks!")

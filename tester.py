# This is the Python program to test skiplist.
import matplotlib.pyplot as plt
import math
import random
import time
from skiplistholder import findElement, insertElement, removeElement, closestKeyAfter, closestKeyBefore, size


def test_size():
    # This function controls the sizes of the test data
    print("Running test_size")  # Press Ctrl+F8 to toggle the breakpoint.
    testsizes = [1000, 10000, 100000, 1000000]
    return testsizes


def generate_data(testsizes):
    # Makes lists of random number tuples
    number_of_tests = len(testsizes)
    print(f"generate_data will run {number_of_tests} tests")
    print(f"The test sizes will be: {testsizes}")
    max_key_sizes = testsizes * 2   # establish twice as many keys as entries
    inputlists = [[] for i in range(number_of_tests)]
    print(inputlists)
    for i in range(number_of_tests):
        for j in range(testsizes[i]):
            key = random.randint(0, max_key_sizes[i])
            value = key + 1
            key_value = [key, value]
            inputlists[i].append(key_value)
    print(len(inputlists))
    return inputlists


def measure_time(function, inputlist):
    # Returns the time required to complete each function
    start = time.time()
    print(f"doing something {function}")
    function(inputlist)
    end = time.time()
    time_elapsed = end - start
    print(f"Elapsed_time: {time_elapsed} seconds")
    return time_elapsed


def run_tests(functions, inputlists):
    # Runs the function passed on the tuples passed to it

    for function in functions:
        times = []
        for list in inputlists:
            times.append(measure_time(function, list))
        graph_times(inputlists, times)
        time.sleep(1)   # Sleep for 1 second
    return True


def graph_times(inputlists, times):
    # Displays a graph of the test times
    print(f"graph_times: {times}")

    x = []
    compare = []
    for i in range(len(inputlists)):
        x.append(len(inputlists[i]))
        compare.append(math.log2(x[i]) * 0.002)
    y = times
    print(f"x = {x}, y = {y}, overlay = {compare}")
    plt.plot(x, y, color='blue')      # plot the Graph
    plt.plot(x, compare, color='red')
    plt.title("Skiplist Time Function")
    plt.xlabel("Number of Elements")
    plt.ylabel("Execution Time (seconds)")
    plt.show()
    return True


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    testsizes = test_size()
    inputlists = generate_data(testsizes)
    functions = [findElement, insertElement, removeElement, closestKeyAfter, closestKeyBefore]
    run_tests(functions, inputlists)
    print("That's all, Folks!")

# This is the Python program to test skiplist.
import matlabplt as plt
import random
import time
from skiplistholder import findElement, insertElement, removeElement, closestKeyAfter,closestKeyBefore, size


def test_size():
    # Use a breakpoint in the code line below to debug your script.
    print("Running test_size")  # Press Ctrl+F8 to toggle the breakpoint.
    testsizes = [5, 10, 15]
    return testsizes


def generate_data(testsizes):
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


def measure_time(function):
    start = time.time()
    print(f"doing something {function}")
    function([10000])
    end = time.time()
    time_elapsed = end - start
    print(f"Elapsed_time: {time_elapsed} seconds")
    return time_elapsed


def run_test(functions):
    for function in functions:
        times = measure_time(function, inputlists)
    return times    


def graph_times(times):
    print(f"graph_times: {times}")
    return True


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    testsizes = test_size()
    inputlists = generate_data(testsizes)
    functions = [findElement, insertElement, removeElement, closestKeyAfter, closestKeyBefore]
    times = run_test(functions)
    graph_times(times)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# This is the Python program to test skiplist.
import matplotlib.pyplot as plt
import math
import random
import time
from skiplistholder import findElement, insertElement, removeElement, closestKeyAfter, closestKeyBefore, size


def generate_data(testsizes):
    # Makes lists of random number tuples (key-value pairs)
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
        # time.sleep(1)   # Sleep for 1 second
    return True


def graph_times(inputlists, times):
    # Displays a graph of the test times
    print(f"graph_times: {times}")

    x = []
    compare = []
    max_length = 0
    max_time = max(times)
    for i in range(len(inputlists)):
        x.append(len(inputlists[i]))
        max_length = max(max_length, len(inputlists[i]))
    y = times
    compare = [(((max_time + 0.1)/ math.log2(max_length)) * math.log2(j)) for j in range(2, max_length, 10)]
    x2 = range(2, max_length, 10)
    print(f"x = {x}, y = {y}, max time = {max_time + 0.1}")                          # print output values
    plt.plot(x, y, color='blue', label='Function')      # plot the Graph
    plt.plot(x2, compare, color='red', label='O(log n)') # plot log2(n) for comparison
    plt.title("Skiplist Time Function")
    plt.xlabel("Number of Elements")
    plt.ylabel("Execution Time (seconds)")
    axis = plt.gca()
    axis.get_xaxis().get_major_formatter().set_scientific(False)
    plt.legend()
    plt.show()
    return True


# Press the green button to run the script.
if __name__ == '__main__':
    testsizes = [100, 5000, 10000, 100000, 500000]      # This controls the sizes of the test data
    inputlists = generate_data(testsizes)           # This generates the key-value pairs
    functions = [findElement, insertElement, removeElement, closestKeyAfter, closestKeyBefore]
    run_tests(functions, inputlists)                # This tests the functions and graphs results

    print("That's all, Folks!")

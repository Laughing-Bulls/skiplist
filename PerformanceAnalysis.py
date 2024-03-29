# This is the Python program to test skiplist.
import math
import random
import time
import matplotlib.pyplot as plt
import numpy as np
from OrderedDictionary import OrderedDictionary, DictionaryException


def generate_keys(number_tests, dictionary_sizes, functions):
    # Make lists of random number tuples (key-value pairs)
    number_of_dictionaries = len(dictionary_sizes)
    number_of_functions = len(functions)
    print(f"generate_keys: creates {number_of_dictionaries} tests, with trial sizes of {number_tests}")
    max_key_sizes = [i * 2 for i in dictionary_sizes]   # establish room for twice as many keys as entries
    inputlists = [[] for i in range(number_of_dictionaries)]
    for i in range(number_of_dictionaries):                     # for each Skiplist dictionary size
        for j in range(number_tests * number_of_functions):     # generate random key-value pairs
            key = random.randint(0, max_key_sizes[i])
            value = key + 1     # value is arbitrarily equal to  key+1
            key_value = [key, value]
            inputlists[i].append(key_value)
    return inputlists


def run_tests(trialsize, dictionary_sizes, test_values, function_names):
    # Runs the functions on the test key-value tuples passed to it
    number_of_functions = len(function_names)
    times = np.zeros((len(function_names), len(test_values)), dtype=object)  # this matrix will hold the times
    dictionary_number = 0
    for dictionary in dictionary_sizes:     # for each dictionary size
        print(f"Number of dictionary entries being filled: {dictionary}")
        sl = OrderedDictionary()                     # instantiate new skip list object
        # fill the skiplist with odd number keys until it is half full
        for i in range(1, 2 * dictionary, 2):   # fill initial skiplist with odd numbers
            sl.insertElement(i, i + 1)
        for j in range(trialsize):
            function_number = 0
            for operation in function_names:                 # cycle through each operation
                function = sl.__getattribute__(operation)    # get the function from the list of names
                # use different key-value pair for each operation
                random_key = test_values[dictionary_number][j * number_of_functions + function_number]
                # print(f"Skiplist operation: {operation}, key-value: {random_key}")   # debugging print
                # add elapsed time to the times matrix
                times[function_number][dictionary_number] += measure_time(function, random_key)
                function_number += 1
        dictionary_number += 1

    avg_times = (times / trialsize) * 1000      # compute average time and convert to milliseconds
    print_table(function_names, dictionary_sizes, avg_times)    # print a table of results
    graph_times(function_names, dictionary_sizes, avg_times)    # graph the results
    return True


def measure_time(function, key_value):
    # Returns the time required to complete each function
    if function.__name__ == 'insertElement':
        key = [key_value[0], key_value[1]]  # pass key-value pair
    else:
        key = [key_value[0]]                # pass key only

    start = time.perf_counter()  # start timer
    try:
        returned = function(*key)    # run function
    except DictionaryException:    # catch DictionaryException if thrown by removeElement
        pass
    end = time.perf_counter()    # end timer
    time_elapsed = end - start
    # print(f"Time elapsed: {time_elapsed:.5}")  # debugging print
    # print(f"Value returned: {returned}")  # debugging print
    return time_elapsed


def print_table(functions, inputsizes, times):
    print()
    print(f"\nResults (in milliseconds):")
    print(f"Size of Skiplist               ", inputsizes)
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

    # compute log2(n) time function for comparison
    max_time = np.max(times)            # get maximum time for scaling
    max_test = np.max(inputsizes)       # get maximum value of inputsizes
    compare = [(((max_time + 0.005) / (math.log2(max_test))) * math.log2(j))
               for j in range(2, max_test, 10)]
    x2 = range(2, max_test, 10)
    plt.plot(x2, compare, color='black', label='O(log n)')  # plot O(log n) time for comparison

    axis = plt.gca()
    plt.setp(axis.get_xticklabels(), rotation=25, horizontalalignment='right')
    axis.get_xaxis().set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))
    plt.legend.loc = 'lower right'
    plt.xlabel("Keys in Skiplist")
    plt.ylabel("Execution Time (milliseconds)")
    plt.title("Average Time to Execute Each Function")
    plt.legend()
    plt.show()
    # individual_graphs(functions, inputsizes, times, x2, compare)  # used to create individual graphs for Summary
    return True


def individual_graphs(functions, inputsizes, times, x2, compare):
    for i in range(len(functions)):  # plot each function individually
        plt.figure()
        plt.plot(inputsizes, times[i], label=functions[i])  # plot function
        plt.plot(x2, compare, color='black', label='O(log n)')  # plot O(log n) time for comparison

        axis = plt.gca()
        plt.setp(axis.get_xticklabels(), rotation=25, horizontalalignment='right')
        axis.get_xaxis().set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))
        plt.legend.loc = 'lower right'
        plt.xlabel("Keys in Skiplist")
        plt.ylabel("Execution Time (milliseconds)")
        plt.title("Average Time to Execute Function")
        plt.legend()
        plt.show()
    return True


# Main script.
if __name__ == '__main__':

    function_names = ['findElement', 'insertElement', 'removeElement', 'closestKeyAfter', 'closestKeyBefore']
    dictionary_sizes = [50000, 100000, 500000, 1000000, 2500000]  # This controls the sizes of the skiplists
    trialsize = 1000  # This controls the number of trials

    inputlists = generate_keys(trialsize, dictionary_sizes, function_names)   # This generates random key-value pairs

    run_tests(trialsize, dictionary_sizes, inputlists, function_names)  # This tests the functions and graphs results

    print("That's all, Folks!")

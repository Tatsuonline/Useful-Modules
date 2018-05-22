""" The beyonder takes in the test function along with a
    dictionary of tests and expected outputs and provides
    a fancy output. """

def beyonder (test_function, test_dictionary):

    counter = 0
    
    for key in test_dictionary.keys():
        print("\n=== \033[94mTest Case# " + str(counter) + "\033[0m ===")
        print("Input: " + str(key))
        print("Expected Output: " + str(test_dictionary[key]))
        print("Actual Output: " + str(test_function(key)))
        if test_function(key) == test_dictionary[key]:
            print("Result: \033[92mPASS\033[0m")
        else:
            print("Result: \033[91;5mFAIL\033[0m")

        counter += 1

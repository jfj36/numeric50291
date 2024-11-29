import numpy as np
###
## Module for basic statistics
###

## Here I need functions to take in data
## and do the following:
##
## 1. Calculate mean. Calculate median. Calculate 
##    standard deviation.
##
## 2. Display the result with a nice print statement.
##
## 3. Plot a histogram of the data, with the mean and median 
##    marked on the plot. This should be part of a new Python
##    file in the package, called graphics.py.
##
## 4. Remember to provide a mechanism for checking that the input
##    is a numpy array or a list (if a list, you must convert it
##    to a numpy array).
##
## 5. Also, do something and/or throw an exception/message if the
##    numpy and matplotlib packages are not installed.



def calculate_statistics(data):
    # Check if input is a numpy array
    if not isinstance(data, np.ndarray):
        # Check if input can be converted to a numpy array
        try:
            data = np.array(data)
        except:
            raise ValueError("Input must be a numpy array or convertible to a numpy array")

    # Calculate mean, median, variance, and standard deviation
    mean = np.mean(data)
    median = np.median(data)
    variance = np.var(data)
    std_dev = np.std(data)

    # Display the results
    print("Mean:", mean)
    print("Median:", median)
    print("Variance:", variance)
    print("Standard Deviation:", std_dev)

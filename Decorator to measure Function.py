import time

# Function to measure execution time
def measure_time(func):
    # Start the timer
    start_time = time.time() 
    # Call the function 
    func()  
    end_time = time.time()  
    print(f"Time taken by {func.__name__}: {end_time - start_time:.6f} seconds")

# Function 1: Generate list using range
def measure_with_range():
    # Using range to generate a list
    my_list = list(range(100000))  
    return my_list

# Function 2: Generate list using list comprehension
def measure_with_comprehension():
    # Using list comprehension
    my_list = [i for i in range(100000)]  
    return my_list

# Function 3: Generate list using append
def measure_with_append():
    # Empty list
    my_list = []  
    # Loop to append values
    for i in range(100000):  
        my_list.append(i)
    return my_list

# Function 4: Generate list using concatenation
def measure_with_concatenation():
    list = [] 
    # Loop to concatenate values
    for i in range(10000):  
        list = list + [i]
    return list

# Measure the time for each function
measure_time(measure_with_range)
measure_time(measure_with_comprehension)
measure_time(measure_with_append)
measure_time(measure_with_concatenation)


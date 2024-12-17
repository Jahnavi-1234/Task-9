import time

# Step 1: Define the decorator to measure execution time
def measure_time(func):
    def wrapper(*args, **kwargs):
        # start the timer
        start_time = time.time()  
        # Call the original function
        result = func(*args, **kwargs)  
        end_time = time.time()  
        print(f"Time taken by {func.__name__}: {end_time - start_time:.6f} seconds")
        return result
    return wrapper

# Step 2: Apply the decorator to each function

@measure_time
def measure_with_range():
    # Generate list using range
    my_list = list(range(100000))  
    return my_list

@measure_time
def measure_with_comprehension():
    # Generate list using list comprehension
    my_list = [i for i in range(100000)]  
    return my_list

@measure_time
def measure_with_append():
    # Generate list using append
    my_list = []  
    for i in range(100000):
        my_list.append(i)
    return my_list

@measure_time
def measure_with_concatenation():
    # Generate list using concatenation
    my_list = []  
    # Reduced to 10000 to avoid long execution time
    for i in range(10000):  
        my_list = my_list + [i]
    return my_list

# Step 3: Call the functions
measure_with_range()
measure_with_comprehension()
measure_with_append()
measure_with_concatenation()

 


# Function to generate Fibonacci sequence up to n terms
def fibonacci_generator(n):
    # Initialize the first two Fibonacci numbers
    a, b = 0, 1  
    for i in range(n):
        # Yield the current Fibonacci number
        yield a  
        # Update a and b for the next Fibonacci number
        a, b = b, a + b  
for number in fibonacci_generator(100):  
    print(number, end=" ")

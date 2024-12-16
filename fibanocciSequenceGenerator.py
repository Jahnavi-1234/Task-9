# Function to generate Fibonacci sequence up to n terms
def fibonacci(n):
    a, b = 0, 1  
    for i in range(n):  
        # Print current value of a
        print(a, end=" ")  
        # Update a and b to the next values
        a, b = b, a + b  

n = int(input("Enter the number of terms in the Fibonacci sequence: "))  
# Call the function to print the Fibonacci sequence
fibonacci(n)  
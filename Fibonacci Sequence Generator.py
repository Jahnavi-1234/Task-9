# Function to generate Fibonacci sequence up to n terms
def fibonacci(n):
    a, b = 0, 1  # Starting values of Fibonacci sequence
    for i in range(n):  # Loop n times
        print(a, end=" ")  # Print current value of a
        a, b = b, a + b  # Update a and b to the next values

# Example usage
n = int(input("Enter the number of terms in the Fibonacci sequence: "))  # Ask user for number of terms
fibonacci(n)  # Call the function to print the Fibonacci sequence

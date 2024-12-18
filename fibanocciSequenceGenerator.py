# Function to generate Fibonacci sequence up to n terms
def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b

# Get user input
n = int(input("Enter the number of Fibonacci terms you want: "))

# Generate and print Fibonacci sequence
for number in fibonacci(n):
    print(number, end=" ")


# Fibonacci Iterator

class FibonacciIterator:
    def __init__(self, max_count):
        # Total numbers to generate
        self.max_count = max_count  
        # First number in the sequence
        self.prev = 0  
        self.curr = 1  
        # Counter to keep track of how many numbers have been generated
        self.count = 0  
    def __iter__(self):
        return self
    def __next__(self):
        if self.count >= self.max_count:
            raise StopIteration

        # Return the current number and move to the next
        result = self.prev
        # Calculate the next Fibonacci number
        next_value = self.prev + self.curr  
        # Update previous number
        self.prev = self.curr  
         # Update current number
        self.curr = next_value 
        # Increment the counter
        self.count += 1  
        return result
max_count= int(input("Enter the number of fibanocci terms you want: "))
print("Fibonacci numbers:")
fib_iter = FibonacciIterator(max_count)
for num in fib_iter:
    print(num, end=" ")


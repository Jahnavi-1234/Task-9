# Fibonacci Iterator

class FibonacciIterator:
    def __init__(self, max_count):
        self.max_count = max_count  # Total numbers to generate
        self.prev = 0  # First number in the sequence
        self.curr = 1  # Second number in the sequence
        self.count = 0  # Counter to keep track of how many numbers have been generated
    def __iter__(self):
        return self
    def __next__(self):
        if self.count >= self.max_count:
            raise StopIteration

        # Return the current number and move to the next
        result = self.prev
        next_value = self.prev + self.curr  # Calculate the next Fibonacci number
        self.prev = self.curr  # Update previous number
        self.curr = next_value  # Update current number
        self.count += 1  # Increment the counter
        return result
print("Fibonacci numbers:")
fib_iter = FibonacciIterator(50)
for num in fib_iter:
    print(num, end=" ")


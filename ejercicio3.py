import timeit
import matplotlib.pyplot as plt

# Function to measure execution time for O(n) complexity with if-then-else

def conditional_loop(n):
    for i in range(n):
        if i % 2 == 0:
            pass  # Simulating an operation
        else:
            pass  # Simulating another operation

# Function to measure execution time
def process_time(n):
    return timeit.timeit(lambda: conditional_loop(n), number=1)

# Values of n
n_values = [1, 10, 100, 1000, 10000, 100000]
actual_times = [process_time(n) for n in n_values]

# Plot results
plt.figure(figsize=(8, 5))
plt.plot(n_values, actual_times, marker='o', linestyle='-', label='Processing Time (O(n))')
plt.xscale("log")  # Logarithmic scale for x-axis
plt.xlabel("n (Input Size)")
plt.ylabel("Time (seconds)")
plt.title("Processing Time vs. Input Size (If-Then-Else O(n))")
plt.legend()
plt.grid(True)
plt.show()
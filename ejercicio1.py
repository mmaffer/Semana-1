import timeit
import matplotlib.pyplot as plt

# Function to measure execution time for O(log n) complexity
def logarithms(n):
    i = 1
    while i <= n:
        i *= 2  # Doubling i in each iteration

# Function to measure execution time
def process_time(n):
    return timeit.timeit(lambda: logarithms(n), number=1)

# Values of n
n_values = [1, 10, 100, 1000, 10000, 100000, 1000000]
actual_times = [process_time(n) for n in n_values]

# Plot results
plt.figure(figsize=(8, 5))
plt.plot(n_values, actual_times, marker='o', linestyle='-', label='Processing Time (O(log n))')
plt.xscale("log")  # Logarithmic scale for x-axis
plt.xlabel("n (Input Size)")
plt.ylabel("Time (seconds)")
plt.title("Processing Time vs. Input Size (O(log n))")
plt.legend()
plt.grid(True)
plt.show()
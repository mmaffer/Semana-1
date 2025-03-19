import timeit
import matplotlib.pyplot as plt

# Function to measure execution time for O(n) complexity
def simple_loop(n):
    for i in range(n):
        pass  # Simulating an operation

# Function to measure execution time
def process_time(n):
    return timeit.timeit(lambda: simple_loop(n), number=1)

# Values of n
n_values = [10**2, 10**3, 10**4, 10**5, 10**6]
actual_times = [process_time(n) for n in n_values]

# Plot results
plt.figure(figsize=(8, 5))
plt.plot(n_values, actual_times, marker='o', linestyle='-', label='Processing Time (O(n))')
plt.xscale("log")  # Logarithmic scale for x-axis
plt.xlabel("n (Input Size)")
plt.ylabel("Time (seconds)")
plt.title("Processing Time vs. Input Size (O(n))")
plt.legend()
plt.grid(True)
plt.show()
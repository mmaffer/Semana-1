import timeit
import matplotlib.pyplot as plt


# Define the function to measure execution time
def process_time(n):
    start_time = timeit.default_timer()


    # Simple loop - O(n)
    for i in range(n):
        pass  # Simulating some operation


    # Nested loop - O(n^2)
    for i in range(n):
        for j in range(n):
            pass  # Simulating some operation


    end_time = timeit.default_timer()
    return end_time - start_time


# Values of n
n_values = [100, 400, 600, 800, 1000, 1100]
times = [process_time(n) for n in n_values]


# Plot the results
plt.figure(figsize=(8, 5))
plt.plot(n_values, times, marker='o', linestyle='-', label='Processing Time')
plt.xlabel("n (input size)")
plt.ylabel("Time (seconds)")
plt.title("Processing Time vs. Input Size (O(n + n²))")
plt.legend()
plt.grid(True)
plt.show()
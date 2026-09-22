import time
import matplotlib.pyplot as plt

#Reversal
def reverse_array(A):
    """Reverse a list of ints in place."""
    start = 0
    end = len(A) - 1
    while start < end:
        temp = A[start]
        A[start] = A[end]
        A[end] = temp
        start += 1
        end -= 1

#Runtime information
def get_runtime(n):
    """Times one reversal of a list of size n. Returns time in microseconds."""
    A = list(range(n))
    start_time = time.perf_counter()
    reverse_array(A)
    end_time = time.perf_counter()
    return (end_time - start_time) * 1_000_000

# Setting the list and reversing it
my_list = [1, 2, 3, 4, 5]
print("Before reversal:", my_list)
reverse_array(my_list)
print("After reversal:", my_list)

# Sizes required for the plot
sizes = [500, 1500, 2500]
runtimes = []

for n in sizes:
    runtime = get_runtime(n)
    runtimes.append(runtime)
    print(f"n = {n}: {runtime:.4f} microseconds")

# Plot runtime vs. array size
plt.plot(sizes, runtimes, marker="o")
plt.title("Runtime of reverse_array vs. Input Size")
plt.xlabel("Array size (n)")
plt.ylabel("Runtime (microseconds)")
plt.savefig("runtime_plot.png", dpi=150)
plt.show()

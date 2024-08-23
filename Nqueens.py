import minizinc
import time
import matplotlib.pyplot as plt

# Create MiniZinc model instance
model = minizinc.Model("n_queens.mzn")  # Path to your MiniZinc model file
gecode = minizinc.Solver.lookup("gecode")

# Initialize lists to store N values and average execution times
n_values = []
average_execution_times = []

# Number of repetitions
num_repeats = 3

# Loop over values of N and run the model
for N in range(5, 90):
    # Store times for each repetition
    times = []
    
    for _ in range(num_repeats):
        # Set the value of N in the model
        instance = minizinc.Instance(gecode, model)
        instance["N"] = N
        
        # Measure the time for solving the model
        start_time = time.time()
        result = instance.solve()
        end_time = time.time()
        
        # Calculate runtime
        runtime = (end_time - start_time) * 1000  # Convert to milliseconds
        
        # Append runtime to the list of times
        times.append(runtime)
    
    # Calculate the average runtime
    average_runtime = sum(times) / len(times)
    
    # Store N and average runtime
    n_values.append(N)
    average_execution_times.append(average_runtime)
    
    # Print the result for the current N
    if result.solution:
        print(f"N = {N}")
        print(f"Solution: {result.solution}")
        print(f"Average Runtime: {average_runtime:.2f} ms over {num_repeats} repetitions")
    else:
        print(f"N = {N}")
        print("No solution found.")
    
    print("-" * 40)

# Plot the results
plt.figure(figsize=(10, 6))
plt.plot(n_values, average_execution_times, marker='o', linestyle='-', color='b')
plt.xlabel('N (Size of the Board)')
plt.ylabel('Average Execution Time (ms)')
plt.title('Average Execution Time vs. N for N-Queens Problem')
plt.grid(True)
plt.show()

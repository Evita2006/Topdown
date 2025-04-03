import time
import tracemalloc
import sys

# Increase recursion limit
sys.setrecursionlimit(20000)

def fibonacci_top_down(n, memo={}):
    if n <= 1:
        return n
    if n in memo: 
        return memo[n]
    memo[n] = fibonacci_top_down(n - 1, memo) + fibonacci_top_down(n - 2, memo)
    return memo[n]

def main():
    tracemalloc.start()
    start_time = time.time()
    try:
        n = int(input("Enter a number: "))
        result = fibonacci_top_down(n)
        print(f"Fibonacci({n}) = {result}")
    except RecursionError:
        result = "Recursion limit exceeded"
        print(f"Fibonacci({n}) = {result}")
    end_time = time.time()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    print(f"Time: {end_time - start_time:.6f}s")
    print(f"Memory: Current={current / 1024:.2f}KB, Peak={peak / 1024:.2f}KB")

main()
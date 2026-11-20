import numpy as np
import timeit

rng = np.random.default_rng(42)
latency_ms = rng.uniform(5, 250, 1_000_000)

def loop_version():
    squared = []
    for value in latency_ms:
        seconds = value / 1000.0
        squared.append(seconds ** 2)
    return squared

def vectorized_version():
    seconds = latency_ms / 1000.0
    return seconds ** 2

loop_time = timeit.timeit(loop_version, number=1)
vector_time = timeit.timeit(vectorized_version, number=3) / 3
result = vectorized_version()

print("BASE CASE: one million latency values")
print("First five squared values:", result[:5])
print(f"Loop time: {loop_time:.4f} seconds")
print(f"Vectorized time: {vector_time:.4f} seconds")
print(f"Approximate speed-up: {loop_time / vector_time:.1f}x")

# Changed parameter: use 100,000 rather than 1,000,000 measurements
smaller = latency_ms[:100_000]
print("\nCHANGED CASE: 100,000 measurements")
print("Mean squared latency (seconds squared):", np.mean((smaller / 1000) ** 2))

# Related case: vectorized conversion of a batch of file sizes from MB to GB
file_sizes_mb = np.array([500, 1200, 2500, 800])
print("\nRELATED CASE: file-size conversion to GB")
print(np.round(file_sizes_mb / 1024, 3))

# Big O Classifications
# Function A: O(1) - Accessing the first element of a list takes constant time.
# Function B: O(n) - The function checks every element in the list once.
# Function C: O(n^2) - Two nested loops each iterate through the list.
# Function D: O(log n) - n is repeatedly halved until it becomes <= 1.
# Function E: O(n log n) - sum(data) is O(n), sorted(data) is O(n log n), and indexing is O(1); the dominant term is O(n log n).

import random
import time
from pathlib import Path


class txt:
    """Simple text-file helper with useful read/write/append behavior."""

    def __init__(self, path):
        self.path = Path(path)

    def read(self):
        with self.path.open("r", encoding="utf-8") as file:
            return file.read()

    def write(self, content):
        with self.path.open("w", encoding="utf-8") as file:
            return file.write(content)

    def append(self, content):
        with self.path.open("a", encoding="utf-8") as file:
            return file.write(content)

    def close(self):
        return None


# O(n^2) solution
def count_pairs_n2(data, target):
    count = 0
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[i] + data[j] == target:
                count += 1
    return count

# O(n) solution
def count_pairs_n(data, target):
    seen = {}
    count = 0

    for num in data:
        complement = target - num

        if complement in seen:
            count += seen[complement]

        seen[num] = seen.get(num, 0) + 1

    return count


def benchmark():
    sizes = [1000, 5000, 10000, 20000, 40000,]
    target = 100

    file_path = Path(r"benchmark_results.txt")
    results = txt(file_path)
    results.write("PAIR COUNTING BENCHMARK RESULTS\n")
    results.append("=" * 60 + "\n\n")

    for size in sizes:
        data = [random.randint(0, 100) for _ in range(size)]

        start = time.perf_counter()
        result_n2 = count_pairs_n2(data, target)
        time_n2 = time.perf_counter() - start

        start = time.perf_counter()
        result_n = count_pairs_n(data, target)
        time_n = time.perf_counter() - start

        output = (
            f"List Size: {size}\n"
            f"O(n²) Result: {result_n2} pairs\n"
            f"O(n²) Time: {time_n2:.6f} seconds\n"
            f"O(n) Result: {result_n} pairs\n"
            f"O(n) Time: {time_n:.6f} seconds\n"
            + "-" * 60 + "\n"
        )

        print(output)
        results.append(output)

    print(f"Benchmark results saved to {file_path}.")
    results.close()
    print("Benchmark complete.")
    


if __name__ == '__main__':
    benchmark()

import matplotlib.pyplot as plt
import numpy as np


def is_prime(n):
    """Check if a number is a prime number."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def first_n_primes(n):
    """Generate the first n prime numbers."""
    primes = []
    num = 2
    while len(primes) < n:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes

def differences_between_consecutive_primes(primes):
    """Calculate the differences between consecutive prime numbers."""
    differences = []
    for i in range(len(primes) - 1):
        diff = primes[i] - primes[i + 1]
        differences.append(diff)
    return differences

def differences_increase_between_primes(primes):
    """Calculate the difference in increase between consecutive prime numbers."""
    differences = []
    for i in range(len(primes) - 1):
        diff_increase = primes[i + 1] - primes[i]
        differences.append(diff_increase)
    return differences

def find_top_repeated_numbers(numbers, top_count=1):
    """Find the top repeated numbers and their counts in a list."""
    counts = {}
    for num in numbers:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
    
    # Sort counts dictionary by values in descending order
    sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)
    
    # Extract the top repeated numbers and their counts
    top_repeated = sorted_counts[:top_count]
    
    return top_repeated

# Generate the first 1000 prime numbers
first_1000_primes = first_n_primes(1000)

# Calculate the differences between each prime and the first prime
differences_with_first = [prime - first_1000_primes[0] for prime in first_1000_primes]

# Calculate the differences between consecutive primes
consecutive_differences = differences_between_consecutive_primes(first_1000_primes)

# Calculate the differences in increase between consecutive primes
increase_differences = differences_increase_between_primes(first_1000_primes)

# Find the top repeated numbers in a sample list
numbers = [1, 2, 3, 4, 5, 1, 2, 1, 2, 3, 4, 5, 5]
top_repeated = find_top_repeated_numbers(numbers, top_count=3)

# Print the results
print("Differences between each prime and the first prime:")
print(differences_with_first)
print("\nDifferences between consecutive primes:")
print(consecutive_differences)
print("\nDifferences in increase between consecutive prime numbers:")
print(increase_differences)
print("\nTop repeated numbers and their counts:")
for number, count in top_repeated:
    print(f"Number: {number}, Count: {count}")
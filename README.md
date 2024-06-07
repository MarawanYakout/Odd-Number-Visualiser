# Prime Numbers Analysis

This program performs several operations related to prime numbers and their differences. It includes functionality to:

1. Check if a number is a prime number.
2. Generate the first `n` prime numbers.
3. Calculate differences between consecutive prime numbers.
4. Calculate the difference in increase between consecutive prime numbers.
5. Find the most frequently repeated numbers in a list and their counts.

## Requirements

- Python 3.x
- `matplotlib`
- `numpy`

Install the required libraries using pip:

```sh
pip install matplotlib numpy
```

## Functions

### `is_prime(n)`

Checks if a number `n` is a prime number.

- **Parameters:** 
  - `n` (int): The number to check.
- **Returns:** 
  - `bool`: `True` if `n` is prime, `False` otherwise.

### `first_n_primes(n)`

Generates the first `n` prime numbers.

- **Parameters:** 
  - `n` (int): The number of prime numbers to generate.
- **Returns:** 
  - `list`: A list of the first `n` prime numbers.

### `differences_between_consecutive_primes(primes)`

Calculates the differences between consecutive prime numbers.

- **Parameters:** 
  - `primes` (list): A list of prime numbers.
- **Returns:** 
  - `list`: A list of differences between consecutive prime numbers.

### `differences_increase_between_primes(primes)`

Calculates the difference in increase between consecutive prime numbers.

- **Parameters:** 
  - `primes` (list): A list of prime numbers.
- **Returns:** 
  - `list`: A list of differences in increase between consecutive prime numbers.

### `find_top_repeated_numbers(numbers, top_count=1)`

Finds the top repeated numbers and their counts in a list.

- **Parameters:** 
  - `numbers` (list): A list of numbers.
  - `top_count` (int, optional): The number of top repeated numbers to find. Default is 1.
- **Returns:** 
  - `list`: A list of tuples containing the top repeated numbers and their counts.

## Example Usage

```python
# Importing necessary libraries
import matplotlib.pyplot as plt
import numpy as np

# put the number of prime numbers uou need !
first_100_primes = first_n_primes(100)

# Calculate the differences between each prime and the first prime
differences_with_first = [prime - first_100_primes[0] for prime in first_100_primes]

# Calculate the differences between consecutive primes
consecutive_differences = differences_between_consecutive_primes(first_100_primes)

# Calculate the differences in increase between consecutive primes
increase_differences = differences_increase_between_primes(first_100_primes)

# Find the top repeated numbers in a sample list , so just place the numbers you want to check how many times they were repeated
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
```

## Running the Program

1. Ensure all required libraries are installed.
2. Copy the provided example code into a Python file (e.g., `prime_analysis.py`).
3. Run the file using Python:

```sh
python prime_analysis.py
```

This will generate and print the analysis results of the first 100 prime numbers and the top repeated numbers in a sample list.


Enjoy ! Thanks !

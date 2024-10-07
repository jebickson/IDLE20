def is_prime(num):
    """Check if a number is prime."""
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def count_twin_primes(arr):
    """Count twin prime pairs in the array."""
    primes = []
    
    # Step 1: Find all primes in the array
    for number in arr:
        if is_prime(number):
            primes.append(number)
    
    # Step 2: Count twin prime pairs
    twin_prime_count = 0
    prime_set = set(primes)  # Use a set for quick lookups

    for prime in primes:
        if (prime + 2) in prime_set:
            twin_prime_count += 1
            
    return twin_prime_count

# Input reading
input_str = input().strip()
arr = list(map(int, input_str.split(',')))

# Count twin primes and print the result
result = count_twin_primes(arr)
print(result)
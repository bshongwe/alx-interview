#!/usr/bin/python3
"""Task 0. Prime Game module: Maria and Ben
"""


def isWinner(x, nums):
    """Determines the winner of a prime game session with `x` rounds.
    """
    if x < 1 or not nums:
        return None

    # Determine maximum value in nums to know range for prime calculation
    max_num = max(nums)

    # Generate prime numbers up to max_num using Sieve of Eratosthenes
    primes = [True] * (max_num + 1)
    primes[0] = primes[1] = False  # 0 and 1 are not prime numbers
    for i in range(2, int(max_num**0.5) + 1):
        if primes[i]:
            for j in range(i*i, max_num + 1, i):
                primes[j] = False

    marias_wins, bens_wins = 0, 0

    # Play x rounds of the game
    for n in nums:
        prime_count = sum(primes[2:n + 1])
        if prime_count % 2 == 1:
            marias_wins += 1
        else:
            bens_wins += 1

    if marias_wins > bens_wins:
        return "Maria"
    elif bens_wins > marias_wins:
        return "Ben"
    else:
        return None

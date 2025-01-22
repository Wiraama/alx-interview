#!/usr/bin/python3
""" game """


def isWinner(x, nums):
    """
    Determines the winner of the game for x rounds.

    Args:
        x (int): Number of rounds.
        nums (list): List of n values for each round.

    Returns:
        str: Name of the winner ("Maria" or "Ben"), or None if tied.
    """
    if x < 1 or not nums:
        return None

    # Determine the maximum value of n
    max_n = max(nums)

    # Sieve of Eratosthenes to precompute prime numbers up to max_n
    primes = [True] * (max_n + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(max_n**0.5) + 1):
        if primes[i]:
            for j in range(i * i, max_n + 1, i):
                primes[j] = False

    # Precompute the number of primes up to each number
    prime_count = [0] * (max_n + 1)
    for i in range(1, max_n + 1):
        prime_count[i] = prime_count[i - 1] + (1 if primes[i] else 0)

    # Determine the winner for each round
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if prime_count[n] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    # Determine overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

#!/usr/bin/python3
"""
Prime Game Module
"""


def isWinner(x, nums):
    """
    Determines the overall winner of the prime game.

    Args:
        x (int): The number of rounds.
        nums (list): A list of integers representing the rounds.

    Returns:
        str: The name of the winner ('Maria' or 'Ben') or None if it's a tie.
    """

    def sieve_of_eratosthenes(n):
        """
        Return a list of primes up to n using the Sieve of Eratosthenes
        algorithm.

        Args:
            n (int): The upper limit to find primes.

        Returns:
            list: A list of prime numbers up to n.
        """
        is_prime = [True] * (n + 1)
        p = 2
        while p * p <= n:
            if is_prime[p]:
                for i in range(p * p, n + 1, p):
                    is_prime[i] = False
            p += 1
        return [p for p in range(2, n + 1) if is_prime[p]]

    def determine_winner(n):
        """
        Determine the winner of the game given n.

        Args:
            n (int): The upper limit to find primes.

        Returns:
            str: The name of the winner ('Maria' or 'Ben').
        """
        if n < 2:
            return "Ben"
        primes = sieve_of_eratosthenes(n)
        # Game strategy based on number of primes
        return "Maria" if len(primes) % 2 == 1 else "Ben"

    win_count = {"Maria": 0, "Ben": 0}
    for num in nums:
        winner = determine_winner(num)
        win_count[winner] += 1

    if win_count["Maria"] > win_count["Ben"]:
        return "Maria"
    elif win_count["Ben"] > win_count["Maria"]:
        return "Ben"
    else:
        return None

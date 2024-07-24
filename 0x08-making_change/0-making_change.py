#!/usr/bin/python3
"""
This module provides a function to determine the fewest number of coins
needed to meet a given amount total. This is a classic problem of dynamic
programming.

The function `makeChange` takes a list of coin values and a total amount,
and returns the minimum number of coins needed to make up that amount. If
it's not possible to make that total with the given coins, the function
returns -1.
"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given amount total.

    :param coins: List of the values of the coins in possession.
    :param total: The total amount to be achieved.
    :return: The fewest number of coins needed to meet total, or -1 if it
    cannot be met.
    """
    if total <= 0:
        return 0

    # Initialize DP array with a large value (infinity)
    dp = [float("inf")] * (total + 1)
    dp[0] = 0  # Base case: 0 coins needed to make 0 amount

    # Fill the DP array
    for i in range(1, total + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    # If dp[total] is still infinity, it means we cannot make the total with
    # the given coins
    return dp[total] if dp[total] != float("inf") else -1

#!/usr/bin/python3
"""Module Making Change.
"""


def makeChange(coins, total):
    """Calculates the fewest number of coins needed to meet a given total.
        tofewest number of coins needed to meet the total.
    """
    # If the total is zero or less, we don't need any coins
    if total <= 0:
        return 0
    # Sort the coins in decreasing order
    coins.sort(reverse=True)
    # Initialize count to zero
    coin_count = 0
    # Iterate through n the list of coins
    for coin in coins:
        # If the coin is greater remaining total, skip it
        if coin > total:
            continue
        # Calculate the number current coin can be used
        count = total // coin
        # Update the total the value of the coins used
        total -= count * coin
        # Update the coin the number of coins used
        coin_count += count
        # If the total zero, we're done
        if total == 0:
            break
    # If we couldn't the total, return -1
    if total > 0:
        return -1
    # Otherwise,t
    return coin_count

#!/usr/bin/python3
""" This module contains a function makeChange """


def makeChange(coins, total):
    """ Calculate minimum number of coins needed to
    get a given amount """
    if total <= 0:
        return 0
    dp = [total + 1] * (total + 1)
    dp[0] = 0

    for a in range(1, total + 1):
        for c in coins:
            if a - c >= 0:
                dp[a] = min(dp[a], 1 + dp[a - c])
    if dp[total] != total + 1:
        return dp[total]
    else:
        return -1

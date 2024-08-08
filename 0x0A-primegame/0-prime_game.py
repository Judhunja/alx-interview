#!/usr/bin/python3
""" This module contains functions sieveoferatosthenes and isWinner """


def sieveoferatosthenes(n):
    """ Find the prime numbers in range n """
    prime = [True for i in range(n + 1)]
    p = 2
    while (p * p <= n):
        if (prime[p] is True):
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    primenums = [p for p in range(2, n + 1) if prime[p]]
    return primenums


def isWinner(x, nums):
    """ Determine winner of each game of choosing a prime number from the set
        and removing the prime number and its multiples from the set """
    if x == 0:
        return None

    n = max(nums)

    primenums = sieveoferatosthenes(n)

    ben = 0
    maria = 0

    not_taken = [True for i in range(n + 1)]
    turn = 0

    for prime in primenums:
        if prime > n:
            break
        if not not_taken[prime]:
            for multiple in range(prime, n + 1, prime):
                not_taken[multiple] = False
            turn = 1 - turn

    # if the turn changes means Maria found a prime in the previous round
    if turn == 1:
        maria += 1
    else:
        ben += 1

    if maria > ben:
        return "Maria"
    elif ben > maria:
        return "Ben"
    else:
        return None

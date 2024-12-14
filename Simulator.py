from random import random

def repeatAndCount(n, function, args = None):
    counter = {}
    for i in range(1, n + 1):
        if args is not None:
            res = function(*args)
        else:
            res = function()
        counter[res] = counter.get(res, 0) + 1
    return counter

def SimulateN(n):
    if n == 0:
        return True
    outcome = determineOutcome()
    total = outcome
    while outcome != -1 and total < n:
        outcome = determineOutcome()
        total = total + outcome
    if total < n:
        return False
    else:
        return True

def determineOutcome():
    number = random()
    if number < 0.35:
        return -1 #fail
    elif number < 0.675:
        return 1
    else:
        return 2





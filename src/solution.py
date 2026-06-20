from functools import reduce
from math import gcd


def solution(signals):
    def lcm(a, b):
        return a * b // gcd(a, b)

    def get_lcm_list(numbers):
        return reduce(lcm, numbers)

    periods = [G + Y + R for G, Y, R in signals]
    max_time = get_lcm_list(periods)

    for t in range(1, max_time + 1):
        all_yellow = True
        for G, Y, R in signals:
            period = G + Y + R
            pos = (t - 1) % period
            if not (G <= pos < G + Y):
                all_yellow = False
                break
        if all_yellow:
            return t

    return -1

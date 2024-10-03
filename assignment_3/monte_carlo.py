import random

def in_circle(r, x, y):
    distance_from_center = (x * x + y * y) ** 0.5
    return distance_from_center <= r

def random_throw(r):
    x = random.uniform(a=r,b=-r)
    y = random.uniform(a=-r,b=r)
    return x, y

def monte_carlo_pi(n):
    """
    For simplicity purposes, r is set to 1.
    This is a simulation of random dart throws in a square with a circle inside
    The probability, multiplied by 4 will equate approximately to 3.14 (Pi)
    :param n: number of dart throws
    :return: the Probability in float
    """
    r = 1
    n_circle = 0
    for i in range(n):
        x, y = random_throw(r)
        if in_circle(r, x, y):
            n_circle += 1
    p = n_circle/n * 4.0
    return p

print(monte_carlo_pi(10))
print(monte_carlo_pi(100))
print(monte_carlo_pi(1000))
print(monte_carlo_pi(10000))
print(monte_carlo_pi(100000))
print(monte_carlo_pi(1000000))
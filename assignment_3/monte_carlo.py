import random

def random_around_zero(r):
    square_width = 2 * r
    return random.random() * square_width - r

def in_circle(r, x, y):
    distance_from_center = (x * x + y * y) ** 0.5
    return distance_from_center <= r

def number_generator():
    x = random.uniform(a=1,b=-1)
    y = random.uniform(a=-1,b=1)
    return x,y

def monte_carlo_pi(n):
    n_circle=0
    for i in range(n):
        x,y = number_generator()
        if in_circle(1,x,y):
            n_circle += 1

    p =  n_circle/n * 4.0
    return p

print(monte_carlo_pi(10))
print(monte_carlo_pi(100))
print(monte_carlo_pi(1000))
print(monte_carlo_pi(10000))
print(monte_carlo_pi(100000))
print(monte_carlo_pi(1000000))
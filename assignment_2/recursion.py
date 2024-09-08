def factorialR(n):
    if n == 1:
        return 1
    else:
        print(n)
        return n * factorialR(n-1)

if __name__ == "__main__":
    value = factorialR(400)
    print(value)
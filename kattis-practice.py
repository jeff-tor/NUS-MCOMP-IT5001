def count_chars(input):
    counter = 0
    for i in input:
        if i == 'u':
            counter += 1
    return counter

print(count_chars('uuuuuuuuuuuuuu'))
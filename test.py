def recursive(num):
    if len(str(num)) == 1:
        return num
    if (str(num))[0] != '0':
        return recursive(int(str(num)[0])) * recursive(int(str(num)[1:]))


print(recursive(2**200-1))
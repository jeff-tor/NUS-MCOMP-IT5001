def filter_wave(wave,times):
    # for i in range(len(wave)):
    #     wave[i]*=1000
    new_wave = wave.copy()
    for i in wave:
        if wave.index(i) == 0:
            new_wave[i] = int(0 + wave[i] * 0.6 + wave[i+1] * 0.2)

        elif wave.index(i) == len(wave):
            new_wave[i] = int(wave[i-1] * 0.2 + wave[i] * 0.6 + 0)
        else:

            new_wave[i] = int(wave[i-1] * 0.2 + wave[i] * 0.6 + wave[i+1] * 0.2)

    # for i in range(len(new_wave)):
    #     new_wave[i]*=1000
    print(new_wave)
    return new_wave


resistor_list = (75,80,90,77,88,91,60,74,73,70,55,93,59),150,[(59, 91), (60, 90), (70, 80), (73, 77)]
resistor_list_2 = (23,75,80,90,77,88,91,60,1,74,73,4,70,55,7,9,93,59,12,43),170,[(77, 93), (80, 90)]

def flatten(xs):
    for x in xs:
        try:
            yield from flatten(x)
        except:
            yield x

res = list(flatten(resistor_list_2))

print(sorted(res))

def matchResistors(R, n):

    hash_table = {}
    matches_pairs = []
    for number in hash_table:
        complement = n - number
    if complement in hash_table:
        matches_pairs.append((number, hash_table[seen[complement]]))
    else:
        hash_table[number] = hash_table.index(number)

    return matches_pairs

x = matchResistors(resistor_list_2, 90)
print(x)
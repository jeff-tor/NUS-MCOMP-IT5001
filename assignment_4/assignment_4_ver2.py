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
resistor_list_2 = (23,59,7,75,80,90,77,88,91,60,1,74,73,4,70,55,7,9,93,59,12,43),170,[(77, 93), (80, 90), (59, 7)]

def flatten(xs):
    for x in xs:
        try:
            yield from flatten(x)
        except:
            yield x
def matchResistors(R, n):
    flatten_list = sorted(flatten(R))
    d = {}
    matched_pairs = []
    for index, number in enumerate(flatten_list):
        complement = int(n - number)
        if complement in d.values():
            id = list(d.values()).index(complement)
            if d.get(id) == None:
                matched_pairs.append((number, d.get((id+1))))
                d.pop(id+1)
            else:
                matched_pairs.append((number, d.get(id)))
                d.pop(id)
        else:
            d[index] = number
    return matched_pairs


def matchResistors_v2(R, n):
    flatten_list = sorted(flatten(R))
    d = []
    matched_pairs = []
    for number in flatten_list:
        complement = int(n - number)
        if complement in d:
            matched_pairs.append((number, d[d.index(complement)]))
            del d[d.index(complement)]
        else:
            d.append(number)
    return matched_pairs

print(matchResistors(resistor_list_2, 66))

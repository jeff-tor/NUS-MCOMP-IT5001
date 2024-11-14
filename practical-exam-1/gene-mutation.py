def final_pos_r(x,y,seq):
    if seq == '':
        return (x,y)
    first_char = seq[0]
    if first_char == 'N':
        y += 1
    if first_char == 'E':
        x += 1
    if first_char == 'S':
        y -= 1
    if first_char == 'W':
        x -= 1
    return final_pos_r(x,y,seq[1:])

def final_pos_o(x,y,seq):
    return (x + seq.count('E')
            - seq.count('W'),
            y + seq.count('N')
            - seq.count('S'))

def burger_upgrade(b1,b2):
    pointer_2 = 0
    for pointer_1 in len(range(b1)):
        if b1[pointer_1] == b2[pointer_2]:
            pointer_2 += 1
    return pointer_2 == len(b2)

### b1 : B P C L B
#        ^ <- this is pointer 1

### b2 : B C P B
#        ^ <- this pointer moves if it matches b1


print(final_pos_r(2,4,'WNWNE'))
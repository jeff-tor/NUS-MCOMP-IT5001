seq1 = [('CW',40),('CW',100),('CCW',10),('CW',30),('CCW',20),('CW',180)]

def dial_i(start,seq1):
    res = 0
    for i in seq1:
        if i[0][0] == 'CW':
            res += i[0][1]
        else:
            res -= i[0][1]

    return res

def dial_r(start, seq):
    if seq == []:
        return start
    return (+(seq[0][1]) if seq[0][0] == 'CW' else -(seq[0][1])) + dial_r(start,seq[1:])

def dial_u(start,seq):
    return [+(seq[x][1]) if seq[x][0] == 'CW' else -(seq[x][1]) for x in seq]
print(dial_r(70,seq1))




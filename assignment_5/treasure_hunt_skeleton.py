from importlib.metadata import files

d1 = {'D': 'W', '1': 'W', 'Z': 'W', 'C': 'T', '3': 'T', 'F': 'T', '0': '.', '2': '.', '4': '.', 'B': '^', '+': '^', ';': '^', 'Q': 'E', '7': 'E', '8': 'E', 'X': 'M', 'P': 'M', '!': 'M', '(': ':', ')': ':', '9': ':', '*': ' ', '|': ' ', '#': ' '}
d2 = {'C': 'W', '3': 'W', 'F': 'W', '0': 'T', '2': 'T', '4': 'T', 'B': '.', '+': '.', ';': '.', 'Q': '^', '7': '^', '8': '^', 'D': 'E', '1': 'E', 'Z': 'E', '(': 'M', ')': 'M', '9': 'M', '*': ':', '|': ':', '#': ':', 'X': ' ', 'P': ' ', '!': ' '}
        
# def decode_map(mapfile,ddict,outfile):
#     w = open(outfile, 'w')
#     res = ''
#     f = open(mapfile, 'r')
#     for line in f:
#         data = line.rstrip('\n')
#         for i in data:
#             if ddict.get(i) == None:
#                 res += i
#             else:
#                 res += ddict.get(i)
#         w.write(f'{res}'+'\n')
#         res = ''
#     w.close()
#     f.close()

def find_treasure(mapfile):
    print('finding treasure')
    coordinate_list = []
    f = open(mapfile, 'r')
    for i, row in enumerate(f):
        for j, val in enumerate(row):
            if val == 'T':
                coordinate_list.append((i,j))
    print(coordinate_list)

    for i in coordinate_list:
        print(i[0],i[1])


print("Map 1")
# decode_map('encoded_map.txt',d1,'decoded_map.txt')
print(find_treasure('decoded_map.txt'))

# Uncomment the following for your test cases
'''
print("Map 2")
decode_map('encoded_map2.txt',d1,'decoded_map2.txt')
print(find_treasure('decoded_map2.txt'))

print("Map 3")
decode_map('encoded_map3.txt',d1,'decoded_map3.txt')
print(find_treasure('decoded_map3.txt'))

print("Map 5")
decode_map('encoded_map5.txt',d1,'decoded_map5.txt')
print(find_treasure('decoded_map5.txt'))

print("Map 1 B")
decode_map('encoded_mapB.txt',d2,'decoded_mapB.txt')
print(find_treasure('decoded_mapB.txt'))
'''

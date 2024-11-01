
def createZeroMatrix(n,m):
    return [[0 for i in range(m)] for j in range(n)]

def mTightPrint(m):
    for i in range(len(m)):
        line = ''
        for j in range(len(m[0])):
            line += str(m[i][j])
        print(line)
        
def PDMap(r,c,sites):
    town = createZeroMatrix(r,c)
    for i in range(0,r):
        for j in range (0,c):
            elem = town[i][j]
            print(elem)

    def near_one(x,y, sites):
        res = []
        for n in range(len(sites)):
            res.append(int((((x-sites[n][0])**2 + (y-sites[n][1])**2))**0.5))
        result = res.index(min(res))
        print((i,j))
        print(res)
        print(min(res))
        print(result)
        return result
    map2 = []
    for i in range(0,r):
        row = []
        for j in range(0,c):
            row.append(near_one(i,j,sites))
        map2.append(row)
    return map2

# ((ax2 – x1)^2 + (y2 – y1)^2) ** 0.5 - formula for euc distance
#take minimum of all 3 stores lambda x; y2-y2 / x2-x1
#mTightPrint(PDMap(50,80,[[20,10], [30,30],[40,20],[45,55],[10,55],[35,70],[35,60]]))
# mTightPrint(PDMap(10,10,[[2,3],[4,9],[7,2]]))
#
# mTightPrint(PDMap(60,70,[[10,20],[30,20],[40,50]]))
print(PDMap(7,8,[[1,3],[4,7],[7,2]]))

# print(mTightPrint(PDMap(50,80,[[20,10], [30,30],[40,20],[45,55],[10,55],[35,70],[35,60]])))

# print(createZeroMatrix(7,8))
# print(PDMap(7,8,[[1,2],[5,7],[3,5]]))
import time

'''
n = number of elements
k = number of elements in combination
'''
def nChooseK_recursive(n,k):
    if k > n:
        return 0
    if k == 0 or k == n:
        return 1
    else:
        return nChooseK_recursive(n-1,k-1) + nChooseK_recursive(n-1,k)

def nChooseK(n, k):

    list_construct = [[0 for x in range(k+1)] for x in range(n+1)]
    print(list_construct)

    # Calculate value of Binomial
    # Coefficient in bottom up manner
    for i in range(n+1):
        for j in range(min(i, k)+1):
            print(f'range {range(min(i, k)+1)}')
            print(f'j == {j}, i == {i}')
            # Base Cases
            if j == 0 or j == i:
                print(f'met')
                list_construct[i][j] = 1
                print(f'list_construct -- {list_construct}')
            # Calculate value using
            # previously stored values
            else:
                list_construct[i][j] = list_construct[i-1][j-1] + list_construct[i-1][j]
    print(f'list_construct[n][k] -- {list_construct[n][k]} {n} {k} ')
    return list_construct[n][k]


if __name__ == "__main__":
    print(nChooseK(33,20))
    print(f'time taken -- {time.process_time()}')
    print(nChooseK_recursive(33,20))
    print(f'time taken -- {time.process_time()}')

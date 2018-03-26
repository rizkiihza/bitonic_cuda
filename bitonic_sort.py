
def powerOfTwoGreaterThanX(n):
    idx = 1
    while idx < n:
        idx *= 2
    return idx

def compare(asc, x):
    mid = len(x) // 2
    for i in range(mid):
        if (x[i] > x[i+mid]) == asc:
            x[i], x[i+mid] = x[i+mid], x[i]


def bitonic_merge(asc, x):
    if len(x) == 1:
        return x
    else:
        compare(asc, x)
        first = bitonic_merge(asc, x[:len(x)//2])
        second = bitonic_merge(asc, x[len(x)//2:])
        return first + second

def bitonic_sort(asc, x):
    if len(x) <= 1:
        return x
    else:
        first = bitonic_sort(asc, x[:len(x)//2]);
        second = bitonic_sort(not asc, x[len(x)//2:]);
        return bitonic_merge(asc, first+second)

def sort(x):
    #tambah unit sisa
    panjang = len(x)
    sisa = powerOfTwoGreaterThanX(len(x)) - len(x)
    maxUnit = max(x)
    for i in range(sisa):
        x.append(maxUnit+1)
    result = bitonic_sort(True, x)
    return result[:panjang]
    
print(sort([0, 92,13,54,66,21,1,2,40]))






if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arr_unique = list(set(arr))
    arr_unique.sort()

    result = []
    for i in range(len(arr_unique)):
        t = (arr_unique[i],arr.count(arr_unique[i]))
        result.append(t)
    
    result.sort(key=lambda x: x[1], reverse=True)
    result = result[0][0]

    print(result)


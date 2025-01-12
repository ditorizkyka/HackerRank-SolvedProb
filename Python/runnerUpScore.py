if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr_list = list(arr)
    arr_sorted = sorted(arr_list)
    arr_unique =list( set(arr_sorted))
    print(arr_unique[-2])
def average(array):
    array_unique = set(array)        # ambil elemen unik
    res = sum(array_unique)          # jumlahkan semua elemen unik
    return res / len(array_unique)   # bagi dengan banyaknya elemen

            
                
        

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)

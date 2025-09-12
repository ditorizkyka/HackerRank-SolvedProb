if __name__ == '__main__':
    N = int(input())
    lst = []
    for i in range(N):
        data = input().split()

        if len(data) == 3:
            method, i, e = data
            i, e = int(i), int(e)
            if method == 'insert':
                lst.insert(i, e)

        elif len(data) == 2:
            method, e = data
            e = int(e)
            if method == 'remove':
                lst.remove(e)
            elif method == 'append':
                lst.append(e)

        elif len(data) == 1:
            method = data[0]
            if method == 'print':
                print(lst)
            elif method == 'sort':
                lst.sort()
            elif method == 'pop':
                lst.pop()
            elif method == 'reverse':
                lst.reverse()
        else:
            print("Format input tidak sesuai")
            exit()

    
        



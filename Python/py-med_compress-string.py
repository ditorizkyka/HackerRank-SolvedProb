
if __name__ == '__main__':
    num = int(input())
    array = []
    lst = [int(d) for d in str(num)]
    for i in range(len(lst)):
        p = 1
        for j in range(len(lst)):
            if lst[j+1] == lst[i]:
                p = p+1
            else:
                t = (lst[i],p)
                i= j
                array.append(t)
                break
            j = j+1
            print(lst[i], lst[j+1])
    # print(lst) 
    # t = (1,)
    # t =(1,3)
    # array.append(t)
    print(array)
    
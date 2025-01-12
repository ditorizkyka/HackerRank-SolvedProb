if __name__ == '__main__':
    arr_list = []
    arr_score = []
    arr_name = []
    for _ in range(int(input())):
        arr_data = []
        name = input()
        score = float(input())
        arr_data.append(name)
        arr_data.append(score)
        arr_list.append(arr_data)
        arr_score.append(score)

    arr_unique = list(set(arr_score))
    arr_unique.sort()
    arr_unique = arr_unique[1]
    print(arr_score)
    for i in range(len(arr_list)):
        if arr_list[i][1] == arr_unique:
            arr_name.append(arr_list[i][0])
    arr_name.sort()

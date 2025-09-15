def symetric_diff(set1, set2):
    return set1.symmetric_difference(set2)

if __name__ == '__main__':
    m = int(input())
    set1 = set(map(int, input().split()))
    n = int(input())
    set2 = set(map(int, input().split()))
    result = symetric_diff(set1, set2)
    for i in sorted(result):
        print(i)
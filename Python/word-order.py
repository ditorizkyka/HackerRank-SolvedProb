from collections import Counter

if __name__ == '__main__':
    n = int(input())
    word = [input() for _ in range(n)]

    freq = Counter(word)             # hitung jumlah kemunculan tiap kata
    distict_word = list(freq.keys()) # ambil kata unik
    
    print(len(distict_word))         # jumlah kata unik
    print(*freq.values())  
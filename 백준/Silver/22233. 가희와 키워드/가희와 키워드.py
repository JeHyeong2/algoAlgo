import sys
input = sys.stdin.readline

N, M = map(int,input().split())
key_word = {}
key_word_num = 0
writen = [0]*N


for i in range(N):
    key = input().strip()

    if key not in key_word:
        key_word[key] = 1
    key_word_num += 1

for i in range(M):
    key = input().strip()
    key = key.split(",")
    for j in key:
        if j in key_word:
            if key_word[j]:
                key_word[j] = 0
                key_word_num -= 1

    print(key_word_num)

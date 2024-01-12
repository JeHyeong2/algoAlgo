word_list = []
for i in range(5):
    word = list(input())
    word_list.append(word)
maxx = 0
for i in word_list:
    if len(i) > maxx:
        maxx = len(i)
ans = []

for i in range(maxx):
    for j in range(5):
        if len(word_list[j]) < i+1:
            continue
        else:
            ans.append(word_list[j][i])


answer = "".join(ans)
print(answer)

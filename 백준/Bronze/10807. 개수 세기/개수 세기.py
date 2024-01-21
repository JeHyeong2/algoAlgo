n = int(input())

list_ = map(int,input().split())
v = int(input())
count = 0 
for i in list_:
    if i == v:
        count+=1
print(count)
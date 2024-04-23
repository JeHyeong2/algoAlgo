s1,s2,c,d = map(int,input().split())


print(min(min(s1,c-s1),min(s2,d-s2)))
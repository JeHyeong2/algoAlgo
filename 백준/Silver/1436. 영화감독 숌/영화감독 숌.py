N = int(input())

count = 0
NB = 0
endgame =0
while count != N:
    acount = 0
    a = str(NB)
    for j in a:
        if j == "6":
            acount+=1
        else:
            acount = 0
        if acount == 3:
            count += 1
    if count == N:
        print(NB)
    NB+=1

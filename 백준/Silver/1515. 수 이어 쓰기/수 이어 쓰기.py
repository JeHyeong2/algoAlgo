def check():
    num = 1
    pointer = 0
    while True:
        compare = str(num)
        for i in compare:
            if i == N[pointer]:
                pointer +=1
            if pointer == len(N):
                return num
        num +=1
N = input()



print(check())

stop = True

while stop:
    word = input()
    if word == 'end':
        break
    aeiou = False
    itriple_checker = 0
    triple_checker = 0
    aeiou_check = ['a','e','i','o','u']
    for i in range(len(word)):
        if word[i] in aeiou_check:
            aeiou = True
            itriple_checker +=1
            triple_checker = 0
        else:
            itriple_checker = 0
            triple_checker +=1

        if itriple_checker ==3 or triple_checker == 3:
            print(f'<{word}> is not acceptable.')
            break

        if i >= 1:
            if word[i] == 'e' and word[i-1] == 'e' or word[i] == 'o' and word[i-1] == 'o':
                continue
            else:
                if word[i] == word[i-1]:
                    print(f'<{word}> is not acceptable.')
                    break
    else:
        if aeiou:
            print(f'<{word}> is acceptable.')
        else:
            print(f'<{word}> is not acceptable.')









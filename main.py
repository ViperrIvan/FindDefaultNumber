numberList = map(int, input().split())
scoreSost = 0
scoreDef = 0
for number in numberList:
    score = 0
    for i in range(2, number//2):
        if number%i==0:
            score+=1
    if score==0:
        print(f'Число {number} простое')
        scoreDef+=1
    else:
        print(f'Число {number} составное')
        scoreSost += 1
print(f'Количество составных чисел: {scoreSost}')
print(f'Количество простых чисел: {scoreDef}')

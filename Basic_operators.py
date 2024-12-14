import random
def numbers_on_the_wall():
    random_numbers = [3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    numbers = random.choice(random_numbers)
    return numbers
one = numbers_on_the_wall()
result = []
for i in range(1, one):
    for j in range(1 , one):
        if i>=j:
            continue
        if one % (i+j) ==0:
           result.append([i,j])
        else:
            continue
dict = {3:12, 4:13, 5:1423, 6:121524, 7:162534, 8:13172635, 9:1218273645, 10:141923283746,
    11:11029384756, 12:12131511124210394857, 13:112211310495867, 14:1611325212343114105968,
    15:1214114232133124115106978, 16:1317115262143531341251161079, 17:11621531441351261171089,
    18:12151811724272163631545414513612711810, 19:118217316415514613712811910,
     20:13141911923282183731746416515614713812911}
print("выпало число - ", one)
result = sum(result,[])
result = int(str(result)[1:-1].replace(", ", ""))
print("код для этого числа - ", result)
if dict[one] == result:
    print('!!!!!!!!!!!!!ПАРОЛЬ ПОДОШЁЛ!!!!!!!!!!!!')
else:
    print('!!!!!!!!!!!!!ПАРОЛЬ ВВЕДЕН НЕ ПРАВИЛЬНО!!!!!!!!!!!!!!')
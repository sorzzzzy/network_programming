# 플레이어가 처음에 $50을 가지고 있다. 
# 동전을 한 번 던져서 앞면(1) 또는 뒷면(2)이 나온다. 
# 맞추면 $9을 따고 틀리면 $10을 잃는다. 
# 플레이어가 돈을 모두 잃거나 $100이 되면 게임이 종료된다.

from random import randint

user_money = 50

while True:
    coin = randint(1,2)
    res = int(input("앞면은 1, 뒷면은 2를 입력하세요"))
    print(res)
    if coin == res :
        user_money += 9
        print(user_money)
    else :
        user_money -= 10
        print(user_money)
    
    if user_money < 0 :
        print("돈을 모두 잃었습니다")
        break
    if user_money > 100 :
        print("100달러를 모두 획득했습니다")
        break

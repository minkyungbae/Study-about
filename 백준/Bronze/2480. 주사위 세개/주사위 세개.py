dice1, dice2, dice3 = map(int,input().split())

if dice1==dice2==dice3:
    print(10000 +dice1 *1000)
elif dice1==dice2 or dice1 == dice3 or dice2 == dice3:
    same_number = dice1 if dice1 == dice2 or dice1 == dice3 else dice2
    prize = 1000 + same_number * 100
    print(prize)

else:
    print(max(dice1, dice2, dice3)*100)
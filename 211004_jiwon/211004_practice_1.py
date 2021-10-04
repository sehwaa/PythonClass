from random import randrange

def lotto(num):
    #당첨 번호 3개
    winning = []
    for _ in range(1, 4): #n회 반복하기 위한 변수는 언더바로 대체가능
        winning.append(randrange(1, 4))
    print(winning)

    count = 0
    for idx in range(0, len(winning)):
        if num[idx] == winning[idx]:
            count += 1

    if count == 3:
        print("1등 당첨!")
    elif count == 2:
        print("2등 당첨!")
    elif count == 1:
        print("3등 당첨!")
    else:
        print("다음 기회에!")

    #사용자 입력 번호 3개
num = []
for _ in range(0, 3):
    num.append(randrange(1,4))
print(num)

lotto(num)
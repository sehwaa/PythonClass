from random import randrange

def lotto(num:list):
    # 당첨 번호 3개
    winning = []
    for _ in range(1, 4):
        winning.append(randrange(1, 4))

    count = 0
    for idx in range(0, len(winning)):
        if num[idx] == winning[idx]:
            count += 1

    if count == 3:
        print("first prize")
    elif count == 2:
        print("second prize")
    elif count == 1:
        print("third prize")
    else:
        print("다음 기회에!")

#사용자 입력 번호
num = []
for _ in range(0, 3):
    num.append(randrange(1,4))
print(num)

lotto(num)

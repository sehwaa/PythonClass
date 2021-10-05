#6) - 다음 문자열에서 대문자인 것만 출력하시오. (hint: isupper() 사용)
# "Beyond The Scene"

s = "Beyond The Scene"

for i in s:
    if i.isupper():
        print(i)
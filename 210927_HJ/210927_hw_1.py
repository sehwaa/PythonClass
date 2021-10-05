#1) ["NICE", "TO", "MEET", "YOU"] 리스트의 각 요소들을 모두 소문자로 바꿔서 출력하시오.

s = ["NICE", "TO", "MEET", "YOU"] #첫번째방법
s_join = ' '.join(s)
s_split = s_join.lower().split()
print(s_split)

s = ["NICE", "TO", "MEET", "YOU"] #두번째방법
s_lower = []
for i in s:
   s_lower.append(i.lower())

s = ["NICE", "TO", "MEET", "YOU"] #세번째방법
s_lower = [i.lower() for i in s]
print(s_lower)


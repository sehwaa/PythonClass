#5) 다음 리스트에서 길이가 4이상인 문자열만 출력하시오.
# ["python", "java", "c++", "language"]

s = ["python", "java", "c++", "language"]
a = [i for i in s if len(i) >=4]
print(a)

# st=input("영어 1글자를 입력하세요")
# if st.isupper():     #대문자-> true 아니면 -> fals  # ture일때 수행 -> 소문자로 변경
#     print(st.lower())
# else:
#     print(st.upper())

score = int(input("점수를 입력하세요 :"))
if 81 <= score <= 100:
        grade = 'A'
elif 61 <= score <= 80:
        grade = 'B'
elif 41 <= score <= 60:
        grade = 'C'
elif 21 <= score <= 40:
        grade = 'D'
elif 0 <= score <= 20:
        grade = 'E'
else:
        grade = "범위 외 점수"
print("당신의 학점은", grade, "입니다.")
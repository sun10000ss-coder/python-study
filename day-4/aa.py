# 주민번호를 입력
# 1, 3 -> 남자 아니면 여자
jumin=input("주민번호 입력하세요") #080331 3153528
num= jumin.split("-")[1]
#080331
#3153528
if num[0] =='1' or num[0] =='3': 
#(jumin[7]=='1' or jumin[7]=='3'):
    print("남자")
else:
    print("여자")

    # 사용자로부터 세 개의 숫자를 입력 받은 후
    # 가장 큰 숫자를 출력하라
num1=int(input("숫자1을 입력하세요"))
num2=int(input("숫자2을 입력하세요"))
num3=int(input("숫자3을 입력하세요"))
if num1 >= num2 and num1>num3 :
    print("큰수는:",num1)
elif num2 >= num1 and num2>=num3 :
    print("큰수는:",num2)
else:
    print("큰수는:",num3)
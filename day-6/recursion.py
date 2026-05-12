# 재귀 호출(함수)(함수 내부에서 자기자신을 호출)
# 5!(팩토리얼): 1*2*3*4*5
def fact(n): #fact: 함수명(매개변수는 1개)
    if n == 1:
        return 1
    else:
        return n * fact(n-1) # 5*fact(4)= 5*24 =120
                             # 4*fact(3)= 3*6 =24
                             # 3*fact(2)= 3*2 =6
                             # 2*fact(1)= 2*1

a=int(input("정수를 입력하세요")) #예) 5 입력
res = fact(a) #함수 호출, 인수 a(정수) 보냄
# 반환되어서 온 결과값을 res 저장
print(a,"!는",res,"이다")

# 순환(재귀)함수를 활용하여 1부터 입력받은
# 숫자끼리 합을 구하는 프로그램을 작성하시오.
# 입력받은 수가 5
# 출력 1~5(입력받은 숫자)까지의 합
def abcd(a):
    if a == 1:
        return 1
    else:
        return b + a(a-1)
b=int(input("정수를 입력하세요"))
res=a(b)
print(b,"!는",res,"이다")
# 상품 이름과 가격, 수량을 입력받아 총 가격을 출력하세여
# 상품 이름: 사과
# 가격: 1000
# 수량: 3
# 출력결과: 사과의 총 가격은 3000원 입니다.
a=input("상품 이름:")
b=int(input("가격:"))
c=int(input("수량:"))
total = b * c
print(a,"의 총 금액은",total,"원입니다")
print(a+"의 총 금액은"+str(total)+"원입니다")
print(f"{a} 의 총금액은 {total}원 입니다")
# print 안에서 f는 f-string이라하며 포맷 문자열 
# ==> {변수 값}
# 숫자 -> 문자로 변환 :str
# 실수는 float만 있음(8바이트)
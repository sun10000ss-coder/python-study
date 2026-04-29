a_price = 2000
b_price = 3000
c_price = 3500
a=int(input("아메리카노 판매 개수:"))
b=int(input("카페라떼 판매 개수:"))
c=int(input("카푸치노 판매 개수:"))
sales = a*b
sales = sales + b* b_price
sales = sales + c* c_price
print("총 매출은", sales, "입니다")
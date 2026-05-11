num1 = int(input("3의 배수 입력:"))
num2 = int(input("5의 배수 입력:"))
match num1%2,num2%2 :
    case 0,0:
        print("num1은 3의 배수 num2는 5의 배수")
    case 0,_:
        print("num1은 3의 배수 num2는 아무숫자")
    case _,1:
        print("num2는 5의 배수 num1은 아무숫자")
    case _:
        print("둘다 오류")

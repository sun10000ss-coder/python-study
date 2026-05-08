# 문자열
s="Hello python"
print(s[6]) # 인덱싱
print(s[6:12]) # 슬라이싱

jumin="080331-3153528"
print("성별:"+jumin[7])
print("월:"+jumin[2:4])#2~3
print("일:"+jumin[4:6])#4~5
print("뒷자리:"+jumin[7:]) #7~끝

s1="나는 학생입니다"
s2="파이썬을 배웁니다"
s3="재미있습니다"
s4="""  
    나는 학생입니다
    파이썬을 배웁니다
    재미있습니다
"""
print(s4)

year="1985"
month="3"
day="15"
date=year+"-"+month+"-"+day
print(date)

date2= date.split('-')
print(date2)
print(type(date2))
print(date[1][0:2], end="*") 

name="kakao taxi"
name2=name.replace("k","t",1)
print()
print(name2)

print("python"*5) # 반복
# 문자열에서 컴마 제거
won="63,120,450"
won2=won.replace(",","")
print(won2)

won3=345608000
won4=format(won3, ",d")
print(won4)

p="Pyton is Amazing"
print(p.lower()) #소문자
print(p.upper()) #대문자
print(p.capitalize())#첫글자 대문자
print(p[0].isupper())#true
print(len(p))
print(p.count("i"))

#위치
index=p.index("i") #7
print(index)
index=p.index("i", index+1) #14
print(index)

#문자열 연결 
words = ["python","is","easy"]
result="".join(words) 
print(result)


num = "5"
result = num.zfill(3)
print(result)

#format
age=19
print("나는 %d살입니다" %age)
print("나는 {}살입니다".format(age))

like="노래부르기"
print("나는 %d살이고 %s를 좋아해요" %(age, like))
print("나는 {0}살이고 {1}를 좋아해요".format(age,like))

print("나의 주소는 {addr}이며, 나의 키는 {height}cm 입니다".format(addr="인천", height=150))

print("\n배우는 과목은\n \"파이썬\" 입니다")

print("red apple\rplne")
print("i like you!\b!!")
print("red\t apple")

p.="Python is Amazing"
print(p.find("A"))
print(p.rfind("A"))
print(p.index("a"))
print(p.rindex("a"))

print(p.find("java"))

arr_Str=input('input String :').split('-')
arr_Len==int(input('input Number :'))
arr_Val=list(range(0. arr_Len, 2))
arr_Val.remove(4)
print(arr_Str[1].find('i')+arr_Val[2])

#input Sring : information-techology
#input Number : 12

st=input("영어 1글자를 입력하세요")
if st.isupper():     #대문자-> true 아니면 -> fals  # ture일때 수행 -> 소문자로 변경
    print(st.lower())
else:
    print(st.upper())
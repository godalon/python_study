# # if  문 문법
# a,b = 1,10
# if a>b : 
#      print("조건이 참이면 실행 ")
#      print("실행 코드는 뛰어쓰기로 구분")
# # if문이 거짓일때
# elif a == b:
#      print("ab가 같다")
# else:  # if 문의 조건이 거짓
#      print("if조건문이 거짓일때실행")

# # print("종료")      
# 
# number = int(input("숫자를 입력 : n"))    
#     if(number %2 == 0):
#         print("짝수입니다.")
#     else:
#         print("홀수입니다.")    


height = int(input("키를 cm로 입력해 주세요 : \n"))
if height > 120:
    print("청룡열차를 탈수있습니다.")
    age = int(input("나이를 입력해주세요:\n"))
    
    if age <12:
        print("요금은 5000원입니다. ")
    elif age <=18:
        print(" 요금은 7000원 입니다.")
    else:
        print("요금은 12000원 입니다.")
        
else:
    print("죄송하지만 탈수 없습니다.")
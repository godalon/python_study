'''
# # 여러개의 변수를 동시에 초기화
# a,b,c = 1,2,3
# print(a)
# print(b)
# print(c)

# my_Name = "홍길동"
# print(my_Name)

# 놀이기구 = "자이로드롭"
# print(놀이기구)

# 살21 = 1,2,3,4
# print(살21)

# 이름 = "박써니"
# print(이름)

# x=10
# print(x)

# x,y,z = 1,2.1,"문자열"
# print(x,y,z)

# print(type (x), type (y), type (z))

# # 🚨 여기 코드는 수정 안합니다.👇
# a = input("a: ")
# b = input("b: ")
# # 🚨 여기 코드는 수정 안합니다. 👆
# a , b = b,a
# print("a: " +a)
# print("b: " +b)
'''

# 문자열 
# 긴 문자열은 따옴표 3개 (''',"""")
var3 = '''
'따옴표 '3 개는 
끝나는 문장까지 
모두를 문자열로 처리
----------------------!
'''
print (var3)

# 문자열 (+) 연산
성 = '홍'
이름 = '길동'
name = 성 + ' ' + 이름
print(name)

#타입 변환 : str(), int(), float()

print(type(int(str(100))))


# 1
str1 = '\tIt\'s "kind of" sunny\n Have a nice Day!'
print(str1)

# 2
str2='''
다스베이더가 말했다. "내가 니 애비다!" 그말을 들은 루크는 '깜짝'놀랐다.
'''
print(str2)
#3
print("밴드 이름 만들기 프로그램에 환영합니다.")
city = input('태어난 도시가 어딘가요??\n')
petName = input('애완동물의 이름은?\n')
print ('당신의 밴드 이름은' +city + ' ' + petName)
# \n 한줄 띄우기



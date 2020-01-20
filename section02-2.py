# Section02-2
# 파이썬 기초 코딩
# 몸풀기 코딩 실습

# import this # 파이썬에 대한 철학을 볼 수 있는 문구
import sys

# 파이썬 기본 인코딩 (3.x에서는 입력과 출력 기본이 utf-8 이다)
print(sys.stdin.encoding)
print(sys.stdout.encoding)

# 출력문
print('My name is Goodboy!')

# 변수 선언 (어떤 값을 선언하여 할당하는 것)
myName = 'Goodboy'

# 조건문
if myName == 'Goodboy':
    print('ok')

# indent(들여쓰기) 자체를 문법으로 규정

# 반복문
for i in range(1,10):
    for j in range(1,10):
        print('%d * %d ='%(i,j), i*j)

# 변수 선언(한글)
# 한글도 가능하지만 절대 권장되지 않는다.
이름 = '좋은사람'

# 출력
print(이름)

# 함수 선언(한글)
def 인사():
    print("안녕하세요. 반갑습니다.")

인사()

# 함수 선언
def greeting():
    print('Hello!')

greeting()

# 클래스
class Cookie:
    pass

# 객체 생성
cookie = Cookie()

print(id(cookie))
print(dir(cookie))
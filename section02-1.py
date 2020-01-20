# Section02-1
# 파이썬 기초 코딩
# Print 구문의 이해
# 참고 : https://www.python-course.eu/python3_formatted_output.php

# 기본출력 
print('Hello Python!')
print("Hello Python!")
print("""Hello Python!""")
print('''Hello Python!''')
# 작은 따옴표와 큰 따옴표를 다 사용가능하다
# 3개씩 뭉쳐진 형태도 가능하다
# 학원에서 배울 때는 혼용해서 사용했으나 
# 세세한 사용법에 대한 설명이 있을 시 추가한다.

print()

# Separator 옵션 사용
print('T','E','S','T')
print('T','E','S','T',sep='')
print('2019','02','19',sep='-')
print('niceman','google.com',sep='@')
# 단어들 사이를 이어주는 separator 를 지정한다.

# end 옵션 사용
# print 함수가 자동으로 개행을 해주는 것을 막고
# 끝에 어떤 문자나 형식을 추가할 수 있다.
print('Welcome To', end=' ')
print('the black parade',end=' ')
print('piano notes')
print('testset')

print()

# format 사용
print('{} and {}'.format('You','Me'))
print("{0} and {1} and {0}".format('You','Me'))
print("{a} are {b}".format(a='You',b='Me'))

# format 을 사용할 때 보다 더 정확하게 명시를 해줄 수 있다.
# 코딩을 함에 있어서는 가장 정확하게 명시해줄 수 있음에 효과적이다.
print("%s's favorite number is %d"%('Eunki',7)) # %s : 문자, %d : 정수, %f : 실수

# %4.2f = 정수부 4자리 소수부 2자리
print("Test1 : %5d, Price: %4.2f"%(776, 6534.123))
print("Test1 : {0:5d}, Price: {1: 4.2f}".format(776,6534.1234))
print("Test1 : {a: 5d}, Price: {b: 4.2f}".format(a=776, b=6534.1234))

"""
참고 : Escape 코드

\n : 개행
\t : 탭
\\ : 문자
\' : 문자
\" : 문자
\r : 캐리지 리턴
\f : 폼 피드
\a : 벨 소리
\b : 백 스페이스
\000 : 널 문자
"""

print("'you'")
print('\'you\'')
print('"you"')
print("""'you'""")
print('\\you\\\n')
print('\t\t\ttest')
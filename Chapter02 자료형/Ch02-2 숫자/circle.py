# > 원의 반지름을 사용자로부터 입력받아 둘레와 면적을 구하는 프로그램 작성 (circle.py)
r = int(input("반지름을 입력하시오:"))
a = 3.14
print('원의 둘레는 %s 입니다.' %int(2*a*r))
print('원의 면적은 %s 입니다.' %int(a*r*r))
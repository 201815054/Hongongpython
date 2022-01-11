from math import pi
 
PI = pi

def number_input():
    output = input("숫자 입력")
    return float(output)

def get_circumference(radius):
    return 2* PI * radius

def get_circle_area(radius):
    return PI * radius ** 2  #변수도 있고 함수도 있어서 모듈을 만든것임.
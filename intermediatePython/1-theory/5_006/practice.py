'''
사용자가 가로, 세로 길이를 입력하면 삼각형과 사각형의 넓이 출력
'''

def area():
    width = int(input('가로 길이 입력 : '))
    height = int(input('세로 길이 입력 : '))
    triangle = width * height / 2
    square = width * height

    print(f'삼각형의 넓이 : {triangle}')
    print(f'사각형의 넓이 : {square}')

area()

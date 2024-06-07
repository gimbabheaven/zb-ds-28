'''
키오스크에서 메뉴를 선택하면 영수증이 출력되는 프로그램
'''
print('1. 카페라떼(3.5)\t2. 에스프레소(3.0)\t3. 아메리카노(2.0)\t4. 곡물라뗴(4.0)\t5. 밀크티(4.3)\t')

userMenu = int(input('메뉴를 선택하세요 : '))

print('-'*10)
if userMenu == 1:
    print('메뉴 : 카페라떼 \n가격 : 3,500원')
elif userMenu ==2:
    print('메뉴 : 에스프레소 \n가격 : 3,000원')
elif userMenu ==3:
    print('메뉴 : 아메리카노 \n가격 : 2,000원')
elif userMenu ==4:
    print('메뉴 : 곡물라떼 \n가격 : 4,000원')
elif userMenu ==5:
    print('메뉴 : 밀크티 \n가격 : 4,300원')
else:
    print('올바른 메뉴 번호를 입력하세요.')

print('-'*10)
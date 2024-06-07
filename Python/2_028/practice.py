'''
출퇴근시 이용하는 교통 수단에 따라 세금을 감면해주는 정책을 세우려고 한다.
다음 내용에 맞게 프로그램을 만들어보자
'''
question = int(input('당신은 출퇴근 대상자인가요 ? 1. Yes, 2. No')) 

if question == 1: #출퇴근 대상자
    question2 = int(input('이용 수단을 선택하세요 : 1. 도보, 자전거 2. 버스, 지하철 3. 자가용 '))
    if question2 == 1:
        print('세금 5% 감면 대상자 입니다.')
    elif question2 == 2:
        print('세금 감면 3% 대상자 입니다.')
    elif question2 == 3:
        print('추가 세금 1% 대상자 입니다.')
    else:
        print('보기를 제대로 선택하세요.')
elif question ==2:
    print('세금 변동 없음') #출퇴근 대상자 아님
else:
    print('보기를 제대로 선택하세요.')

def sendSMS(msg):
    if len(msg) > 10:
        raise Exception('길이 초과, MMS 전환', 1)
    else:
        print('SMS 발송 성공')

def sendMMS(msg):
    if len(msg) <= 10:
        raise Exception('길이 미달, SMS 전환', 2)
    else:
        print('MMS 발송')

msg = input('input message : ')

try:
    sendSMS(msg)
except Exception as e:
    print(f'e : {e.args[0]}')
    print(f'e : {e.args[1]}')

    if e.args[1] == 1: #두번째 매개변수 값을 통해 continue 동작 선언
        sendMMS(msg)
    elif e.args[2] == 2:
        sendSMS(msg)

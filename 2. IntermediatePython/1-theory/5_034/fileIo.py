import time

file = open('/Users/lydia/workspace/zb-ds-28/intermediatePython/text/schedule.txt', 'w') # 읽기모드, 파일 없으면 새로 생성, truncate 이후 쓰기
 
lt = time.localtime()

# dateStr = '[' + str(lt.tm_year) + '년 ' + str(lt.tm_mon) + '월 ' + str(lt.tm_mday) + '일] '

dateStr = '[' + time.strftime('%Y-%m-%d %H:%M:%S %p') + '] '
todaySchedule = input('스케줄을 입력하세여 : ')

file.write(dateStr + todaySchedule)

file.close()





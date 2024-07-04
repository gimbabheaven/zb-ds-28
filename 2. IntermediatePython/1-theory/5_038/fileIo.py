# writelines() : 리스트 또는 튜플 데이터를 파일에 쓰기 위한 함수

languages = ['c/c++', 'java', 'c#', 'python', 'javascript']

uri = '/Users/lydia/workspace/zb-ds-28/intermediatePython/text/'

""" with open(uri + 'languages.txt', 'a') as f:
    # f.write(item)
    # f.write('\n')
    f.writelines(item + '\n' for item in languages) """

with open(uri + 'languages.txt', 'r') as f:
    print(f.read())

'''
모든 칸을 흰색으로 바꾸기 위해 최소로 클릭해야 하는 횟수를 반환하는 함수를 작성하세요.
뒤집기
다음과 같이 n x m 의 판이 주어집니다. () 각각의 판에는 흰색 혹은 검은색이 칠해져 있으며, 흰색은 0, 그리고 검은색은 1로 주어진다.
이제 이 모든 판의 색깔을 흰색으로 만들려고 한다. 색을 바꾸는 것은 특정 칸을 ‘클릭’ 함으로써 이루어진다. 
한 번에 한 칸을 ‘클릭’ 할 수 있으며, 한 칸을 ‘클릭’ 할 경우에는 그 칸의 색깔 뿐만 아니라 상, 하, 좌, 우 칸의 모두 색깔이 바뀐다. 
즉, 흰색일 경우에는 검은색으로, 검은색일 경우에는 흰색으로 바뀐다. 만약 (0, 0) 과 같이 상, 좌 칸은 없고 하, 우 칸만 존재할 경우, 그 존재하는 칸의 색깔만 바뀌게 된다.
n x m 의 판의 상태가 주어질 때, 이를 모두 흰색으로 만들기 위하여 ‘클릭’ 해야하는 최소 칸의 수를 출력하는 프로그램을 작성하시오. 
만약, ‘클릭’을 통하여 모두 흰색으로 바꾸는 것이 불가능하다면 -1을 출력한다.

입력
첫째 줄에 n, m이 주어진다. 두 번째 줄부터 각 칸의 상태가 주어진다. 0은 흰색을 의미하며, 1은 검은색을 의미한다.

입력 예시 1
4 3
0 1 0
1 0 1
1 0 1
0 1 0

출력 예시 1
2

설명 1
(2, 1)을 클릭한 후, (1, 1)을 클릭하면 모든 칸이 흰색이 된다.

입력 예시 2
4 6
0 1 1 0 1 0
1 1 0 0 1 1
1 0 0 0 1 0
0 1 0 0 0 0

출력 예시 2
4

설명 2
(1, 2), (2, 1), (1, 4), 그리고 (1, 1)을 차례대로 클릭하면 모든 칸을 흰색으로 만들 수 있다.

입력 예시 3
4 4
0 0 0 0
0 0 1 1
0 0 1 0
0 0 0 0

출력 예시 3
-1

문제 조건
1≤n≤1000
1≤m≤10
'''
import sys
sys.setrecursionlimit(100000)

def flip(myMap, n, m) :

    return 0

def main():
    '''
    이 부분은 수정하지 마세요.
    '''

    data = [int(x) for x in input().split()]

    n = data[0]
    m = data[1]

    myMap = []

    for i in range(n) :
        line = [int(x) for x in input().split()]
        myMap.append(line)

    print(flip(myMap, n, m))

if __name__ == "__main__":
    main()

#elice_utils.py
import base64
import mimetypes
import os
import urllib.parse
import urllib.request

EXECUTION_TOKEN = os.getenv('EXECUTION_TOKEN')
EXECUTOR_IP = os.getenv('EXECUTOR_IP')
EXECUTOR_COM_PORT = os.getenv('EXECUTOR_COM_PORT')

if not all((EXECUTION_TOKEN, EXECUTOR_IP, EXECUTOR_COM_PORT)):
    raise Exception('Invalid elice environment.')

_OTP_KEY = None


def _send(url, data):
    data_encoded = urllib.parse.urlencode(data)
    q = urllib.request.Request(url,
                               data=data_encoded.encode('utf-8'))

    try:
        urllib.request.urlopen(q)
    except Exception:
        raise Exception('Failed to send message to elice.')


def _handle_image(filepath):
    mtype, _ = mimetypes.guess_type(filepath)

    if mtype is None or not mtype.startswith('image/'):
        raise ValueError('Invalid image filepath.')

    with open(filepath, 'rb') as f:
        data = 'data:%s;base64,%s' % (
            mtype,
            base64.b64encode(f.read()).decode('utf-8')
        )

    return data


def _handle_file(filepath):
    mtype, _ = mimetypes.guess_type(filepath)

    with open(filepath, 'rb') as f:
        data = '%s;data:%s;base64,%s' % (
            os.path.basename(filepath),
            mtype or 'application/octet-stream',
            base64.b64encode(f.read()).decode('utf-8')
        )

    return data


def send(msg_type, msg_data):
    _send(
        'http://%s:%s/comm/send/%s' % (EXECUTOR_IP,
                                       EXECUTOR_COM_PORT,
                                       EXECUTION_TOKEN),
        {'type': msg_type, 'data': msg_data}
    )


def send_image(filepath):
    send('image', _handle_image(filepath))


def send_file(filepath):
    send('file', _handle_file(filepath))


def secure_init():
    try:
        r = urllib.request.urlopen(
            'http://%s:%s/comm/secure/init/%s' % (EXECUTOR_IP,
                                                  EXECUTOR_COM_PORT,
                                                  EXECUTION_TOKEN)
        )
    except Exception:
        raise Exception('Failed to initialize elice util secure channel.')

    global _OTP_KEY
    _OTP_KEY = r.read().decode('utf-8')


def secure_send(msg_type, msg_data):
    _send(
        'http://%s:%s/comm/secure/send/%s/%s' % (EXECUTOR_IP,
                                                 EXECUTOR_COM_PORT,
                                                 EXECUTION_TOKEN,
                                                 _OTP_KEY),
        {'type': msg_type, 'data': msg_data}
    )


def secure_send_image(filepath):
    secure_send('image', _handle_image(filepath))


def secure_send_file(filepath):
    secure_send('file', _handle_file(filepath))


def secure_send_grader(msg):
    secure_send('grader', msg)


def secure_send_score(score):
    secure_send('score', score)

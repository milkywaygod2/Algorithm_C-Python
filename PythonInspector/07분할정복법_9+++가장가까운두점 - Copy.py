'''
n개의 점이 주어질 때, 가장 가까운 두 점 사이의 거리의 제곱을 반환하는 함수를 작성하세요.
예를 들어, 점이 4개가 있고, 각각의 좌표가 (0, 3), (1, 1), (2, 2), (7, 1) 이라면 points에는 다음과 같이 그 정보가 저장됩니다.
points = [ (0, 3), (1, 1), (2, 2), (7, 1) ]
이 때, 가장 가까운 두 점 사이의 거리의 제곱은 2입니다.

가장 가까운 두 점 찾기 (Big)
2차원 평면에 n개의 점이 있다. 이 점들 중에서 그 거리가 가장 가까운 두 점 사이의 거리의 제곱을 출력하는 프로그램을 작성하시오. 
단, 두 점 (x1, y1)과 (x2, y2) 사이의 거리는 sqrt( (x1-x2)^2 + (y1-y2)^2 ) 로 정의된다.
예를 들어, 4개의 점이 각각 (0, 3), (1, 1), (2, 2), (7, 1) 에 위치해 있다고 하면, 가장 가까운 두 점은 (1, 1)과 (2, 2)이며, 그 거리의 제곱은 2이다.
이때 그 거리의 제곱인 2를 출력하면 됩니다.

입력 예시
4
0 3
1 1
2 2
7 1

출력 예시
2

문제 조건
점의 개수는 최대 100,000개를 넘지 않습니다.
점의 좌표는 모두 정수입니다.
'''


import sys

def getDistBig(points) :

    return 0

def main():
    '''
    이 부분은 수정하지 마세요.
    '''

    n = int(input())
    points = []

    for i in range(n) :
        line = [int(x) for x in input().split()]
        points.append( (line[0], line[1]) )

    print(getDistBig(points))

if __name__ == "__main__":
    main()

#eilce_utils.py
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

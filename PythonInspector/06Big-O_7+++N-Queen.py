
'''
n개의 Queen을 배치하는 경우의 수를 반환하는 함수를 작성하세요.
N-Queen n x n 의 체스 판에 n개의 Queen을 놓으려 합니다. 이 때, 다음의 규칙을 반드시 따라야 합니다.
같은 행에 2개 이상의 Queen이 존재해서는 안됩니다.
같은 열에 2개 이상의 Queen이 존재해서는 안됩니다.
하나의 대각선에 2개 이상의 Queen이 존재해서는 안됩니다. 이는 ‘\’ 방향의 대각선과 ‘/’ 방향의 대각선 모두에 대하여 해당되는 조건입니다.
예를 들어 n = 4 일 경우, 아래와 같이 Queen을 배치하는 것은 가능하지 않다.

first 왜냐하면 다음과 같이 조건 1, 그리고 조건 3에 반하기 때문이다.

second n = 4 일 경우에는 다음과 같이 Queen 을 배치할 수 있는 경우가 2가지 존재한다.

third n이 주어질 때, n개의 Queen을 배치할 수 있는 경우의 수를 출력하는 프로그램을 작성하시오.

입력 예시 1
4

출력 예시 1
2

입력 예시 2
5

출력 예시 2
10

힌트) itertools의 모듈의 permutations()함수를 사용하면 for문을 사용하지 않고도 순열을 구할 수 있습니다.
from itertools import permutations
p = ['a', 'b', 'c']
perm = permutations(p)
print(list(perm))
# 출력 결과
# [('a', 'b', 'c'), ('a', 'c', 'b'), ('b', 'a', 'c'), ('b', 'c', 'a'), ('c', 'a', 'b'), ('c', 'b', 'a')]

문제 조건
퀸의 개수는 최대 10개입니다.
'''
import sys
sys.setrecursionlimit(100000)

def nQueen(n) :

    return 0

def main():
    '''
    이 부분은 수정하지 마세요.
    '''

    n = int(input())

    print(nQueen(n))

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

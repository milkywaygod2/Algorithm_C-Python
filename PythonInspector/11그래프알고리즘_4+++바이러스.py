'''
엘리스 바이러스의 개체 수가 n개가 될 수 있으면 True, 아니면 False를 반환하는 함수를 작성합니다.

바이러스
엘리스 바이러스는 그 개체 수가 불규칙하기로 매우 유명한 바이러스입니다. 
이 바이러스의 개체 수는 1초가 지날때마다 변화하는데, 그 개체 수가 2배로 늘어날 수도 있고, 1/3배로 줄어들 수도 있습니다. 
예를 들어, 현재 시간에 바이러스가 10마리라면, 1초 후에는 20마리가 될 수도 있고, 3마리가 될 수도 있습니다.

엘리스 바이러스는 특성상 10000 마리를 초과하지 못합니다. 예를 들어, 현재 개체수가 7000개라면, 2배로 늘어날 수 없다는 의미입니다. 
왜냐하면 2배로 늘어날 경우 그 개체 수가 14000 마리가 되는데, 이는 10000 마리를 초과하기 때문입니다.
엘리스 바이러스는 초기에 그 개체 수가 1개라고 할 때, 일정 시간이 지나면 특정한 개체수 m마리가 될 수 있는지를 판단하는 프로그램을 작성하세요. 
예를 들어, m = 10일 경우, 엘리스 바이러스의 개체 수가 10마리가 될 수 있는가를 묻는 것이며, 이는 가능합니다. 그 가능한 방법 중 하나는 다음과 같습니다.
1 -> 2 -> 4 -> 8 -> 16 -> 5 -> 10

입력
첫째 줄에 엘리스 바이러스의 최종 개체 수 m이 주어집니다.

출력
엘리스 바이러스의 개체 수가 1부터 시작할 때, 개체 수가 m개가 될 수 있다면 True, 아니면 False를 출력합니다.

입력 예시
10

출력 예시
True
'''

import sys
sys.setrecursionlimit(100000)

def checkVirus(n) :


    result = True 

    return result 

#main.py
def main():
    '''
    이 부분은 수정하지 마세요.
    '''

    m = int(input())

    print(checkVirus(m))

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

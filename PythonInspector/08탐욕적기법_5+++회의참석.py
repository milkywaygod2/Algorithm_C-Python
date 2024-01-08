
'''
회의 일정이 list로 주어질 때, 엘리스씨가 참석할 수 있는 최대 회의 수를 반환하는 함수를 작성하세요. 
회의 참석
n개의 회의가 언제 시작하는지, 그리고 언제 끝나는지가 주어진다. 엘리스씨는 이제 이 n개의 미팅 중에서 최대한 많은 미팅에 참석하고자 한다. 
물론, 동시에 진행되는 두 개의 회의에는 동시에 참석할 수 없다. 또한, 10초에 끝나는 회의와 10초에 시작하는 회의가 있다면, 이 두 회의에는 모두 참석할 수 있다고 하자.
n개의 회의에 대한 정보가 주어질 때, 엘리스씨가 참석할 수 있는 회의의 최대 개수를 출력하는 프로그램을 작성하시오.
입력의 첫째 줄에 회의실의 개수 n이 주어진다.이후 각 회의에 대하여 회의가 시작하는 시간, 그리고 끝나는 시간이 주어진다.

입력 예시 1
5
1 4
3 5
2 7
4 6
7 8

출력 예시 1
3

문제 조건
회의실의 개수는 최대 100,000개 입니다.
회의의 시작시간과 종료시간은 모두 정수입니다.
출력
엘리스씨가 참석할 수 있는 회의의 최대 수를 출력한다.
'''
import sys

def attending(meetingList) :

    return 0

def main():

    n = int(input())
    meetingList = []

    for i in range(n) :
        data = [int(x) for x in input().split()]
        meetingList.append( (data[0], data[1]) )

    print(attending(meetingList))

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

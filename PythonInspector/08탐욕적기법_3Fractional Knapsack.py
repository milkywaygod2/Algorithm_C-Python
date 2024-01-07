import sys

def fKnapsack(materials, maxWeight) :
    '''
    무게 maxWeight까지 버틸 수 있는 베낭이 담을 수 있는 최대 가치를 반환하는 함수를 작성하세요.
    주의 : 셋째 자리에서 반올림하는 것을 고려하지 않고 작성하셔도 됩니다. 
    materials의 인자를 m이라 할때,
    m[0] : 무게
    m[1] : 가치
    '''
    materials = sorted(materials, key = lambda m : m[1]/m[0], reverse=True)
    #sort는 원본리스트 직접변경-반환값none, sorted는 원본리스트변경x-정렬된리스트반환
    #lambda는 임의의 인자(현재m)를 입력하여 그 인자에 간단한 연산을 적용하는 익명의 함수를 생성
    #reverse=True는 내림차순, 기본은 오름차순임

    accValue = 0
    accWeight = 0

    for i in range(len(materials)):
        #1.i를 넣어도 maxWeight에 여유있을때 
        #2.i를 넣으면 maxWeight가 넘칠때.(끝)
        #3.i를 넣으면 maxWeight가 딱 찰때.(끝)
        #4.i를 다 넣어도 maxWeight가 비어있을때.(끝)
        if accWeight + materials[i][0] < maxWeight: #1
            accWeight += materials[i][0]
            accValue += materials[i][1]
        elif accWeight + materials[i][0] > maxWeight: #2
            extraWeight = maxWeight - accWeight
            accValue += extraWeight * (materials[i][1] / materials[i][0])
            return accValue
        else: #3 accWeight + materials[i][1] == m
            accWeight += materials[i][0]
            accValue += materials[i][1]
            return accValue

    return accValue #4

def main():
    '''
    이 부분은 수정하지 마세요.
    '''

    line = [int(m) for m in input().split()]

    n = line[0]
    maxWeight = line[1]

    materials = []

    for i in range(n) :
        data = [int(m) for m in input().split()]
        materials.append( (data[0], data[1]) )

    print("%.3lf" % fKnapsack(materials, maxWeight))

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

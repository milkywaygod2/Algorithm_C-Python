'''
멱집합 : 어떤집합의, 모든 부분집합을 모은 집합, 수학-집합단원의 nCr개념
=> 데이터분석,머신러닝,인공지능등에서 특징선택이나 변수선택문제 해결시 사용(최적모델검사)
=> 네트워크디자인,전력등에서 경로선택문제
<= 단점 집합크기커질수록 계산복잡도 급격히 높아짐O(n^3)
n개의 원소를 가지는 집합 A의 멱집합의 원소를 [[[사전 순서대로]]] list로 반환하는 함수를 작성하시오.
집합 A에 대하여, A의 모든 부분집합을 원소로 가지는 집합을 A의 멱집합이라고 한다. 
예를 들어, 집합 A의 원소가 {1, 2, 3} 일 경우, A의 멱집합은 다음과 같이 8개의 원소를 갖는 집합이다.
{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}
집합 A의 원소는 1부터 n까지의 자연수로 구성된다. 
n이 주어질 때, A의 멱집합의 원소를 사전 순서대로 모두 출력하여 배열에 저장하는 프로그램을 작성하시오. 
단, 공집합은 제외하고 출력한다.
3

1
1 2
1 2 3
1 3
2
2 3
3
'''
import sys

def getPowerset(n, k):
    if n == k:
        return [[k]]

    result = [[k]] #1자기자신
    temp = []

    for kk in range(k+1,n+1): #2자기자신다음수kk~n까지 멱집합 구하기 재귀
        temp = temp + getPowerset(n,kk) #전부 [ [],[], ... ,[] ] 형태로 더해짐

    for i in range(len(temp)): #3반환된 부분집합에 자기자신k를 포함시켜줌 []레벨
        temp[i] = [k] + temp[i] #[k, ..부분집합]

    return result + temp #1과 3을 합쳐줌, [ [k], [k, ...부분집합], ... , [k, temp[i]] ]

def powerSet(n) :
    '''
    n개의 원소를 가지는 집합 A의 멱집합의 원소를 사전 순서대로 list로 반환하는 함수를 작성하시오.
    예를 들어, n = 3 일 경우 다음의 list를 반환한다.
    [ [1], [1, 2], [1, 3], [1, 2, 3], [2], [2, 3], [3] ]
    '''
    result = []
    for i in range(1, n+1): #range두번째인자직전까지시퀸스 1~n까지
        result += getPowerset(n, i) #반환값을 배열에 밀어넣기

    return result

def main():
    '''
    이 부분은 수정하지 마세요.
    '''

    n = int(input())

    result = powerSet(n)
    
    for line in result :
        print(*line)

if __name__ == "__main__":
    main()

#elice_utiles.py
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

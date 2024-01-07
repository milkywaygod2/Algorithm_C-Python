'''
균형 맞추기 : 모든 부분집합의 모든 합을 구한다음 비교하여 가장 작은 값을 선택하는 것 (멱집합:모든부분집합을 모은 집합, 수학-집합단원의 nCr개념)
n개의 숫자를 두 그룹 A, B로 나눈다고 할 때, | (A의 원소의 합) - (B의 원소의 합) | 의 최솟값을 반환하는 함수를 작성하시오.

n개의 숫자가 주어진다. 이제 이 숫자를 두 개의 그룹으로 나눌 것이다. 예를 들어 5개의 숫자 [1, -3, 4, 5, -2] 가 주어진다면, 
이를 두 개의 그룹으로 나누는 경우는 여러가지가 있을 수 있다. 가능한 경우로써 [1, -3], [4, 5, -2] 가 있을 수 있고, 또 다른 경우로는 [1, 4, -2], [-3, 5] 가 있을 수 있다.
나눈 두 그룹을 A, B라고 할 때, (A의 원소의 합) - (B의 원소의 합) 의 절댓값을 최소화 하는 프로그램을 작성하시오. 
위의 예제에서는 A = [1, 4, -2], B = [-3, 5] 라고 하였을 때 (A의 원소의 합) - (B의 원소의 합) 의 절댓값 = |3 - 2| = 1 이며, 이보다 더 작은 값을 만드는 A, B는 존재하지 않는다.
이 경우 절댓값의 최솟값인 1을 출력하면 된다.
1 -3 4 5 -2

1
'''
import sys
import math

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

#자연수1~n의 멱집합을 반환
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

def makeEqual(data) :
    '''
    n개의 숫자를 두 그룹 A, B로 나눈다고 할 때,

    | (A의 원소의 합) - (B의 원소의 합) | 의 최솟값을 반환하는 함수를 작성하시오.
    '''
    #1~n 범위의 리턴 = {r = (1→n)}nCr의 모든 부분집합
    everyC = powerSet(len(data)) 
    sumTotal = sum(data)
    result = math.inf #무한대-초기화

    for c in everyC: #모든 부분집합
        sumA = 0
        sumB = 0

        for i in c: #각 부분집합i의 
            sumA += data[i-1] #원소의 합
            sumB = sumTotal - sumA #부분집합i의 여집합의 합
        
        result = min(result, abs(sumA-sumB)) #최소편차값 남기고 버리기

    return result

def main():
    '''
    이 부분은 수정하지 마세요.
    '''

    data = [int(x) for x in input().split()]

    print(makeEqual(data))

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

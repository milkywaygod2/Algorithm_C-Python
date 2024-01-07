'''
���� ���߱� : ��� �κ������� ��� ���� ���Ѵ��� ���Ͽ� ���� ���� ���� �����ϴ� �� (������:���κ������� ���� ����, ����-���մܿ��� nCr����)
n���� ���ڸ� �� �׷� A, B�� �����ٰ� �� ��, | (A�� ������ ��) - (B�� ������ ��) | �� �ּڰ��� ��ȯ�ϴ� �Լ��� �ۼ��Ͻÿ�.

n���� ���ڰ� �־�����. ���� �� ���ڸ� �� ���� �׷����� ���� ���̴�. ���� ��� 5���� ���� [1, -3, 4, 5, -2] �� �־����ٸ�, 
�̸� �� ���� �׷����� ������ ���� ���������� ���� �� �ִ�. ������ ���ν� [1, -3], [4, 5, -2] �� ���� �� �ְ�, �� �ٸ� ���δ� [1, 4, -2], [-3, 5] �� ���� �� �ִ�.
���� �� �׷��� A, B��� �� ��, (A�� ������ ��) - (B�� ������ ��) �� ������ �ּ�ȭ �ϴ� ���α׷��� �ۼ��Ͻÿ�. 
���� ���������� A = [1, 4, -2], B = [-3, 5] ��� �Ͽ��� �� (A�� ������ ��) - (B�� ������ ��) �� ���� = |3 - 2| = 1 �̸�, �̺��� �� ���� ���� ����� A, B�� �������� �ʴ´�.
�� ��� ������ �ּڰ��� 1�� ����ϸ� �ȴ�.
1 -3 4 5 -2

1
'''
import sys
import math

def getPowerset(n, k):
    if n == k:
        return [[k]]

    result = [[k]] #1�ڱ��ڽ�
    temp = []

    for kk in range(k+1,n+1): #2�ڱ��ڽŴ�����kk~n���� ������ ���ϱ� ���
        temp = temp + getPowerset(n,kk) #���� [ [],[], ... ,[] ] ���·� ������

    for i in range(len(temp)): #3��ȯ�� �κ����տ� �ڱ��ڽ�k�� ���Խ����� []����
        temp[i] = [k] + temp[i] #[k, ..�κ�����]

    return result + temp #1�� 3�� ������, [ [k], [k, ...�κ�����], ... , [k, temp[i]] ]

#�ڿ���1~n�� �������� ��ȯ
def powerSet(n) :
    '''
    n���� ���Ҹ� ������ ���� A�� �������� ���Ҹ� ���� ������� list�� ��ȯ�ϴ� �Լ��� �ۼ��Ͻÿ�.
    ���� ���, n = 3 �� ��� ������ list�� ��ȯ�Ѵ�.
    [ [1], [1, 2], [1, 3], [1, 2, 3], [2], [2, 3], [3] ]
    '''
    result = []
    for i in range(1, n+1): #range�ι�°������������������ 1~n����
        result += getPowerset(n, i) #��ȯ���� �迭�� �о�ֱ�

    return result

def makeEqual(data) :
    '''
    n���� ���ڸ� �� �׷� A, B�� �����ٰ� �� ��,

    | (A�� ������ ��) - (B�� ������ ��) | �� �ּڰ��� ��ȯ�ϴ� �Լ��� �ۼ��Ͻÿ�.
    '''
    #1~n ������ ���� = {r = (1��n)}nCr�� ��� �κ�����
    everyC = powerSet(len(data)) 
    sumTotal = sum(data)
    result = math.inf #���Ѵ�-�ʱ�ȭ

    for c in everyC: #��� �κ�����
        sumA = 0
        sumB = 0

        for i in c: #�� �κ�����i�� 
            sumA += data[i-1] #������ ��
            sumB = sumTotal - sumA #�κ�����i�� �������� ��
        
        result = min(result, abs(sumA-sumB)) #�ּ������� ����� ������

    return result

def main():
    '''
    �� �κ��� �������� ������.
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

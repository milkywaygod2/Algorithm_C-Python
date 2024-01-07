'''
������ : �������, ��� �κ������� ���� ����, ����-���մܿ��� nCr����
=> �����ͺм�,�ӽŷ���,�ΰ����ɵ�� Ư¡�����̳� �������ù��� �ذ�� ���(�����𵨰˻�)
=> ��Ʈ��ũ������,���µ�� ��μ��ù���
<= ���� ����ũ��Ŀ������ ��꺹�⵵ �ް��� ������O(n^3)
n���� ���Ҹ� ������ ���� A�� �������� ���Ҹ� [[[���� �������]]] list�� ��ȯ�ϴ� �Լ��� �ۼ��Ͻÿ�.
���� A�� ���Ͽ�, A�� ��� �κ������� ���ҷ� ������ ������ A�� �������̶�� �Ѵ�. 
���� ���, ���� A�� ���Ұ� {1, 2, 3} �� ���, A�� �������� ������ ���� 8���� ���Ҹ� ���� �����̴�.
{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}
���� A�� ���Ҵ� 1���� n������ �ڿ����� �����ȴ�. 
n�� �־��� ��, A�� �������� ���Ҹ� ���� ������� ��� ����Ͽ� �迭�� �����ϴ� ���α׷��� �ۼ��Ͻÿ�. 
��, �������� �����ϰ� ����Ѵ�.
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

    result = [[k]] #1�ڱ��ڽ�
    temp = []

    for kk in range(k+1,n+1): #2�ڱ��ڽŴ�����kk~n���� ������ ���ϱ� ���
        temp = temp + getPowerset(n,kk) #���� [ [],[], ... ,[] ] ���·� ������

    for i in range(len(temp)): #3��ȯ�� �κ����տ� �ڱ��ڽ�k�� ���Խ����� []����
        temp[i] = [k] + temp[i] #[k, ..�κ�����]

    return result + temp #1�� 3�� ������, [ [k], [k, ...�κ�����], ... , [k, temp[i]] ]

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

def main():
    '''
    �� �κ��� �������� ������.
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

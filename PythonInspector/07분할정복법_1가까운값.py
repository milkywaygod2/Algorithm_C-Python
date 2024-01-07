'''
1 4 6 7 10 14 16
8

7
'''
import sys

def getNearestInternal(data, m):
    if len(data) == 1:
        return (data[0].data[0])
    elif len(data) == 2:
        return (data[0], data[1]) # [0] m���� ����, [1]m�̻� ����
    
    mid = len(data)//2 #�߾Ӱ�
    if data[mid] <= m:
        return getNearestInternal(data[mid:],m)
    else:
        return getNearestInternal(data[:mid+1],m)


def getNearest(data, m) :
    '''
    "������������ ���ĵ�!" n���� ���ڰ� list�� �־�����, ���� m�� �־��� ��, 
    n���� ���� �߿��� m�� ���� ����� ���ڸ� ��ȯ�ϴ� �Լ��� �ۼ��ϼ���.
    ����Ž���� �����ϴ� �ͺ��� �ݾ������� ��͵����� �������� ���� ����Ʈ!!
    1.������ �������� ���� ���� ����� ��ã��, ���ؼ� �� ����� �� ��ȯ
    '''
    value = getNearestInternal(data,m)
    if (m - value[0]) <= (value[1] - m):
        return value[0] # =��Ȳ������ [0][1] ����ų� ����
    else:
        return value[1]
    

    return 0

def main():
    '''
    �� �κ��� �������� ������.
    '''

    data = [int(x) for x in input().split()]
    m = int(input())

    print(getNearest(data, m))

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

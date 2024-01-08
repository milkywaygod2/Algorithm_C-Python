'''
������ ���̷����� ��ü ���� n���� �� �� ������ True, �ƴϸ� False�� ��ȯ�ϴ� �Լ��� �ۼ��մϴ�.

���̷���
������ ���̷����� �� ��ü ���� �ұ�Ģ�ϱ�� �ſ� ������ ���̷����Դϴ�. 
�� ���̷����� ��ü ���� 1�ʰ� ���������� ��ȭ�ϴµ�, �� ��ü ���� 2��� �þ ���� �ְ�, 1/3��� �پ�� ���� �ֽ��ϴ�. 
���� ���, ���� �ð��� ���̷����� 10�������, 1�� �Ŀ��� 20������ �� ���� �ְ�, 3������ �� ���� �ֽ��ϴ�.

������ ���̷����� Ư���� 10000 ������ �ʰ����� ���մϴ�. ���� ���, ���� ��ü���� 7000�����, 2��� �þ �� ���ٴ� �ǹ��Դϴ�. 
�ֳ��ϸ� 2��� �þ ��� �� ��ü ���� 14000 ������ �Ǵµ�, �̴� 10000 ������ �ʰ��ϱ� �����Դϴ�.
������ ���̷����� �ʱ⿡ �� ��ü ���� 1����� �� ��, ���� �ð��� ������ Ư���� ��ü�� m������ �� �� �ִ����� �Ǵ��ϴ� ���α׷��� �ۼ��ϼ���. 
���� ���, m = 10�� ���, ������ ���̷����� ��ü ���� 10������ �� �� �ִ°��� ���� ���̸�, �̴� �����մϴ�. �� ������ ��� �� �ϳ��� ������ �����ϴ�.
1 -> 2 -> 4 -> 8 -> 16 -> 5 -> 10

�Է�
ù° �ٿ� ������ ���̷����� ���� ��ü �� m�� �־����ϴ�.

���
������ ���̷����� ��ü ���� 1���� ������ ��, ��ü ���� m���� �� �� �ִٸ� True, �ƴϸ� False�� ����մϴ�.

�Է� ����
10

��� ����
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
    �� �κ��� �������� ������.
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

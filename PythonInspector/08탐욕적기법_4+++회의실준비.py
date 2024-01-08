
'''
ȸ�� ������ list�� �־��� ��, ���������� �غ��ؾ� �ϴ� ȸ�ǽ��� ���� �ּڰ��� ��ȯ�ϴ� �Լ��� �ۼ��ϼ���.
�� ������ tuple�� �־�����. ���� ���, �־��� �Է��� ��� ������ ���� ����ȴ�.
    
meetingList[0] = (1, 4)
meetingList[1] = (3, 5)
meetingList[2] = (2, 7)
meetingList[3] = (4, 6)

ȸ�ǽ� �غ�
���������� ���� �� ���� ���񽺸� �����ϱ� ���Ͽ� �������� ȸ�Ǹ� �ϴ� ���� ��ȣ�ϴ� ���̴�. 
���⼭ ���������� ������ n���� ȸ�ǰ� ���� �����ϴ���, �׸��� ���� ���������� ��� ������, �� ���� �� ȸ�ǰ� ��� ��ҿ��� �̷������ �ϴ����� ���Ѵ�. 
�� ȸ�ǰ� �����ϴ� �ð�, �׸��� ������ �ð��� �ʴ����� �־����ٰ� ����. ���� ���, �ϳ��� ȸ�Ǵ� 10�ʿ� �����Ͽ� 99�ʿ� ���� �� �ִ�.
�翬�ϰԵ�, �� ���� ȸ�ǰ� �ð��� ��ĥ ��쿡�� ���� ȸ�ǽ��� ����� �� ����. ����, ���� ��Ȯ�� 10�ʿ� ������ ȸ�ǰ� �ְ�, �� �ٸ� ȸ�ǰ� ��Ȯ�� 10�ʿ� �����Ѵٸ�, �� �� ȸ�Ǵ� ���� ȸ�ǽ��� ����� �� �ִ�.
ȸ�ǽ��� ������ ������ ���� ��� ������, ���������� �������� ���� ���� ȸ�ǽ��� �غ��ϰ��� �Ѵ�.
n���� ȸ�ǿ� ���� ������ �־��� ��, ��� ȸ�ǰ� �̷������ ���Ͽ� ������ �ϴ� ȸ�ǽ��� �ּ� ������ ����ϴ� ���α׷��� �ۼ��Ͻÿ�.
�Է��� ù° �ٿ� ȸ�ǽ��� ���� n�� �־�����.
���� �� ȸ�ǿ� ���Ͽ� ȸ�ǰ� �����ϴ� �ð�, �׸��� ������ �ð��� �־�����.

�Է� ���� 1
4
1 4
3 5
2 7
4 6

��� ���� 1
3

���� ����
ȸ�ǽ��� ������ �ִ� 1,000�� �Դϴ�.
'''

import sys

def reservation(meetingList) :

    return 0

def main():
    '''
    �� �κ��� �������� ������.
    '''

    n = int(input())
    meetingList = []

    for i in range(n) :
        data = [int(x) for x in input().split()]
        meetingList.append( (data[0], data[1]) )

    print(reservation(meetingList))

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

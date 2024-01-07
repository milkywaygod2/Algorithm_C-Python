
'''
��� ĭ�� ������� �ٲٱ� ���� �ּҷ� Ŭ���ؾ� �ϴ� Ƚ���� ��ȯ�ϴ� �Լ��� �ۼ��ϼ���.
������
������ ���� n x m �� ���� �־����ϴ�. () ������ �ǿ��� ��� Ȥ�� �������� ĥ���� ������, ����� 0, �׸��� �������� 1�� �־�����.
���� �� ��� ���� ������ ������� ������� �Ѵ�. ���� �ٲٴ� ���� Ư�� ĭ�� ��Ŭ���� �����ν� �̷������. 
�� ���� �� ĭ�� ��Ŭ���� �� �� ������, �� ĭ�� ��Ŭ���� �� ��쿡�� �� ĭ�� ���� �Ӹ� �ƴ϶� ��, ��, ��, �� ĭ�� ��� ������ �ٲ��. 
��, ����� ��쿡�� ����������, �������� ��쿡�� ������� �ٲ��. ���� (0, 0) �� ���� ��, �� ĭ�� ���� ��, �� ĭ�� ������ ���, �� �����ϴ� ĭ�� ���� �ٲ�� �ȴ�.
n x m �� ���� ���°� �־��� ��, �̸� ��� ������� ����� ���Ͽ� ��Ŭ���� �ؾ��ϴ� �ּ� ĭ�� ���� ����ϴ� ���α׷��� �ۼ��Ͻÿ�. 
����, ��Ŭ������ ���Ͽ� ��� ������� �ٲٴ� ���� �Ұ����ϴٸ� -1�� ����Ѵ�.

�Է�
ù° �ٿ� n, m�� �־�����. �� ��° �ٺ��� �� ĭ�� ���°� �־�����. 0�� ����� �ǹ��ϸ�, 1�� �������� �ǹ��Ѵ�.

�Է� ���� 1
4 3
0 1 0
1 0 1
1 0 1
0 1 0

��� ���� 1
2

���� 1
(2, 1)�� Ŭ���� ��, (1, 1)�� Ŭ���ϸ� ��� ĭ�� ����� �ȴ�.

�Է� ���� 2
4 6
0 1 1 0 1 0
1 1 0 0 1 1
1 0 0 0 1 0
0 1 0 0 0 0

��� ���� 2
4

���� 2
(1, 2), (2, 1), (1, 4), �׸��� (1, 1)�� ���ʴ�� Ŭ���ϸ� ��� ĭ�� ������� ���� �� �ִ�.

�Է� ���� 3
4 4
0 0 0 0
0 0 1 1
0 0 1 0
0 0 0 0

��� ���� 3
-1

���� ����
1��n��1000
1��m��10
'''
import sys
sys.setrecursionlimit(100000)

def flip(myMap, n, m) :

    return 0

def main():
    '''
    �� �κ��� �������� ������.
    '''

    data = [int(x) for x in input().split()]

    n = data[0]
    m = data[1]

    myMap = []

    for i in range(n) :
        line = [int(x) for x in input().split()]
        myMap.append(line)

    print(flip(myMap, n, m))

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

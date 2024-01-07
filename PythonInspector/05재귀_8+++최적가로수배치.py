'''
���μ�
�������� �Ǿ��ִ� ������ �� �� ���μ��� ������ �������� �ɾ��� �ֽ��ϴ�. 
���ÿ����� ���μ����� ��� ���� ������ �ǵ��� ���μ��� �߰��� �ɴ� ����� �����ϰ� �ֽ��ϴ�. ���ÿ����� ���깮���� ������ �� ���� ���� ���� ������ �ɰ� �ͽ��ϴ�.

���ǻ� ���μ��� ��ġ�� ���������κ��� ������ �ִ� �Ÿ��� ǥ���Ǹ�, ���μ��� ��ġ�� ��� ���� �����Դϴ�.
���� ���, ���μ��� (1, 3, 7, 13)�� ��ġ�� �ִٸ� (5, 9, 11)�� ��ġ�� ���μ��� �� ������ ��� ���μ����� ������ ���� �˴ϴ�. 
����, ���μ��� (2, 6, 12, 18)�� �ִٸ� (4, 8, 10, 14, 16)�� ���μ��� �� �ɾ�� �մϴ�.

�ɾ��� �ִ� ���μ��� ��ġ�� �־��� ��, ��� ���μ��� ���� ������ �ǵ��� ���� �ɾ�� �ϴ� ���μ��� �ּ� ���� ���ϴ� ���α׷��� �ۼ��ϼ���. 
��, �߰��Ǵ� ������ ������ ������ ���̿��� ���� �� �ֽ��ϴ�.

�Է�
ù° �ٿ��� �̹� �ɾ��� �ִ� ���μ��� ���� ��Ÿ���� �ϳ��� ���� N�� �־����ϴ�.
��° �ٺ��� N���� �ٿ��� �� �ٸ��� �ɾ��� �ִ� ���μ��� ��ġ�� �־����ϴ�.

�Է� ����
4
1
3
7
13

��� ����
3

��Ʈ) �̼� 3. �ִ����� ���ϱ��� GCD() �Լ��� �̿��غ�����.

���� ����
���μ��� ���� 3�̻� 100,000���� �Դϴ�.
���μ��� ��ġ�� 100,000,000 ������ �ڿ����̸�, ��� �ٸ� �� �Դϴ�.
'''
def howManyTree(n, myInput) :
    '''
    ��� ���μ��� ���� ������ �ǵ��� ���� �ɾ�� �ϴ� ���μ��� �ּҼ��� �����ϴ� �Լ��� �����ϼ���.
    '''
    
    cnt = 0

    return cnt

def main():
    '''
    �� �κ��� �������� ������.
    '''
    print("���� ������ �Է� ���ø� ��� ������ ��, �ѹ��� �ٿ��־� �ּ���")
    n = int(input())
    myInput = []
    for _ in range(n) :
        myInput.append(int(input()))

    print("���� ������ �ǵ��� ���� �ɾ�� �ϴ� ���μ��� �ּ� ���� {}�� �Դϴ�.".format(howManyTree(n, myInput)))
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

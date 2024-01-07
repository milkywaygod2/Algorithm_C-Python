'''
k��° �� ã��
n���� ���ڰ� ���ʴ�� �־��� ��, �� �������� �����ݱ��� �Էµ� ���ڵ� �߿��� k��°�� ���� ������ ��ȯ�ϴ� ���α׷��� �ۼ��ϼ���.
���α׷��� �Է����δ� ù°�ٿ� n�� k�� �Էµǰ�, ��°�ٿ� n���� ���ڰ� ���ʴ�� �־����ϴ�.
10 3
1 9 8 5 2 3 5 6 2 10

189 9
1589 8
12589 5
123589 3
1235589 3
12355689 3
122355689 2
12235568910 2

-1 -1 9 8 5 3 3 3 2 2 (��ȯ�Ұ��� ���� ��� -1)
'''
def findKth(myInput, k) :
    '''
    �� �������� k��°�� ���� ���Ҹ� ����Ʈ�� ��ȯ�մϴ�.
    =>myInput������ ���������� �Է��ϸ鼭 �׶��� K��° �� �ݺ���ȯ
    '''

    data = []   #myInput������
    result = [] #k��° ���� ���� ��ȯ��

    for element in myInput:
        data.append(element)
        data.sort() #�迭 ������������

        if len(data) < k:
            result.append(-1)
        else:
            result.append(data[k-1])

    return result

def main():
    '''
    �׽�Ʈ�� �ϰ������, �Ʒ� �κ��� �����մϴ�.
    '''

    firstLine = [int(x) for x in input("n�� k�� �Է��ϼ��� (����:10 3): ").split()]
    myInput = [int(x) for x in input("n���� ���ڸ� ���ʴ�� �Է��ϼ��� (����:1 9 8 5 2 3 5 6 2 10): ").split()]

    print('���� ���: ', *findKth(myInput, firstLine[1]))
if __name__ == "__main__":
    main()

###elice_utils.py
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

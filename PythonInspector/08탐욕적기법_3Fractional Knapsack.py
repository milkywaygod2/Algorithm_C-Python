import sys

def fKnapsack(materials, maxWeight) :
    '''
    ���� maxWeight���� ��ƿ �� �ִ� ������ ���� �� �ִ� �ִ� ��ġ�� ��ȯ�ϴ� �Լ��� �ۼ��ϼ���.
    ���� : ��° �ڸ����� �ݿø��ϴ� ���� ������� �ʰ� �ۼ��ϼŵ� �˴ϴ�. 
    materials�� ���ڸ� m�̶� �Ҷ�,
    m[0] : ����
    m[1] : ��ġ
    '''
    materials = sorted(materials, key = lambda m : m[1]/m[0], reverse=True)
    #sort�� ��������Ʈ ��������-��ȯ��none, sorted�� ��������Ʈ����x-���ĵȸ���Ʈ��ȯ
    #lambda�� ������ ����(����m)�� �Է��Ͽ� �� ���ڿ� ������ ������ �����ϴ� �͸��� �Լ��� ����
    #reverse=True�� ��������, �⺻�� ����������

    accValue = 0
    accWeight = 0

    for i in range(len(materials)):
        #1.i�� �־ maxWeight�� ���������� 
        #2.i�� ������ maxWeight�� ��ĥ��.(��)
        #3.i�� ������ maxWeight�� �� ����.(��)
        #4.i�� �� �־ maxWeight�� ���������.(��)
        if accWeight + materials[i][0] < maxWeight: #1
            accWeight += materials[i][0]
            accValue += materials[i][1]
        elif accWeight + materials[i][0] > maxWeight: #2
            extraWeight = maxWeight - accWeight
            accValue += extraWeight * (materials[i][1] / materials[i][0])
            return accValue
        else: #3 accWeight + materials[i][1] == m
            accWeight += materials[i][0]
            accValue += materials[i][1]
            return accValue

    return accValue #4

def main():
    '''
    �� �κ��� �������� ������.
    '''

    line = [int(m) for m in input().split()]

    n = line[0]
    maxWeight = line[1]

    materials = []

    for i in range(n) :
        data = [int(m) for m in input().split()]
        materials.append( (data[0], data[1]) )

    print("%.3lf" % fKnapsack(materials, maxWeight))

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

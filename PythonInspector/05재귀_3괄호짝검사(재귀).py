
'''
�ùٸ� ��ȣ���� �Ǵ��ϱ�
�� ���������� �Է����� �־����� ��ȣ�� �ùٸ� ��ȣ������ �Ǵ��ϴ� ���α׷��� �ۼ��մϴ�.
���� ���, ��(())�� �� �ùٸ� ��ȣ������, ��(()))��, Ȥ�� ��(()()(�� �� �ùٸ� ��ȣ�� �ƴմϴ�.
�ùٸ� ��ȣ�϶� ��YES����, �ùٸ��� ���� ��ȣ�϶� ��NO���� ����� ���ô�.
((()())(()())))(())
NO
(((())())(()())((())()))
YES
'''


def checkParen(p):
    '''
    ��ȣ ���ڿ� p�� ���� ������ "YES", �ƴϸ�  "NO"�� ��ȯ
    1.��������ó��
    2.p�� ������ ��ȣ�� ã�� ����
    3.���
    '''
    if len(p) == 0:
        return "YES"
    elif len(p) == 1:
        return "NO"
    
    for i in range(len(p)-1): #i�� i+1 ��ȸ�ؼ� ���� �Ŷ� -1
        if p[i] == '(' and p[i+1] == ')':
            q = p[:i]+p[i+2:] #i-1�������� i+2�� ���ĸ� ��ȯ
            return checkParen(q) #�������Ǳ��� ��͵�
    return "NO"

def main():
    '''
    �� �κ��� �������� ������.
    '''

    x = input()
    print(checkParen(x))

if __name__ == "__main__":
    main()


#elice_util.py
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

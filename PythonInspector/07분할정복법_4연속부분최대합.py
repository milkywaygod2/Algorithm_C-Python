'''
    ���Ӻκ��ִ���?..����Ž������ /2�� ����ؼ� �ð����⵵�� �������� ���̱� (����� �ߺ� ���� ���̱�, ��ǻ�ʹ� �����ϰ� �ٰ��)
    ����Ž���������, start,end ���� n���� ������ * ���õ� start-end������ n���� �κ����� ������ = O(n^3)
    ���ݾ� ������ ���ܸ� �����ؼ� ��͸� �����ԵǸ�, 2���� log(n)�� ���� ������ ���� n���� �κ����� ������ = O(2log(n)*n)       
    (���ܽ����� 1�� �Ǵ� 2�� �¼��� 2^log(n)��, ����� ���� ==>nlog(n))
    1.���ݾ� ������ ����Ѵ� + �������ǰ��. 
    2.��ģ ��� ����Ѵ�. 
    3.���������� �� ���ݾ��� ��ģ����� �κ����� ���Ѵ�. 
    = �������������ִ��� vs ���������������ִ��� vs ���罺���ִ���

    n���� ���ڰ� list�� �־��� ��, �� ���� �κ� �ִ����� ��ȯ�ϴ� �Լ��� �ۼ��ϼ���.
    1 2 -4 5 3 -2 9 -10 6 -8 7
    [1 2 -4 5 3] [-2 9 -10 6 -8 7]
    [[1 2] [-4 5 3]] [[-2 9 -10] [6 -8 7]]
    [[1] [2]/[-4] [5 3]] / [[-2] [9 -10] / [6] [-8 7]] 
    [[1] [2]/[-4] [5, 3]] / [[-2] [9, -10] / [6] [-8, 7]] ��11�� but��������� ���ܽ��ÿ��Ҵ� ������ 1��

    ��ȯ���� ���ø��� ������Ʈ�Ǵ� ��ȯ���ϻ� data[]���� ������ �״����!
    [[1] [2]/[-4] ["8"]] / [[-2] ["9"] / [6] ["7"]]
    ["3"/"8"] / ["9"/"7"] 
    ["8"] / ["9"]
    ["15"]

    15
    '''

import sys

def getSubsum(data) :
    
# 1.�������� : ���ܽ��� ����    
    n = len(data)
    if n == 1:
        return data[0] #����1���� ���ܽ���, �ڱⰪ ��ȯ�� ����, ��ͽ����� ���ܽ��ñ��� �����!

# 2.���� ����/������ ����, �ִ�κ��� ���
    mid = n//2
    left = getSubsum(data[:mid]) #���ܽ��ÿ��� ����1���� ��ȯ
    right = getSubsum(data[mid:])
    
# 3.�ִ�κ����� ����/�����ʿ� ��ģ ��� (�����ִ��Ĺ���+�������ִ�������)
    #��� Sum�� 'temp��', data[]���ҿ� ����X (������ �ƹ��� ���Ƶ� �迭��ü ����X)
    #��ͽ����� �κ����� Ž��(Sum)�ϴ� ������ ��������� 2�辿 Ȯ�� 
    back_leftSum = 0 #���� �Ĺ���
    front_rightSum = 0 #������ ������
    temp_leftSum = 0 #���� �ִ��Ĺ���
    temp_rightSum = 0 #������ �ִ�������
   
    for i in range(mid-1, -1, -1): # range(start,end,step): start~end�������� step����, range(mid) == range(0,mid,1)�� �����ݴ�
        back_leftSum += data[i]
        temp_leftSum = max(back_leftSum,temp_leftSum) # �ʱⰪ 0���� ū���� -(���� �ִ��Ĺ���)

    for i in range(mid, n):
        front_rightSum += data[i]
        temp_rightSum = max(front_rightSum, temp_rightSum) # �ʱⰪ 0���� ū���� -(������ �ִ�������)

    return max([left, right, temp_leftSum + temp_rightSum])
    #max([�����ִ�κ���,�����ִ�κ���,�����ִ��Ĺ���+�����ִ�������])
    #max([a,b,c]) : �� ���ڰ� �迭�� ���, �� �迭�� �ִ밪�� ���ڷ� �ϰ� �� �� ���� ū ���� ��ȯ
    

def main():
    '''
    �� �κ��� �������� ������.
    '''

    data = [int(x) for x in input().split()]

    print(getSubsum(data))

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

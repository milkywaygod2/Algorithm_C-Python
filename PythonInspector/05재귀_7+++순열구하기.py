'''
순열 구하기
순열이란, n개의 원소 중에서 r개를 나열하는 것을 의미합니다. 
예를 들어, 4개의 원소 중에서 2개를 나열한다고 하고, 우리가 갖고있는 원소가 ‘a’, ‘b’, ‘c’, ‘d’라면, 
그 순열은 ‘ab’, ‘ac’, ‘ad’, ‘ba’, ‘bc’, ‘bd’, ‘ca’, ‘cb’, ‘cd’, ‘da’, ‘db’, dc’ 로써 총 12개의 서로 다른 경우가 존재합니다.

입력으로 n과 r이 주어질 때, n개의 원소 중에서 r개를 나열한 결과를 출력하는 프로그램을 작성하세요. 
단, 원소는 항상 ‘a’부터 시작하여 n개의 알파벳이라고 가정합니다.

입력 예시
4 2

출력 예시
ab
ac
ad
ba
bc
bd
ca
cb
cd
da
db
dc

힌트) 스켈레톤 코드에 주어진 함수만으로 해결하기 어렵다고 판단되면, 원하는 형태의 새로운 함수를 만들어 추가하는 것도 하나의 해결 방법입니다.
getPermutation(n, r) 이 부족하다고 생각되면 getPermInternal(buf, n, r)를 새롭게 정의해보세요.
'''
def getPermutation(n, r) :
    '''
    n개의 알파벳 중에서 r개를 뽑아 나열한 결과를 리스트로 반환합니다.

    예를 들어, n = 4, r = 2 일 경우에는
    
    ["ab", "ac", "ad", "ba", "bc", "bd", "ca", "cb", "cd", "da", "db", dc"] 를 반환합니다.
    '''

    result = []

    return result

def main():
    '''
    테스트를 하고싶으면, 아래 부분을 수정합니다.
    '''

    firstLine = [int(x) for x in input().split()]

    print('\n'.join(getPermutation(firstLine[0], firstLine[1])))

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

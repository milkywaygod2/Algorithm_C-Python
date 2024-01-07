'''
    연속부분최대합?..완전탐색보단 /2로 재귀해서 시간복잡도를 기적으로 줄이기 (계산의 중복 조합 줄이기, 컴퓨터는 무식하게 다계산)
    완전탐색법적용시, start,end 각각 n개의 선택지 * 선택된 start-end에서의 n가지 부분집합 선택지 = O(n^3)
    절반씩 나누고 예외를 보완해서 재귀를 돌리게되면, 2번의 log(n)에 대한 각각에 대한 n가지 부분집합 선택지 = O(2log(n)*n)       
    (말단스택이 1이 되는 2의 승수는 2^log(n)임, 상수는 생략 ==>nlog(n))
    1.절반씩 나눠서 재귀한다 + 기저조건고려. 
    2.걸친 경우 고려한다. 
    3.최종적으로 각 절반씩과 절친경우의 부분합을 비교한다. 
    = 왼쪽직전스택최대합 vs 오른쪽직전스택최대합 vs 현재스택최대합

    n개의 숫자가 list로 주어질 때, 그 연속 부분 최대합을 반환하는 함수를 작성하세요.
    1 2 -4 5 3 -2 9 -10 6 -8 7
    [1 2 -4 5 3] [-2 9 -10 6 -8 7]
    [[1 2] [-4 5 3]] [[-2 9 -10] [6 -8 7]]
    [[1] [2]/[-4] [5 3]] / [[-2] [9 -10] / [6] [-8 7]] 
    [[1] [2]/[-4] [5, 3]] / [[-2] [9, -10] / [6] [-8, 7]] 총11개 but결과적으로 말단스택원소는 무조건 1개

    반환값은 스택마다 업데이트되는 반환값일뿐 data[]수열 원본은 그대로임!
    [[1] [2]/[-4] ["8"]] / [[-2] ["9"] / [6] ["7"]]
    ["3"/"8"] / ["9"/"7"] 
    ["8"] / ["9"]
    ["15"]

    15
    '''

import sys

def getSubsum(data) :
    
# 1.기저조건 : 말단스택 규정    
    n = len(data)
    if n == 1:
        return data[0] #원소1개인 말단스택, 자기값 반환후 종결, 재귀스택은 말단스택까지 강요됨!

# 2.각각 왼쪽/오른쪽 한정, 최대부분합 재귀
    mid = n//2
    left = getSubsum(data[:mid]) #말단스택에서 원소1개를 반환
    right = getSubsum(data[mid:])
    
# 3.최대부분합이 왼쪽/오른쪽에 걸친 경우 (왼쪽최대후반합+오른쪽최대전반합)
    #모든 Sum은 'temp값', data[]원소에 영향X (스택이 아무리 돌아도 배열자체 영향X)
    #재귀스택의 부분합을 탐색(Sum)하는 범위는 기계적으로 2배씩 확장 
    back_leftSum = 0 #왼쪽 후반합
    front_rightSum = 0 #오른쪽 전반합
    temp_leftSum = 0 #왼쪽 최대후반합
    temp_rightSum = 0 #오른쪽 최대전반합
   
    for i in range(mid-1, -1, -1): # range(start,end,step): start~end직전까지 step간격, range(mid) == range(0,mid,1)랑 순서반대
        back_leftSum += data[i]
        temp_leftSum = max(back_leftSum,temp_leftSum) # 초기값 0보다 큰수로 -(왼쪽 최대후반합)

    for i in range(mid, n):
        front_rightSum += data[i]
        temp_rightSum = max(front_rightSum, temp_rightSum) # 초기값 0보다 큰수로 -(오른쪽 최대전반합)

    return max([left, right, temp_leftSum + temp_rightSum])
    #max([왼쪽최대부분합,오른최대부분합,왼쪽최대후반합+오른최대전반합])
    #max([a,b,c]) : 각 인자가 배열인 경우, 각 배열의 최대값을 인자로 하고 그 중 가장 큰 값을 반환
    

def main():
    '''
    이 부분은 수정하지 마세요.
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

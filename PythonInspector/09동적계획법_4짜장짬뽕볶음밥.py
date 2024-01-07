'''
탐욕적기법 vs 동적계획법
1.문제해결방식: 독립적 최선값 반복으로 최종값 결정 vs 하위문제결과를 상위에 반영하여 최종값 탐색
2.문제의 중복성: 독립사건으로 중복x vs 중복o 중복값재활용
3.최적해보장: 보장x vs 보장o

deliciousity(i,j) i번째날에 j음식먹었을때 최대선호합
deliciousity(i,j) = max(deliciousity(i-1,k)) + today(i,j) {k != j}

짜장, 짬뽕, 볶음밥
중식을 좋아하는 상훈이는 늘 점심엔 짜장, 짬뽕, 볶음밥 셋 중 하나를 먹어야 기분이 좋아진다
규칙이 하나 있는데, 전날 먹은 음식은 먹지 않는다는 것이다. 

각 날짜 별 음식의 선호도가 list로 주어질 때, 
선호도 총합의 최댓값을 반환하는 함수를 작성하세요.
첫 줄에는 며칠동안 먹을 것인지에 대한 정수(1≤n≤100,000)가 주어지고 
그 밑으로 각각 짜장, 짬뽕, 볶음밥에 대한 하루별 선호도가 주어진다.
선호도는 양의 정수만 들어온다고 가정한다.
3
27 8 35
18 36 10
7 22 45

116
'''

#점화식: d[i][j] = max(d[i-1][k])+data[i][j] (j!=k)
#총만족도[오늘][음식] = 최고값([어제][다른음식])+[오늘][음식]
#배열 3*days 안에 각 days별로 그날 j를 먹었을때 누적 총만족도 최대값을 저장(조합x결과만저장)
def eating(data) :
    days = len(data)
    d = [[0]*3 for i in range(days+1)] 
    #음식3개 날짜수만큼 배열만들고, 선호도가 입력값으로 들어감

    for i in range(1,days+1): #1☞ 모든날
        for j in range(3): #2☞ 오늘먹은음식
            for k in range(3): #어제먹은음식 
                if j == k: continue                
                #3☞ 어제까지의 d비교갱신by오늘선택: 오늘d[i-1][k] vs 어제d[i][j]  
                d[i][j] = max(d[i][j],d[i-1][k]) 
            d[i][j] += data[i-1][j] #4☞ 오늘선호도추가, i가 1부터 시작했음으로 인덱스0으로 조정

    return max(d[days][j] for j in range(3)) #5☞ 최대값(총만족도[마지막날][오늘음식])


import sys

def main():
    '''
    이 부분은 수정하지 마세요.
    '''

    n = int(input())

    data = []

    for i in range(n) :
        __line = [int(x) for x in input().split()]
        data.append(__line)

    print(eating(data))

if __name__ == "__main__":
    main()

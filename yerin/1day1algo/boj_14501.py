# 퇴사
import sys
# sys.stdin = open('input_14501.txt')

N = int(input())  # 상담 가능 기간
# T: 상담을 완료하는데 걸리는 기간 / P: 상담을 완료했을 때 받을 수 있는 금액
schedule = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# [[3, 10], [5, 20], [1, 10], [1, 20], [2, 15], [4, 40], [2, 200]]

dp = [0 for _ in range(N+1)]

for i in range(N):     # i 번째까지 일했을 때 얻는 최대 수익
    for j in range(i+schedule[i][0], N+1):  # i번째 날에 상담 진행했을 때, 상담이 가능한 모든 날짜 ~ 마지막 날
        if dp[j] < dp[i] + schedule[i][1]:  # 최대 수익 비교하여 갱신
            dp[j] = dp[i] + schedule[i][1]


print(dp)

print(dp[-1])


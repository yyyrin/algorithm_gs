# 계단 오르기

import sys
sys.stdin = open('input_2579.txt')

n = int(input())  # 계단의 개수

# 인덱스 1~n까지 점수 넣기
point = [0] + [int(input()) for _ in range(n)] + [0]

now = [0] * (n+2)
now[1] = point[1]
now[2] = point[1] + point[2]  # n=2일 때 최댓값

# 경우의 수 -> 2가지
#  [o x o o] vs [o o x o]
for i in range(3, n+1):
    now[i] = max(now[i-3]+point[i-1]+point[i], now[i-2]+point[i])

print(now[n])
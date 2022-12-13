# 스티커

import sys
sys.stdin = open('input_9465.txt')

T = int(input())
for i in range(1, T+1):
    n = int(input())  # 행 수
    arr = [list(map(int, input().split())) for _ in range(2)]

    print(n, arr)
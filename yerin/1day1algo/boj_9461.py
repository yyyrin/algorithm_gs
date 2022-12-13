# 파도반 수열

T = int(input())
for _ in range(T):
    N = int(input())
    arr = [0, 1, 1, 1, 2, 2]
    for i in range(6, N+1):
        arr.append(arr[i-1] + arr[i-5])
    print(arr[N])
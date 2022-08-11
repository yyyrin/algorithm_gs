<<<<<<< HEAD
'''
자연수 M과 N이 주어질 때 M이상 N이하의 자연수 중 소수인 것을 모두 골라 소수의 합과 최솟값을 찾는 프로그램
예를 들어 M=60, N=100인 경우 60이상 100이하의 자연수 중 소수는 61, 67, 71, 73, 79, 83, 89, 97 총 8개가 있으므로, 이들 소수의 합은 620이고, 최솟값은 61이 된다.
'''

M = int(input())
N = int(input())

primenum_list = []              # 소수 저장
for num in range(M, N+1):
    cnt = 0
    for i in range(2, num):     # num 이 소수인지 확인하기 위해 2 ~ num-1까지 모두 넣어서 체크
        if num % i == 0:        # 소수가 아니면 +1로  탈출
            cnt += 1             
            break
    
    if cnt == 0:                # cnt가 0 인 것만 소수이므로 추가
        primenum_list.append(num)

if len(primenum_list) == 0:     # 소수가 없으면 -1
    print('-1')
else:
    print(sum(primenum_list))
    print(min(primenum_list))

=======
M = int(input())
N = int(input())

primenum = []                       # 소수를 담는 리스트
for num in range(M, N+1):           
    cnt = 0                         # 소수와 소수가 아닌 수를 구분하기 위함
    if num > 1:                     # 소수 판별은 1보다 큰 수 부터
        for i in range(2, M+1):     # 2 ~ M 까지 나눠보자
            if num % i == 0:        # 소수가 아니면 cnt +1
                cnt += 1
                break               # 소수가 아닌 수를 계속 체크할 필요 X
        
        if cnt == 0:                
            primenum.append(num)

if len(primenum) > 0:
    print(sum(primenum))
    print(min(primenum))
else:
    print('-1')
>>>>>>> d6d9f2a994d8be296dee42e49be33222da328543

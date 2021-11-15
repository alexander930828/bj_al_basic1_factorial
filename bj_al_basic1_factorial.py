import math

n = int(input())
n_factorial = str(math.factorial(n))  # n!
cnt = 0

for i in range(len(n_factorial)-1, -1, -1): # n_factoral의 범위 부터 내림차순으로 -1씩
    if n_factorial[i] == '0': #만약 n_factorial[i] /  뒤에자리 부터 0이라면 cnt + 1
        cnt+=1
    else:
        break

print(cnt)
# 주소
# https://www.acmicpc.net/problem/3004

n = int(input())

if n % 2 != 0:
    n1 = n // 2 + 1
    n2 = n // 2 + 2
else:
    n1 = n // 2 + 1
    n2 = n // 2 + 1

print(n1 * n2)
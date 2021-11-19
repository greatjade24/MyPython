# 주소
# https://www.acmicpc.net/problem/4299

n, m = map(int, input().split())

a = (n + m) // 2
b = (n - m) // 2

if a + b != n or a - b != m or n < m:
    print(-1)
else:
    print(a, b)
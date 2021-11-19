# 주소
# https://www.acmicpc.net/problem/4299

n, m = map(int, input().split())

a = (n + m) // 2
b = (n - m) // 2

if a + b != n or a - b != m or n < m:   # n < m 조건을 추가하지 않으면 두 경기의 합이 차보다 작을 경우 -1을 출력하지 않는 반례가 생성됨
    print(-1)
else:
    print(a, b)
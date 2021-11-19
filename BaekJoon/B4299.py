# 주소
# https://www.acmicpc.net/problem/4299

# 두 경기의 합과 차를 입력
n, m = map(int, input().split())

# 연립방정식을 이용해 두 팀의 점수 구하기
a = (n + m) // 2
b = (n - m) // 2

# 역산으로 논리적으로 맞는 합과 차가 주어졌는지 확인
if a + b != n or a - b != m or n < m:   # n < m 조건을 추가하지 않으면 두 경기의 합이 차보다 작을 경우 -1을 출력하지 않는 반례가 생성됨
    print(-1)
else:
    print(a, b)
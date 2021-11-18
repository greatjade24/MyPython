h, m, s = map(int,input().split())
d = int(input())

s1 = (s + d) % 60  #최종 초
m1 = (s + d) // 60

m2 = (m + m1) % 60 # 최종 분
h1 = (m + m1) // 60

h2 = (h + h1) % 24 # 최종 시각

print(h2, m2, s1)
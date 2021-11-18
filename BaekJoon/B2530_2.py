h, m, s = map(int, input().split())
d = int(input())

s += d
if s >= 60:
    m += s // 60
    cS = s % 60
    s = 0
    s = cS
    if m >= 60:
        h += m // 60
        cM = m % 60
        m = 0
        m = cM
        if h >= 24:
            h %= 24    # h -= 24로 하면 h가 48 이상일때 결과값이 24가 넘는 반례가 나옴

print(h, m, s)
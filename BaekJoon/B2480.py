n1, n2, n3 = map(int, input().split())

if n1 == n2 == n3:
    print(10000 + (n1 * 1000))
elif n1 == n2 or n1 == n3 or n2 == n3:
    if n1 == n2:
        print(1000 + (n1 * 100))
    if n1 == n3:
        print(1000 + (n1 * 100))
    if n2 == n3:
        print(1000 + (n2 * 100))
else:
    num = [n1, n2, n3]
    num.sort()
    print(num[-1] * 100)

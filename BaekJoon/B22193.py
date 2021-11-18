while(True):
    n, m = map(int, input().split())
    a = input()
    b = input()

    if len(a) > n or len(b) > m:
        continue
    else:
        print(int(a) * int(b))
        break
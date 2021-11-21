# 주소
# https://www.acmicpc.net/problem/5532

l = int(input())
a = int(input())
b = int(input())
c = int(input())
d = int(input())

# 총 페이지 수가 하루 할 수 있는 페이지 수로 딱 나눠졌을때 +1 해버리는걸 방지
if a % c != 0:
    spendA = a // c + 1
else:
    spendA = a // c
if b % d != 0:
    spendB = b // d + 1 
else:
    spendB = b // d 

# 국어와 수학 방학숙제 소요일 중 큰 값을 구하기 위해 정렬
spend = [spendA, spendB]
spend.sort()

# 총 일자에서 국어와 수학 중 더 큰 소요일을 뺌
print(l - spend[1])

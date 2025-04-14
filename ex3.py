N = int(input())

for i in range(N // 2, 1, -1):
    if N % i == 0:
        print(i)
        break

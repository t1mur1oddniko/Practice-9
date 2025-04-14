def count_stairs(n, max_step):
    if n == 0:
        return 1
    if n < 0 or max_step == 0:
        return 0
    return count_stairs(n, max_step - 1) + count_stairs(n - max_step, max_step - 1)

N = int(input())
print(count_stairs(N, N - 1))

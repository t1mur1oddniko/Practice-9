from itertools import permutations
k = 'SENDMORY'

for letters in permutations(range(10), len(k)):
    S, E, N, D, M, O, R, Y = letters
    if S == 0 or M == 0:
        continue

    SEND = 1000 * S + 100 * E + 10 * N + D
    MORE = 1000 * M + 100 * O + 10 * R + E
    MONEY = 10000 * M + 1000 * O + 100 * N + 10 * E + Y

    if SEND + MORE == MONEY:
        print(f'SEND: {SEND}')
        print(f'MORE: {MORE}')
        print(f'MONEY: {MONEY}')

# 68645: 삼각 달팽이

def solution(n):
    answer = []
    snail = [[0] * _ for _ in range(1, n + 1)]
    num = 1
    i, j = 0, 0

    def down(times, i, j, num):
        for t in range(times):
            if not snail[i][j]:
                snail[i][j] = num
                num += 1
                i += 1
        i -= 1
        return i, num

    def forward(times, i, j, num):
        for t in range(times):
            j += 1
            if not snail[i][j]:
                snail[i][j] = num
                num += 1
        j -= 1
        return j, num

    def up(times, i, j, num):
        for t in range(times):
            i -= 1
            if not snail[i][j]:
                snail[i][j] = num
                num += 1
                j -= 1
        i += 1
        j += 1
        return i, j, num

    k = 0

    for l in range(n, 0, -1):
        if k % 3 == 0:
            i, num = down(l, i, j, num)
            print(snail)
            print(f"i:{i}, j:{j}, num:{num}")
        elif k % 3 == 1:
            j, num = forward(l, i, j, num)
            print(snail)
            print(f"i:{i}, j:{j}, num:{num}")
        else:
            i, j, num = up(l, i, j, num)
            print(snail)
            print(f"i:{i}, j:{j}, num:{num}")
        k += 1

    for row in snail:
        for x in row:
            answer.append(x)

    return answer
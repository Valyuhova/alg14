from typing import List, Tuple

PRIZES_TOP: List[List[int]] = [
    [4, -1,  5,  5, -1, -2,  5,  8],
    [-1, 2, -2, -1,  6,  2, -3,  2],
    [3, -1,  6,  4, -1,  3, -1,  4],
    [1, -2,  5,  3,  3, -4, -4,  7],
    [-1, 3, -1,  4, -4,  2, -2, -3],
    [-3, -2, -1, -5,  3,  1, -3, -2],
    [-1, -2, -3,  4, -1,  2, -1, -4],
    [3, -1, -2, -3, -2, -1,  4,  3],
]


def solve_max_prize(prizes_top: List[List[int]]) -> None:
    n = len(prizes_top)

    board = list(reversed(prizes_top))

    NEG_INF = -10**9

    dp = [[NEG_INF] * n for _ in range(n)]
    parent: List[List[Tuple[int, int] | None]] = [[None] * n for _ in range(n)]

    dp[0][0] = board[0][0]

    for i in range(n):
        for j in range(n):
            if i == 0 and j == 0:
                continue

            best = NEG_INF
            prev = None

            for di, dj in [(-1, 0), (0, -1), (-1, -1)]:
                pi, pj = i + di, j + dj
                if 0 <= pi < n and 0 <= pj < n:
                    if dp[pi][pj] > best:
                        best = dp[pi][pj]
                        prev = (pi, pj)

            dp[i][j] = board[i][j] + best
            parent[i][j] = prev

    max_prize = dp[n - 1][n - 1]

    path_cells: List[Tuple[int, int]] = []
    i = j = n - 1
    while True:
        path_cells.append((i, j))
        if (i, j) == (0, 0):
            break
        i, j = parent[i][j]
    path_cells.reverse()

    human_path = [(i + 1, j + 1) for (i, j) in path_cells]
    path_values = [board[i][j] for (i, j) in path_cells]

    print("Матриця призів P(i, j):")
    for row in prizes_top:
        print(" ".join(f"{v:3d}" for v in row))

    print("\nМаксимальний можливий приз мандрівника:", max_prize)
    print("Довжина шляху (кількість клітинок):", len(human_path))
    print("Шлях (рядок, стовпчик) з нижнього лівого кута:")
    print(" -> ".join(f"({r},{c})" for (r, c) in human_path))

    print("\nПризи вздовж цього шляху:")
    print(" + ".join(str(v) for v in path_values), "=", sum(path_values))

    print("\nМатриця F(i, j) – максимальний приз від (0,0) до (i, j):")
    for i in reversed(range(n)):
        print(" ".join(f"{dp[i][j]:3d}" for j in range(n)))


if __name__ == "__main__":
    solve_max_prize(PRIZES_TOP)
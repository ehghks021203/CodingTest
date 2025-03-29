# 15649. N과 M (1)
from itertools import permutations

def solution(n: int, m: int) -> None:
    nums = list(range(1, n + 1))
    for line in permutations(nums, m):
        for n in line:
            print(n, end=" ")
        print()

if __name__ == "__main__":
    N, M = map(int, input().split())
    solution(N, M)

# (PyPy3) Result: 111808KB / 120ms
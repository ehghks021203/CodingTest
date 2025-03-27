# 15650. N과 M (2)
from itertools import permutations

def solution(N: int, M: int) -> None:
    results = permutations(list(range(1, N+1)))
    for result in results:
        print(result)
        #print(" ".join(result))

if __name__ == "__main__":
    N, M = map(int, input().split())
    solution(N, M)
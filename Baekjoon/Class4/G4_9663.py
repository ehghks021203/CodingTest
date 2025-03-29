# 9663. N-Queen
import sys
input = sys.stdin.readline

def solution(n: int, check: dict, row: int = 0) -> int:
    if n == row:
        return 1
    count = 0
    for col in range(n):
        # 놓을 수 있는 공간에 말 놓기
        if check["c"][col] and check["u"][row+col] and check["d"][row-col+n-1]:
            check["c"][col] = check["u"][row+col] = check["d"][row-col+n-1] = False
            count += solution(n, check, row + 1)
            check["c"][col] = check["u"][row+col] = check["d"][row-col+n-1] = True
    return count

if __name__ == "__main__":
    N = int(input())
    check = {
        "c": [True]*N,
        "u": [True]*(N*2),
        "d": [True]*(N*2),
    }
    print(solution(N, check))
    
# (PyPy3) Result: 121200KB / 13152ms
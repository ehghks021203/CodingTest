# 11444. 피보나치 수 6
import sys
input = sys.stdin.readline

MOD = 1_000_000_007

def solution(n: int):
    F = [[1, 1], [1, 0]]
    return power(F, n-1)[0][0] % 1_000_000_007

def power(F: list, n: int) -> list:
    if n == 0:
        return [[1, 0], [0, 1]]
    temp = power(F, n//2)
    result = multi(temp, temp)
    if n % 2 == 1:
        return multi(F, result)
    else: 
        return result

def multi(A: list, B: list) -> list:
    global MOD
    a = ((A[0][0] % MOD) * (B[0][0] % MOD) + (A[0][1] % MOD) * (B[1][0] % MOD)) % MOD
    b = ((A[0][0] % MOD) * (B[0][1] % MOD) + (A[0][1] % MOD) * (B[1][1] % MOD)) % MOD
    c = ((A[1][0] % MOD) * (B[0][0] % MOD) + (A[1][1] % MOD) * (B[1][0] % MOD)) % MOD
    d = ((A[1][0] % MOD) * (B[0][1] % MOD) + (A[1][1] % MOD) * (B[1][1] % MOD)) % MOD
    return [[a, b], [c, d]]

if __name__ == "__main__":
    n = int(input())
    print(solution(n))

# (PyPy3) Result: 108384KB / 96ms
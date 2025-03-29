# 2438. 별 찍기 - 1

def solution(n: int) -> str:
    result = ""
    for i in range(1, n + 1):
        result += "*"*i + "\n"
    return result

if __name__ == "__main__":
    N = int(input())
    print(solution(N))

# (PyPy3) Result: 108384KB / 88ms
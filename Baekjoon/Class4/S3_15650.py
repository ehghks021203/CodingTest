# 15650. N과 M (2)

def solution(num_list: list, n: int, index: int = 0, result: list = []) -> None:
    if n == index:
        print(" ".join(map(str, result)))
        return
    for num in num_list:
        result.append(num)
        solution(list(range(num+1, N+1)), n, index+1, result)
        result.pop()

if __name__ == "__main__":
    N, M = map(int, input().split())
    solution(list(range(1, N+1)), M)

# (PyPy3) Result: 108384KB / 92ms
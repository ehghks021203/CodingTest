# 2675. 문자열 반복

def solution(string: str, repeat: int) -> str:
    return "".join([s*repeat for s in string])

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        R, S = map(str, input().split())
        print(solution(S, int(R)))

# (PyPy3) Result: 108383KB / 88ms
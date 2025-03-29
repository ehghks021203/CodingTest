# 9935. 문자열 폭발

def solution(str: str, boom: str) -> str:
    stack = []
    for s in str:
        stack.append(s)
        if len(stack) >= len(boom):
            if "".join(stack[-len(boom):]) == boom:
                del stack[-len(boom):]
    if len(stack) == 0:
        return "FRULA"
    return "".join(stack)

if __name__ == "__main__":
    str = input()
    boom = input()
    print(solution(str, boom))

# (PyPy3) Result: 181932KB / 492ms
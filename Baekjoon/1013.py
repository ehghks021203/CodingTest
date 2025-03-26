# 1013. Contact
import re

def solution(pattern: str) -> str:
    # pattern: (100+1+ | 01)+
    if pattern == "":
        return "NO"
    while True:
        find_pattern = re.search(r"100+1+", pattern)
        if pattern == "":
            return "YES"
        if find_pattern:
            s, e = find_pattern.span(0)
            # 100*1*이 연속으로 나올 때
            if pattern[e-1] == pattern[e-2] and len(pattern) >= e + 2:
                if re.match(r"00+1", pattern[e:]):
                    e -= 1
            if re.sub(r"(01)+", "", pattern[:s]) != "":
                return "NO"
            else:
                pattern = pattern[e:]
        else:
            if re.sub(r"(01)+", "", pattern) != "":
                return "NO"
            else:
                return "YES"

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        pattern = input()
        print(solution(pattern))

# Result: 37024KB / 164ms
# 10814. 나이순 정렬
from sys import stdin, stdout

def solution(users: list) -> None:
	return sorted(users, key=lambda x: int(x[0]))

if __name__ == "__main__":
	N = int(stdin.readline())
	users = []
	for _ in range(N): 
		users.append(list(map(str, stdin.readline().split())))
	stdout.write("\n".join(" ".join(map(str, x)) for x in solution(users)) + "\n")

# (PyPy3) Result: 135796KB / 252ms
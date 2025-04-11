# 4134. 다음 소수
from sys import stdin, stdout

def solution(n: int) -> int:
	if n <= 1: n = 2
	while True:
		is_prime = True
		for i in range(2, int(n ** 0.5) + 1):
			if n % i == 0: 
				is_prime = False
				break
		if is_prime: return n
		n += 1

if __name__ == "__main__":
	T = int(stdin.readline().rstrip())
	for _ in range(T): stdout.write(f"{solution(int(stdin.readline().rstrip()))}\n")

# (PyPy3) Result: 110576KB / 388ms
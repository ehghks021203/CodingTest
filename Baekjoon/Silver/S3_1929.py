# 1929. 소수 구하기
from sys import stdin, stdout

def solution(m: int, n: int) -> list:
	prime = []
	for num in range(m, n + 1):
		if num == 1: continue
		is_prime = True
		for i in range(2, int(num ** 0.5) + 1):
			if num % i == 0: 
				is_prime = False
				break
		if is_prime: prime.append(num)
	return prime

if __name__ == "__main__":
	M, N = map(int, stdin.readline().split())
	stdout.write("\n".join(map(str, solution(M, N))) + "\n")

# (PyPy3) Result: 114732KB / 800ms
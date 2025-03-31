# 3344. N-Queen

def solution(n: int):
	if n % 6 == 3:
		for i in range(4, n + 1, 2):
			print(i)
		print(2)
		for i in range(5, n + 1, 2):
			print(i)
		print(1)
		print(3)
	else:
		for i in range(2, n + 1, 2):
			print(i)
		if n % 6 == 2:
			print(3)
			print(1)
			for i in range(7, n + 1, 2):
				print(i)
			print(5)
		else:
			for i in range(1, n + 1, 2):
				print(i)

if __name__ == "__main__":
	N = int(input())
	solution(N)

# (PyPy3) Result: 110900KB / 112ms
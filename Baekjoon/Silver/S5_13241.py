# 13241. 최소공배수
from sys import stdin, stdout
from math import lcm

def solution(num1: int, num2: int) -> int:
	return lcm(num1, num2)

if __name__ == "__main__":
	A, B = map(int, stdin.readline().split())
	stdout.write(f"{solution(A, B)}\n")

# (PyPy3) Result: 108384KB / 88ms
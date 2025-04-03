# 2609. 최대공약수와 최소공배수

def gcd(n1: int, n2: int) -> int:
	if n2 == 0: return n1
	return gcd(n2, n1 % n2)

def lcm(n1: int, n2: int) -> int:
	return n1 * n2 // gcd(n1, n2)

def solution(n1: int, n2: int) -> tuple:
	return gcd(n1, n2), lcm(n1, n2)

if __name__ == "__main__":
	num1, num2 = map(int, input().split())
	gcd_value, lcm_value = solution(num1, num2)
	print(gcd_value)
	print(lcm_value)

# (PyPy3) Result: 108384KB / 88ms
# NOTE: math 라이브러리의 gcd, lcm을 사용해도 됨.
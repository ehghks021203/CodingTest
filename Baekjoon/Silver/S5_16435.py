# 16435. 스네이크버드

def solution(height: int, fruits: list) -> int:
	fruits.sort()
	for fruit in fruits:
		if fruit <= height:
			height += 1
		else:
			break
	return height

if __name__ == "__main__":
	N, L = map(int, input().split())
	fruits = list(map(int, input().split()))
	print(solution(L, fruits))

# (PyPy3) Result: 108384KB / 92ms
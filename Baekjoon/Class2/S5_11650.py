# 11650. 좌표 정렬하기

def solution(coordinate: list) -> list:
	return sorted(coordinate, key=lambda x: (x[0], x[1]))

if __name__ == "__main__":
	N = int(input())
	coordinate = []
	for _ in range(N): coordinate.append(list(map(int, input().split())))
	print("\n".join(" ".join(map(str, x)) for x in solution(coordinate)))

# (PyPy3) Result: 137056KB / 396ms
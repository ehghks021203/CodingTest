# 2166. 다각형의 면적

def solution(polygon: list) -> float:
	p = list(polygon)
	p.append(polygon[0])
	sum1 = sum2 = 0
	for i in range(len(polygon)):
		sum1 += p[i][0] * p[i+1][1]
		sum2 += p[i+1][0] * p[i][1]
	return round(0.5 * abs(sum1 - sum2), 1)

if __name__ == "__main__":
	N = int(input())
	polygon = []
	for _ in range(N): polygon.append(list(map(int, input().split())))
	print(solution(polygon))

# (PyPy3) Result: 111412KB / 116ms
# NOTE: 신발끈 정리
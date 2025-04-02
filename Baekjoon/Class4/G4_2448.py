# 2448. 별 찍기 - 11

def merge(s1: list, s2: list, s3: list, n: int) -> list:
	result = []
	for i in range(len(s1)):
		result.append([" " * (n // 2) + s1[i][0] + " " * (n // 2), " " * (n // 2) + s1[i][1] + " " * (n // 2), " " * (n // 2) + s1[i][2] + " " * (n // 2)])
	for i in range(len(s2)):
		result.append([s2[i][0] + " " + s3[i][0], s2[i][1] + " " + s3[i][1], s2[i][2] + " " + s3[i][2]])
	return result

def solution(n: int) -> None:
	if n == 3:
		return [["  *  ", " * * ", "*****"]]
	else:
		return merge(solution(n // 2), solution(n // 2), solution(n // 2), n)

if __name__ == "__main__":
	N = int(input())
	for star in solution(N):
		for line in star:
			print(line)

# (PyPy3) Result: 161824KB / 300ms
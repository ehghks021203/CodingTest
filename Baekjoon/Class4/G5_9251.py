# 9251. LCS
import sys

def solution(s1: str, s2: str) -> int:
	count_list = [[0 for _ in range(len(s2))] for _ in range(len(s1))]
	for i in range(1, len(s1)):
		for j in range(1, len(s2)):
			count_list[i][j] = count_list[i-1][j-1]
			if s1[i - 1] == s2[j - 1]:
				count_list[i][j] += 1
			else:
				count_list[i][j] = max(count_list[i-1][j], count_list[i][j-1])
	return count_list[-1][-1]

if __name__ == "__main__":
	s1 = sys.stdin.readline()
	s2 = sys.stdin.readline()
	sys.stdout.write(str(solution(s1, s2)))

# (PyPy3) Result: 118584KB / 128ms
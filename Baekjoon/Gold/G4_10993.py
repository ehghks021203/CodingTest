# 10993. 별 찍기 - 18

def make_triangle(n: int) -> list:
	lines = 1 + 2**n - 2
	cols = lines * 2 - 1
	triangle = [[" " for _ in range(cols)] for _ in range(lines)]
	for i in range(lines):
		# 짝수면 역삼각형
		if n % 2 == 0:
			if i == 0:
				triangle[0] = ["*" for _ in range(cols)]
			else:
				triangle[i][i] = "*"
				triangle[i][-i - 1] = "*"
		# 홀수면 일반삼각형
		else:
			if i == lines - 1:
				triangle[-1] = ["*" for _ in range(cols)]
			else:
				triangle[i][cols // 2 - i] = "*"
				triangle[i][cols // 2 + i] = "*"
	return triangle

def merge(b_tri: list, s_tri: list, is_inverted: bool = False) -> list:
	# 두 개의 삼각형 합치기
	b_lines = len(b_tri)		# 큰 삼각형 y 길이
	b_cols = b_lines * 2 - 1	# 큰 삼각형 x 길이
	s_lines = len(s_tri)		# 작은 삼각형 y 길이
	s_cols = s_lines * 2 - 1	# 작은 삼각형 x 길이
	stt_x_offset = b_cols // 2 - s_cols // 2	# x 시작 위치 설정
	end_x_offset = b_cols // 2 + s_cols // 2	# x 종료 위치 설정
	# y 시작 위치 및 종료 위치 설정 (역삼각형인지 아닌지에 따라 오프셋 위치 바뀜)
	if is_inverted:
		stt_y_offset = 1
		end_y_offset = b_lines // 2 + 1
	else:
		stt_y_offset = b_lines // 2
		end_y_offset = b_lines - 1
	
	# 삼각형 병합 시작
	for y in range(stt_y_offset, end_y_offset):
		b_tri[y][stt_x_offset:end_x_offset + 1] = s_tri[y - stt_y_offset]
	return b_tri

def solution(n: int) -> None:
	if n == 1:
		return make_triangle(1)
	if n % 2 == 0:
		return merge(make_triangle(n), solution(n - 1), is_inverted=True)
	else:
		return merge(make_triangle(n), solution(n - 1))

if __name__ == "__main__":
	N = int(input())
	print("\n".join("".join(map(str, x)).rstrip() for x in solution(N)))

# (PyPy3) Result: 132196KB / 156ms
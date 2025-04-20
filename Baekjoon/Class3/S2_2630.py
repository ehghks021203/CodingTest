# 2630. 색종이 만들기

def check_same_color(paper: list) -> tuple:
	return sum(paper) == 0, sum(paper) == len(paper)

def div_paper(paper: list) -> list:
	n = int(len(paper) ** 0.5)
	half = n // 2
	p1 = []
	p2 = []
	p3 = []
	p4 = []
	idx = 0
	for _ in range(half ** 2):
		p1.append(paper[idx])
		p2.append(paper[idx + half])
		p3.append(paper[idx + n * half])
		p4.append(paper[idx + half + n * half])
		idx += 1
		if idx % half == 0: idx += half
	return p1, p2, p3, p4

def solution(paper: list, white: int = 0, blue: int = 0) -> tuple:
	is_white, is_blue = check_same_color(paper)
	if is_white: return white + 1, blue
	elif is_blue: return white, blue + 1
	else:
		p1, p2, p3, p4 = div_paper(paper)
		white, blue = solution(p1, white, blue)
		white, blue = solution(p2, white, blue)
		white, blue = solution(p3, white, blue)
		white, blue = solution(p4, white, blue)
	return white, blue

if __name__ == "__main__":
	N = int(input())
	paper = []
	for _ in range(N): paper += list(map(int, input().split())) 
	white, blue = solution(paper)
	print(f"{white}\n{blue}")

# (PyPy3) Result: 111764KB / 136ms
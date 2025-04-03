# 4153. 직각삼각형

def solution(w: int, h: int, r: int) -> bool:
	if w ** 2 + h ** 2 == r ** 2:
		return True
	if r ** 2 + h ** 2 == w ** 2:
		return True
	if w ** 2 + r ** 2 == h ** 2:
		return True
	else:
		return False

if __name__ == "__main__":
	while True:
		w, h, r = map(int, input().split())
		if w == h == r == 0:
			break
		if solution(w, h, r):
			print("right")
		else:
			print("wrong")

# (PyPy3) Result: 108384KB / 84ms
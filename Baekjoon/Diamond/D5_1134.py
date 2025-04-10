# 1134. 식

max_a, max_b, max_c = (-1, -1, -1)

def restore_equation(exp: list):
	# 수식 복원
	A, B, C = ([], [], [])
	for digit in range(len(exp) -1, -1, -1):
		A.append(exp[digit][0])
		B.append(exp[digit][1])
		C.append(exp[digit][2])
	if -1 in A or -1 in B or -1 in C:
		return -1, -1, -1
	return int("".join(map(str, A))), int("".join(map(str, B))), int("".join(map(str, C)))

def calc_exp(exp: list, nd: list, digit: int, carry: int = 0):
	global max_a, max_b, max_c
	a, b, c = tuple(exp[digit])
	if digit < 0:
		if carry == 0: 
			A, B, C = restore_equation(exp)
			if max_c < C or (max_c == C and max_a < A):
				max_a, max_b, max_c = (A, B, C)
			return
		return
	for k in [0, 1]:
		# no question mark
		if a != -1 and b != -1 and c != -1:
			if (a + b + k) % 10 == c and (a + b + k) // 10 == carry: 
				calc_exp(exp, nd, digit - 1, k)
		# one question mark
		if a != -1 and b != -1 and c == -1:
			if (a + b + k) // 10 == carry:
				if (a + b + k) % 10 == 0 and nd[2] == digit: continue
				exp[digit][2] = (a + b + k) % 10
				calc_exp(exp, nd, digit - 1, k)
				exp[digit][2] = -1
		if a != -1 and b == -1 and c != -1:
			if a + k <= c and carry == 0: tmp = 0
			elif a + k > c and carry == 1: tmp = 10
			else: continue
			if c - a - k + tmp == 0 and nd[1] == digit: continue
			exp[digit][1] = c - a - k + tmp
			calc_exp(exp, nd, digit - 1, k)
			exp[digit][1] = -1
		if a == -1 and b != -1 and c != -1:
			if b + k <= c and carry == 0: tmp = 0
			elif b + k > c and carry == 1: tmp = 10
			else: continue
			if c - b - k + tmp == 0 and nd[0] == digit: continue
			exp[digit][0] = c - b - k + tmp
			calc_exp(exp, nd, digit - 1, k)
			exp[digit][0] = -1
		# two question mark
		if a == -1 and b == -1 and c != -1:
			if carry == 1:
				if c == 9:
					exp[digit][0] = 9
					exp[digit][1] = 9
					k = 1
				if nd[1] == digit and (c - 9 - k) % 10 == 0: 
					exp[digit][0] = 8
					exp[digit][1] = (c - 8 - k + 10) % 10
				else: 
					exp[digit][0] = 9
					exp[digit][1] = (c - 9 - k + 10) % 10
			else:
				if nd[1] == digit and c - 1 < 0: continue
				if nd[1] != digit: exp[digit][1] = 0
				else: exp[digit][1] = 1
				exp[digit][0] = c - exp[digit][1] - k
			calc_exp(exp, nd, digit - 1, k)
			exp[digit][0] = -1
			exp[digit][1] = -1
		if a == -1 and b != -1 and c == -1:
			if carry == 1:
				if (9 + b + k) // 10 != carry: continue
				exp[digit][0] = 9
				exp[digit][2] = (9 + b + k) % 10
			if carry == 0:
				if 9 - b - k < 0: continue
				if nd[0] == digit and 9 - b - k == 0: continue
				exp[digit][0] = (9 - b - k + 10) % 10
				exp[digit][2] = 9
			calc_exp(exp, nd, digit - 1, k)
			exp[digit][0] = -1
			exp[digit][2] = -1
		if a != -1 and b == -1 and c == -1:
			if carry == 1:
				if (9 + a + k) // 10 != carry: continue
				exp[digit][1] = 9
				exp[digit][2] = (9 + a + k) % 10
			else:
				if 9 - a - k < 0: continue
				if nd[1] == digit and 9 - a - k == 0: continue
				exp[digit][1] = (9 - a - k + 10) % 10
				exp[digit][2] = 9
			calc_exp(exp, nd, digit - 1, k)
			exp[digit][1] = -1
			exp[digit][2] = -1
		# three question mark
		if a == -1 and b == -1 and c == -1:
			if carry == 1:
				exp[digit][0] = 9
				exp[digit][1] = 9
				exp[digit][2] = (18 + k) % 10
				calc_exp(exp, nd, digit - 1, k)
				exp[digit][0] = -1
				exp[digit][1] = -1
				exp[digit][2] = -1
			else:
				if nd[1] == digit:
					exp[digit][0] = 8 - k
					exp[digit][1] = 1
					exp[digit][2] = 9
				else:
					exp[digit][0] = 9 - k
					exp[digit][1] = 0
					exp[digit][2] = 9
				calc_exp(exp, nd, digit - 1, k)
				exp[digit][0] = -1
				exp[digit][1] = -1
				exp[digit][2] = -1
	return

def solution(exp: str) -> str:
	global max_a, max_b, max_c
	A = list(exp.split("+")[0][::-1])
	B = list(exp.split("+")[1].split("=")[0][::-1])
	C = list(exp.split("=")[1][::-1])
	# 자리수별 숫자 분해
	exp_num = []
	# C보다 A, B의 자리수가 클 경우 -1 반환
	if len(A) > len(C) or len(B) > len(C): return "-1"
	for i in range(len(C)):
		if C[i] == "?": exp_num.append([0, 0, -1])
		else: exp_num.append([0, 0, int(C[i])])
	for i in range(len(A)):
		if A[i] == "?": exp_num[i][0] = -1
		else: exp_num[i][0] = int(A[i])
	for i in range(len(B)):
		if B[i] == "?": exp_num[i][1] = -1
		else: exp_num[i][1] = int(B[i])
	# C를 최대로 하는 값 찾기
	ad = -1 if len(A) == 1 else len(A) - 1
	bd = -1 if len(B) == 1 else len(B) - 1
	cd = -1 if len(C) == 1 else len(C) - 1
	calc_exp(exp_num, [ad, bd, cd], len(C)-1)
	if max_a == max_b == max_c == -1:
		return "-1"
	return f"{max_a}+{max_b}={max_c}"

if __name__ == "__main__":
	exp = input()
	print(solution(exp))

# (PyPy3) Result: 114820KB / 300ms
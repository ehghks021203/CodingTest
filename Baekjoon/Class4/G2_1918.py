# 1918. 후위 표기식

def calc_priority(op: str) -> int:
	if op in ["+", "-"]: return 1
	if op in ["*", "/"]: return 2
	if op in ["("]: return 3

def solution(exp: str) -> str:
	exp_stack = list(exp)
	pn_stack = []
	postfix = ""
	cursor = 0
	while True:
		if cursor >= len(exp_stack):
			while True:
				if len(pn_stack) == 0: 
					break
				if pn_stack[-1] in ["(", ")"]:
					pn_stack.pop()
				else:
					postfix += pn_stack.pop()
			break
		if exp_stack[cursor] in ["+", "-", "*", "/", "(", ")"]:
			if len(pn_stack) == 0: 
				pn_stack.append(exp_stack[cursor])
			elif pn_stack[-1] == "(":
				pn_stack.append(exp_stack[cursor])
			elif exp_stack[cursor] == ")":
				while True:
					if len(pn_stack) == 0: 
						break
					if pn_stack[-1] == "(":
						pn_stack.pop()
						break
					postfix += pn_stack.pop()
			elif calc_priority(pn_stack[-1]) < calc_priority(exp_stack[cursor]):
				pn_stack.append(exp_stack[cursor])
			else:
				while True:
					if len(pn_stack) == 0: 
						break
					if pn_stack[-1] == "(":
						break
					if calc_priority(pn_stack[-1]) >= calc_priority(exp_stack[cursor]):
						postfix += pn_stack.pop()
					else: 
						break
				pn_stack.append(exp_stack[cursor])
		else:
			postfix += exp_stack[cursor]
		cursor += 1
	return postfix.replace("(", "").replace(")", "")

if __name__ == "__main__":
	exp = input()
	print(solution(exp))

# (PyPy3) Result: 108384KB / 100ms
# NOTE: 어거지로 푼거라 다시 풀어봐야할듯
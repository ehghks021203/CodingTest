# 2920. 음계

def solution(seq: list) -> str:
	is_ascending = is_descending = False
	for i in range(1, len(seq)):
		if seq[i - 1] < seq[i]: is_ascending = True
		if seq[i - 1] > seq[i]: is_descending = True
	if is_ascending and is_descending: return "mixed"
	if is_ascending: return "ascending"
	if is_descending: return "descending"

if __name__ == "__main__":
	print(solution(list(map(int, input().split()))))

# (PyPy3) Result: 108384KB / 88ms
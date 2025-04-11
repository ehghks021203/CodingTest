# 1620. 나는야 포켓몬 마스터 이다솜
from sys import stdin, stdout

def solution(n: int, m: int) -> None:
	poke_n_dict = {}
	poke_i_dict = {}
	for i in range(1, N + 1):
		name = stdin.readline()[:-1]
		poke_n_dict[name] = int(i)
		poke_i_dict[int(i)] = name
	for _ in range(M):
		req = stdin.readline()[:-1]
		if req.isdigit(): stdout.write(f"{poke_i_dict[int(req)]}\n")
		else: stdout.write(f"{poke_n_dict[req]}\n")

if __name__ == "__main__":
	N, M = map(int, stdin.readline().split())
	solution(N, M)

# (PyPy3) Result: 140356KB / 248ms
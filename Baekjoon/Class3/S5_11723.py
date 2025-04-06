# 11723. 집합
from sys import stdin, stdout

class Set():
	def __init__(self):
		self.empty()
	
	def add(self, x: int) -> None:
		self.S |= (1 << x)
	
	def remove(self, x: int) -> None:
		self.S &= ~(1 << x)
	
	def check(self, x: int) -> int:
		stdout.write("1\n") if self.S & (1 << x) else stdout.write("0\n")
	
	def toggle(self, x: int) -> None:
		self.S ^= (1 << x)

	def all(self) -> None:
		self.S = (1 << 21) - 1
	
	def empty(self) -> None:
		self.S = 0

def solution(s: Set, command: str) -> None:
	cmd = command.split(" ")
	if cmd[0] == "add":
		s.add(int(cmd[1]))
	elif cmd[0] == "remove":
		s.remove(int(cmd[1]))
	elif cmd[0] == "check":
		s.check(int(cmd[1]))
	elif cmd[0] == "toggle":
		s.toggle(int(cmd[1]))
	elif cmd[0] == "all\n":
		s.all()
	elif cmd[0] == "empty\n":
		s.empty()

if __name__ == "__main__":
	M = int(stdin.readline())
	s = Set()
	for _ in range(M): solution(s, stdin.readline())

# (PyPy3) Result: 118824KB / 928ms
# 비트마스킹으로 효율적으로 구현 가능

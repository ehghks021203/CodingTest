# 10828. 스택

class Stack():
	def __init__(self):
		self.data = []
	
	def push(self, x: int) -> int:
		self.data.append(x)
	
	def pop(self) -> int:
		if self.empty():
			return - 1
		else:
			return self.data.pop()
	
	def size(self) -> int:
		return len(self.data)
	
	def empty(self) -> int:
		return 1 if len(self.data) == 0 else 0
	
	def top(self) -> int:
		if self.empty():
			return -1
		else:
			return self.data[-1]

def solution(command: str, queue: Stack) -> int:
	cmd = command.split(" ")
	if cmd[0] == "push":
		queue.push(int(cmd[1]))
	elif cmd[0] == "pop":
		print(queue.pop())
	elif cmd[0] == "size":
		print(queue.size())
	elif cmd[0] == "empty":
		print(queue.empty())
	elif cmd[0] == "top":
		print(queue.top())

if __name__ == "__main__":
	N = int(input())
	stack = Stack()
	[solution(input(), stack) for _ in range(N)]

# (PyPy3) Result: 112248KB / 428ms
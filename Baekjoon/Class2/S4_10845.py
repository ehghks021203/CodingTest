# 10845. 큐

class Queue():
	def __init__(self):
		self.data = []
	
	def push(self, x: int) -> int:
		self.data.append(x)
	
	def pop(self) -> int:
		if self.empty():
			return - 1
		else:
			return self.data.pop(0)
	
	def size(self) -> int:
		return len(self.data)
	
	def empty(self) -> int:
		return 1 if len(self.data) == 0 else 0
	
	def front(self) -> int:
		if self.empty():
			return -1
		else:
			return self.data[0]

	def back(self) -> int:
		if self.empty():
			return -1
		else:
			return self.data[-1]

def solution(command: str, queue: Queue) -> int:
	cmd = command.split(" ")
	if cmd[0] == "push":
		queue.push(int(cmd[1]))
	elif cmd[0] == "pop":
		print(queue.pop())
	elif cmd[0] == "size":
		print(queue.size())
	elif cmd[0] == "empty":
		print(queue.empty())
	elif cmd[0] == "front":
		print(queue.front())
	elif cmd[0] == "back":
		print(queue.back())

if __name__ == "__main__":
	N = int(input())
	queue = Queue()
	[solution(input(), queue) for _ in range(N)]

# (PyPy3) Result: 112324KB / 424ms
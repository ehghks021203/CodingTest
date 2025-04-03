# 2164. 카드2
from sys import stdin, stdout
from collections import deque

def solution(n: int) -> int:
	cards = deque([card for card in range(1, n + 1)])
	while True:
		# 현재 덱에 카드가 하나 남아있을 경우
		if len(cards) == 1: return cards[0]
		# 맨 위에 카드 버리기
		cards.popleft()
		# 제일 위에 있는 카드 맨 아래로 옮기기
		cards.append(cards.popleft())
		

if __name__ == "__main__":
	N = stdin.readline()
	stdout.write(str(solution(int(N))))

# (PyPy3) Result: 121200KB / 128ms
# NOTE: 파이썬의 경우 리스트가 배열 형태이기 때문에 pop의 경우 O(n). 따라서 연결리스트로 구현된 deque를 사용하는게 좋음. (O(1)) 
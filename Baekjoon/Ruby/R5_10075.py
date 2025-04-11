# 10075. 친구

def solution(trust: list, hip: list) -> int:
	value = 0
	# 그래프 역순 탐색
	for host, inviter, protocol in reversed(hip):
		# IAmYourFriend -> host 혹은 inviter를 선택하게 됨
		if protocol == 0:
			value += trust[inviter]
			# 호스트 선택 시 신뢰도 손실을 호스트에 반영
			if trust[host] > trust[inviter]: trust[host] -= trust[inviter]
			# 인바이터 선택 시 호스트 죽이기
			else: trust[host] = 0
		# MyFriendsAreYourFriends -> host와 inviter는 독립 노드
		if protocol == 1:
			trust[host] += trust[inviter]
		# WeAreYourFriends -> 현재까지 존재하는 모든 노드들과 연결되어 있음
		if protocol == 2:
			trust[host] = max(trust[host], trust[inviter])
	return value + trust[0]

if __name__ == "__main__":
	n = int(input())
	trust = list(map(int, input().split()))
	info = list(map(int, input().split()))
	host_inviter_protocol = []
	# 호스트-인바이터-프로토콜 파싱
	for i in range(n - 1):
		host_inviter_protocol.append((info[2 * i], i + 1, info[2 * i + 1]))
	print(solution(trust, host_inviter_protocol))

# (PyPy3) Result: 154444KB / 172ms
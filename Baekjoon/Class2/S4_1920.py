# 1920. 수 찾기

def solution(nums: set, find: list) -> None:
	for num in find:
		if num in nums: print(1)
		else: print(0)

if __name__ == "__main__":
	N = int(input())
	nums = set(map(int, input().split()))
	M = int(input())
	find = list(map(int, input().split()))
	solution(nums, find)

# (PyPy3) Result: 145304KB / 176ms
# NOTE: 리스트를 사용하면 O(N)의 시간복잡도가 소요되므로, set을 사용하거나 이분 탐색을 사용해야함.
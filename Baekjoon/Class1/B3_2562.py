# 2562. 최댓값

def solution(nums: list) -> tuple:
	max_num = 0
	max_idx = 0
	for i in range(len(nums)):
		if max_num < nums[i]:
			max_num = nums[i]
			max_idx = i
	return max_num, max_idx + 1

if __name__ == "__main__":
	nums = [int(input()) for _ in range(9)]
	num, idx = solution(nums)
	print(num)
	print(idx)

# (PyPy3) Result: 108384KB / 88ms
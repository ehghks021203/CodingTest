# 2108. 통계학

def solution(nums: list) -> tuple:
	nums.sort()
	avg = round(sum(nums) / len(nums))
	mid = nums[len(nums) // 2]
	mode_dict = {}
	r = nums[-1] - nums[0]
	if len(nums) == 1:
		mode = nums[0]
	else:
		count = 0
		nums.append(float("inf"))
		for i in range(len(nums) - 1):
			count += 1
			if nums[i] != nums[i + 1]:
				if count in mode_dict.keys():
					mode_dict[count].append(nums[i])
				else:
					mode_dict[count] = [nums[i]]
				count = 0
		mode_list = sorted(mode_dict[max(mode_dict.keys())])
		if len(mode_list) == 1:
			mode = mode_list[0]
		else:
			mode = mode_list[1]
	return avg, mid, mode, r


if __name__ == "__main__":
	N = int(input())
	nums = []
	for _ in range(N):	nums.append(int(input()))
	avg, mid, mode, r = solution(nums)
	print(f"{avg}\n{mid}\n{mode}\n{r}")

# (PyPy3) Result: 153292KB / 372ms
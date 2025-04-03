# 1978. 소수 찾기

def solution(nums: list) -> int:
	count = 0
	for num in nums:
		is_prime = True
		if num == 1:
			continue
		for i in range(2, num):
			if num % i == 0:
				is_prime = False
				break
		if is_prime:
			count += 1
	return count

if __name__ == "__main__":
	N = int(input())
	print(solution(list(map(int, input().split()))))

# (PyPy3) Result: 109544KB / 96ms
# NOTE: 에라토스테네스의 채를 사용하면 시간 복잡도 단축 가능.
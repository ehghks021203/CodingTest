# 10818. 최소, 최대

def solution(nums: list) -> None:
    min = float("inf")
    max = float("-inf")
    for num in nums:
        min = min if min < num else num
        max = max if max > num else num
    print(min, max)
    return

if __name__ == "__main__":
    N = int(input())
    nums = list(map(int, input().split()))
    solution(nums)

# (PyPy3) Result: 219596KB / 324ms
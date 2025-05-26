# 2884. 알람 시계

H, M = map(int, input().split())
print(((H - (0 if M - 45 >= 0 else 1)) + 24) % 24, (M + 15) % 60)

# (PyPy3) Result: 108384KB / 84ms
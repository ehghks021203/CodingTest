# 1011. Fly me to the Alpha Centauri

def solution(x: int, y: int):
    speed = 1
    current = x
    move_count = 0
    while True:
        # 앞으로 전진
        current = current + speed
        move_count += 1
        # 만약 목표 지점까지 도달했다면
        if current == y:
            break
        if (speed + 1)/2*(speed + 2) <= y - current:
            speed += 1
        elif speed/2*(speed + 1) <= y - current:
            speed = speed
        else:
            speed -= 1
    return move_count

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        x, y = map(int, input().split())
        print(solution(x, y))

# Result: 32412KB / 1736ms
# 25.09.10
# 2020039069 박용성

# 하노이의 탑


def hanoi_tower(n, fr, tmp, to):
    if n == 1:
        print(f"원판 1: {fr} → {to}")
    else:
        hanoi_tower(n - 1, fr, to, tmp)
        print(f"원판 {n}: {fr} → {to}")
        hanoi_tower(n - 1, tmp, fr, to)


hanoi_tower(4, "A", "B", "C")

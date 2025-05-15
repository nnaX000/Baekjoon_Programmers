def solution(n, w, num):
    row = n // w
    ram = n % w
    boxes = [row] * w

    if ram > 0:
        if row % 2 != 0:  # ← 방향
            for i in range(-1, -1 - ram, -1):
                boxes[i] += 1
        else:  # → 방향
            for i in range(ram):
                boxes[i] += 1

    # 정확한 (row, col) 계산
    num_idx = num - 1
    num_row = num_idx // w
    col_in_row = num_idx % w

    if num_row % 2 == 0:
        num_col = col_in_row  # →
    else:
        num_col = w - 1 - col_in_row  # ←

    return boxes[num_col] - num_row
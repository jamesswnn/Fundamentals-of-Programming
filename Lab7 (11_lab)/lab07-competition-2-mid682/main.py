'''
lab07-competition-2-mid6821
'''
N = int(input())  # จำนวนแถว {0, 1, ..., N-1}
M = int(input())  # จำนวนคอลลัม {0, 1, ..., M-1}

# แผนที่
grid = []
for i in range(N):
    row = []
    for j in range(M):
        value = int(input())
        row.append(value)

    grid.append(row)

# ตำแหน่งเริ่มต้น
curr_r = int(input())
curr_c = int(input())

# หาความสูง
max_height = grid[0][0]
for r in range(N):
    for c in range(M):
        if grid[r][c] > max_height:
            max_height = grid[r][c]

while True:
    current_height = grid[curr_r][curr_c]

    next_r = curr_r
    next_c = curr_c
    best_height = current_height

    # เหนือ, ใต้, ตก, ออก
    neighbors = [(curr_r - 1, curr_c), (curr_r + 1, curr_c),
                 (curr_r, curr_c - 1), (curr_r, curr_c + 1)]

    for nr, nc in neighbors:
        if 0 <= nr < N and 0 <= nc < M:
            if grid[nr][nc] > best_height:
                best_height = grid[nr][nc]
                next_r = nr
                next_c = nc

    if next_r == curr_r and next_c == curr_c:
        break
    else:
        curr_r = next_r
        curr_c = next_c

print(f"{curr_r} {curr_c}")
print(grid[curr_r][curr_c])

if grid[curr_r][curr_c] == max_height:
    print("Iced Americano, no sugar")
else:
    print("Hot Latte 300% sweetness")

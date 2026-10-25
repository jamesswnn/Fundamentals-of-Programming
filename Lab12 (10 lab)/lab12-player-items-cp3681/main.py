'''
lab12-player-items-cp3681
'''
# YOUR CODE GOES HERE
P = int(input()) #player count
I = int(input()) #item_count
A = int(input()) #assignment_line

players = []
player_items = dict()

#เก็บชื่อผู้เล่นและทำsetว่าง
for _ in range(P):
    name = str(input()).strip()
    players.append(name)
    player_items[name] = set()

#เก็บน้ำหนักไอเท็ม ex. sword : 5
item_weight = dict()
for _ in range(I):
    item = str(input()).strip()
    weight = int(input())
    item_weight[item] = weight

#เพิ่มไอเท็มลง set ของผู้เล่นแต่ละคน
for _ in range(A):
    player = str(input()).strip()
    item = str(input()).strip()
    player_items[player].add(item)

#for 'alice' in players
for player in players:
    total_weight = 0
                #player_items['alice']
    for item in player_items[player]:
        total_weight += item_weight[item]

    print(player, total_weight)
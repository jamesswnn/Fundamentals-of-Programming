'''
lab12-func-damage-sum
'''
# YOUR CODE HERE
# function for calculating damage
def total_Damage(Q, E, R, **kwarv):
    total_Damage = 0

    Buff = kwarv.get("Buff", 0)
    Resistance = kwarv.get("Resistance", 0)
    Addition = kwarv.get("Addition", 0)

    return ((sum(Q) + E + R) * (100 + Buff) / 100) * (100 - Resistance) / 100 + Addition


# Main program to retrieve inputs,
# Call total_Damage function, and
# Print the total damage.
Q = int(input())
Q_list = []

for _ in range(Q):
    list_input = int(input())
    Q_list.append(list_input)

E_input = int(input())
R_input = int(input())

Buff_input = input().strip()
Resistance_input = input().strip()
Addition_input = input().strip()

if Buff_input == "-":
    Buff_input = 0
else:
    Buff_input = int(Buff_input)

if Resistance_input == "-":
    Resistance_input = 0
else:
    Resistance_input = int(Resistance_input)

if Addition_input == "-":
    Addition_input = 0
else:
    Addition_input = int(Addition_input)

print(total_Damage(Q = Q_list, E = E_input, R = R_input, Buff = Buff_input, Resistance = Resistance_input, Addition = Addition_input))

'''
lab10-travelled-cities-set
'''

num1 = int(input())

cities = dict()

for city in range(num1):
    citys_name_1 = str(input())
    num2 = int(input())  # traveller_count

    traveller_set = set()
    for traveller in range(num2):
        traveller_name = str(input())
        traveller_set.add(traveller_name)

    cities[citys_name_1] = traveller_set

num3 = int(input())
all_travellers = set()  # นักท่องเที่ยวที่ไปอย่างน้อย1เมือง
common_travellers = set()  # นักท่องเที่ยวที่ไปครบทุกเมือง

for i in range(num3):
    citys_name_2 = str(input())

    if citys_name_2 in cities:
        if i == 0:
            common_travellers = cities[citys_name_2].copy()
        else:
            common_travellers = common_travellers.intersection(
                cities[citys_name_2])

        all_travellers = all_travellers.union(cities[citys_name_2])

# รายชื่อคนที่ไปอย่างน้อย 1 เมือง
if len(all_travellers) > 0:
    print(sorted(all_travellers))
else:
    print("Not Found")

# งรายชื่อคนที่ไปครบทุกเมือง
if len(common_travellers) > 0:
    print(sorted(common_travellers))
else:
    print("Not Found")

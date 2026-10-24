'''
lab12-func-car-search-cp3681
'''

# ---------------- ข้อมูลรถยนต์ (ห้ามแก้)----------------
cars = [
    {"id": 1, "brand": "Toyota", "model": "Camry", "year": 2021, "price": 1200000},
    {"id": 2, "brand": "Honda", "model": "Civic", "year": 2020, "price": 950000},
    {"id": 3, "brand": "Tesla", "model": "Model 3", "year": 2022, "price": 1800000},
    {"id": 4, "brand": "Mazda", "model": "CX-5", "year": 2021, "price": 1100000},
    {"id": 5, "brand": "Toyota", "model": "Corolla", "year": 2022, "price": 800000},
    {"id": 6, "brand": "Honda", "model": "CR-V", "year": 2021, "price": 1300000},
    {"id": 7, "brand": "Tesla", "model": "Model Y", "year": 2023, "price": 2200000},
    {"id": 8, "brand": "Mazda", "model": "Mazda 3", "year": 2020, "price": 750000},
    {"id": 9, "brand": "Toyota", "model": "Camry", "year": 2022, "price": 1350000},
    {"id": 10, "brand": "Honda", "model": "Civic", "year": 2021, "price": 1050000},
    {"id": 11, "brand": "Toyota", "model": "Camry", "year": 2022, "price": 1300000},
    {"id": 12, "brand": "Mazda", "model": "CX-5", "year": 2021, "price": 1000000},
]
# ---------------------------------------------------------------

def search_car(car_list, min_price, max_price, **kwargs):
    """
    คืนค่ารายการ ID ของรถยนต์ที่ตรงตามเงื่อนไขทุกข้อ (ราคา + **kwargs)
    
    *** ข้อบังคับ: ต้องใช้ค่าจาก **kwargs เท่านั้นในการค้นหา Brand, Model, และ Year ***
    *** ห้ามนักเรียนอ้างอิงถึงตัวแปร Global เช่น brand_input โดยเด็ดขาด มิฉะนั้นจะได้ 0 คะแนน ***
    
    Arguments:
        car_list (list): รายการรถยนต์ทั้งหมด
        min_price (int): ราคาขั้นต่ำที่ต้องการ
        max_price (int): ราคาขั้นสูงที่ต้องการ
        **kwargs: เงื่อนไขการค้นหาเพิ่มเติม (เช่น brand="Toyota", model="Civic", year=2021)

    Returns:
        list[int]: รายการ ID ของรถยนต์ที่ตรงตามเงื่อนไขทั้งหมด
    """
    result = [] #เช่น [1,2]
    #เติมโค้ดที่นี่
    for car in car_list:
        # ถ้าราคาเกินหรือน้อยกว่าตามที่ขอให้ข้ามไปดูคันอื่น
        if car["price"] < min_price or car["price"] > max_price:
            continue

        matches = True
        for key in kwargs:
            if car[key] != kwargs[key]:
                matches = False
                break

        if matches:
            result.append(car["id"])

    return result


# ---------------- การรับ Input 5 บรรทัด (ห้ามแก้)----------------
# ตัวแปรเหล่านี้ถูกเก็บไว้ใน Global Scope แต่ห้ามนำไปใช้ในฟังก์ชัน search_car
brand_input = input().strip()
model_input = input().strip()
year_input = int(input().strip())
min_price = int(input().strip())
max_price = int(input().strip())


# การเรียกใช้ฟังก์ชัน: ส่งตัวแปร Input ทั้ง 3 ตัวเป็น Key-Value Arguments (**kwargs) (ห้ามแก้)
print(search_car(cars, min_price, max_price, brand=brand_input))
print(search_car(cars, min_price, max_price, model=model_input))
print(search_car(cars, min_price, max_price, year=year_input))
print(search_car(cars, min_price, max_price, brand=brand_input, model=model_input, year=year_input))
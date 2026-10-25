products = [
    {"id": 1, "category": "Phone", "brand": "Apple", "year": 2024, "price": 30000},
    {"id": 2, "category": "Phone", "brand": "Samsung", "year": 2023, "price": 25000},
    {"id": 3, "category": "Laptop", "brand": "Apple", "year": 2024, "price": 45000},
    {"id": 4, "category": "Phone", "brand": "Xiaomi", "year": 2024, "price": 12000},
    {"id": 5, "category": "Laptop", "brand": "Lenovo", "year": 2023, "price": 30000},
    {"id": 6, "category": "Tablet", "brand": "Apple", "year": 2022, "price": 20000},
    {"id": 7, "category": "Laptop", "brand": "Samsung", "year": 2024, "price": 40000},
    {"id": 8, "category": "Tablet", "brand": "Xiaomi", "year": 2023, "price": 10000},
    {"id": 9, "category": "Phone", "brand": "Apple", "year": 2023, "price": 28000},
    {"id": 10, "category": "Laptop", "brand": "Lenovo", "year": 2024, "price": 35000}
]


def search_product(product_list, min_price, max_price, **kwargs):
    result = []

    # YOUR CODE HERE
    for product in product_list:
        
        if product['price'] < min_price or product['price'] > max_price:
            continue
        
        matches = True
        for key in kwargs:
            if product[key] != kwargs[key]:
                matches = False
                break
            
        if matches:
            result.append(product['id'])
            
    return result

# **kwargs (category, brand, year)
category_input = input().strip()
brand_input = input().strip()
year_input = int(input().strip())
min_price = int(input().strip())
max_price = int(input().strip())

print(search_product(products, min_price, max_price, category=category_input))
print(search_product(products, min_price, max_price, brand=brand_input))
print(search_product(products, min_price, max_price, year=year_input))
print(search_product(
    products, min_price, max_price,
    category=category_input,
    brand=brand_input,
    year=year_input
))
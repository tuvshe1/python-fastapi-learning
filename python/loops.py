# Python For Loop

products = [
    {"name": "Цаас", "quantity": 10},
    {"name": "Үзэг", "quantity": 3},
    {"name": "Дэвтэр", "quantity": 7},
    {"name": "Хавтас", "quantity": 2},
    {"name": "Баллуур", "quantity": 6}
]

for product in products:
    print(product["name"], "-", product["quantity"], "ширхэг")

    if product["quantity"] < 5:
        print("Бага үлдэгдэлтэй байна!")

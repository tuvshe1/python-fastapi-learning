# Python List and Dictionary

products = [
    {"name": "Цаас", "price": 2500, "quantity": 10},
    {"name": "Үзэг", "price": 1500, "quantity": 3},
    {"name": "Дэвтэр", "price": 3000, "quantity": 7}
]

# Бүх барааг хэвлэх
for product in products:
    print("Бараа:", product["name"])
    print("Үнэ:", product["price"])
    print("Үлдэгдэл:", product["quantity"])
    print("------------------")

# Нийт барааны тоог тооцох
total_quantity = 0

for product in products:
    total_quantity += product["quantity"]

print("Нийт үлдэгдэл:", total_quantity)

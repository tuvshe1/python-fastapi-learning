# Python Functions

def check_stock(product, quantity):
    print("Бараа:", product)
    print("Үлдэгдэл:", quantity)

    if quantity < 5:
        print("Бага үлдэгдэлтэй байна!")
    else:
        print("Үлдэгдэл хангалттай байна.")


check_stock("Цаас", 10)
check_stock("Үзэг", 3)
check_stock("Дэвтэр", 7)

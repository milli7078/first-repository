from smartphone import Smartphone


catalog = [
    Smartphone("Apple", "iPhone 13", "+79161234567"),
    Smartphone("Samsung", "Galaxy S21", "+79261234567"),
    Smartphone("Xiaomi", "Mi 11", "+79371234567"),
    Smartphone("OnePlus", "9 Pro", "+79481234567"),
    Smartphone("Google", "Pixel 6", "+79591234567")
]


for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")


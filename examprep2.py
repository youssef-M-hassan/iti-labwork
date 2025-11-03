import math
import logging
from functools import wraps
import time


logging.basicConfig(
    filename="log.txt",
    level=logging.INFO,
)
"""_day2"""


class vehicle_rental:
    rent_multi = 1
    total_vehicles = 0

    def __init__(self, vehicle_id, brand, model, rental_price):
        self.vehicle_id = vehicle_id
        self.brand = brand
        self.model = model
        self.rental_price = rental_price
        self.is_rented = False
        self.total_vehicles += 1

    @property
    def rent(self):
        self.is_rented = False

    @property
    def return_vehicle(self):
        self.is_rented = True

    def calculate_rental_cost(self, days):
        if not isinstance(days, (int, float)):
            print("please provide a number")
            return

        if days < 0:
            print("days cant be 0/negative value u didnt invent time travel")
            return
        days = math.ceil(days)
        total_price = self.rental_price * days * self.rent_multi
        print(f"you rented a {self.__class__.__name__} for {days} for ${total_price}")
        return total_price

    def get_details(self):
        print(f"{self.brand} {self.model} costs ${self.rental_price} per day")
        return f"{self.brand} {self.model} costs ${self.rental_price} per day {'rented' if self.is_rented else 'available'}"


class Car(vehicle_rental):
    rent_multi = 1

    def __init__(self, vehicle_id, brand, model, rental_price, num_doors):
        super().__init__(vehicle_id, brand, model, rental_price)
        self.num_doors = num_doors

    def get_details(self):
        print(f"{self.brand} {self.model} costs ${self.rental_price} per day")
        return f"{self.brand} {self.model} costs ${self.rental_price} per day {'rented' if self.is_rented else 'available'} number of doors= {self.num_doors}"


class Motorcycle(vehicle_rental):
    rent_multi = 1

    def __init__(self, vehicle_id, brand, model, rental_price, engine_cc):
        super().__init__(vehicle_id, brand, model, rental_price)
        self.engine_cc = engine_cc

    def get_details(self):
        print(f"{self.brand} {self.model} costs ${self.rental_price} per day")
        return f"{self.brand} {self.model} costs ${self.rental_price} per day {'rented' if self.is_rented else 'available'} number of engine cc = {self.engine_cc}"


class Truck(vehicle_rental):
    rent_multi = 1

    def __init__(self, vehicle_id, brand, model, rental_price, cargo_capacity_tons):
        super().__init__(vehicle_id, brand, model, rental_price)
        self.cargo_capacity_tons = cargo_capacity_tons

    def get_details(self):
        print(f"{self.brand} {self.model} costs ${self.rental_price} per day")
        return f"{self.brand} {self.model} costs ${self.rental_price} per day {'rented' if self.is_rented else 'available'} capacity = {self.cargo_capacity_tons}"


# car = Car("V001", "Toyota", "Camry", 50, 4)
# motorcycle = Motorcycle("V002", "Harley", "Street 750", 40, 750)
# truck = Truck("V003", "Ford", "F-150", 80, 2.5)

# print(car.get_details())
# print(motorcycle.get_details())
# print(truck.get_details())

# car.calculate_rental_cost(3)
# motorcycle.calculate_rental_cost(2)
# truck.calculate_rental_cost(5)


class CustomRange:
    def __init__(self, stop, start=0, step=1):
        self.stop = stop
        self.start = start
        self.step = step
        self.initial = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.start >= self.stop and self.step > 0:
            raise StopIteration
        elif self.start <= self.stop and self.step < 0:
            raise StopIteration
        current = self.start
        self.start += self.step
        return current

    def reset(self):
        self.start = self.initial


def my_range(start, stop):
    current = start
    end = stop
    while current < stop:
        yield current
        current += 1


class file_manager:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_file(self):
        with open(self.file_path, "r") as file:
            for line in file:
                yield line.strip()

    def filter_lines(self, keyword):
        with open(self.file_path, "r") as file:
            for line in file:
                if keyword in line:
                    yield line.strip()

    def write_file(self, lines):
        with open(self.file_path, "a") as file:
            file.writelines(lines)

    def strip_file(self):
        with open(self.file_path, "r") as file:
            line = self.read_file
        with open(self.file_path, "w") as file:
            for line in lines:
                file.write(line.strip())

    def chunk_lines(self, chunk_size):
        with open(self.file_path, "r") as file:
            chunk = []
            for line in file:
                chunk.append(line.strip())
                if len(chunk) == chunk_size:
                    yield chunk
                    chunk = []
            if chunk:
                yield chunk


file = file_manager("sample.txt")
# file.write_file(["hello world\n", "wiwi", ", very wiwi indeed wiwi\n"])
# for line in file.filter_lines("wiwi"):
#     print(line)

for chunk in file.chunk_lines(3):
    print(chunk)


# koko = []

# myrange = CustomRange(100)
# wiwi = my_range(1, 10)
# for num in wiwi:
#     koko.append(num)


# print(koko)
# for num in myr
# ange:
#     print(num)
# -------------------------------------------------------------------------------------------
def logger(func):
    logging.info(f"you have run the function {func.__name__}")

    @wraps(func)
    def inner(*args, **kwargs):
        result = func(*args, **kwargs)
        logging.info(
            f"the function {func.__name__} has run with arguments {args} and {kwargs} producing {result}"
        )
        return result

    return inner


def slow_down(func):
    print("sleeping")
    time.sleep(1)

    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper


def time_to_exec(func):
    print("outer func ran")

    @wraps(func)
    def timr():
        start = time.time()
        time.sleep(1)
        func()
        end = time.time()
        print(f"the function {func.__name__} took {end-start:.3f} seconds to run")

    return timr


def count_calls(func):
    start_count = 0

    @wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal start_count
        start_count += 1
        print(f"this function {func.__name__} was called {start_count} times ")
        return func(*args, **kwargs)

    return wrapper


@logger
@count_calls
@slow_down
@time_to_exec
def helloo():
    print("hello world")
    return


# helloo()
# helloo()
# helloo()
class product:
    def __init__(self, product_id, name, price, stock=0, category="general"):
        self.name = name
        self.price = price
        self.stock = stock
        self.category = category
        self.product_id = product_id
        self.__is_available = self.stock > 0

    @property
    def is_available(self):
        return self.__is_available

    def add_stock(self, amount):
        if amount < 0:
            print("cant add negative stock")
            return
        self.stock += amount
        self.__is_available = self.stock > 0

    def dec_stock(self, amount):
        if amount < 0:
            print("woah gonna add to inventory now  by using a reduce function ? ? ")
            return
        if amount > self.stock:
            print("u gotta restock")
            return
        self.stock -= amount
        self.__is_available = self.stock > 0

    def Discount(self, percent):
        if percent < 0 or percent > 100:
            print("invalid discount percent")
            return
        discounted_amount = self.price * (percent / 100)
        self.price -= discounted_amount
        print(f"new price after {percent}% discount is {self.price}")

    def __str__(self):
        return f"product {self.name} with id {self.product_id} in category {self.category} costs {self.price} with stock of {self.stock} units"

    def __repr__(self):
        return f"product({self.product_id}, {self.name}, {self.price}, {self.stock}, {self.category})"

    def __eq__(self, other):
        if not isinstance(other, product):
            return False
        return self.product_id == other.product_id


class Review:
    def __init__(self, user, rating, comment):
        self.user = user
        self.rating = rating
        self.comment = comment

    def is_positive(self):
        return self.rating >= 4


class product_with_reviews(product):
    def __init__(self, product_id, name, price, stock=0, category="general"):
        super().__init__(product_id, name, price, stock, category)
        self.reviews = []

    def add_review(self, user, rating, comment):
        if rating < 1 or rating > 5:
            print("rating must be between 1 and 5")
            return
        review = Review(user, rating, comment)
        self.reviews.append(review)

    def average_rating(self):
        if not self.reviews:
            return "No reviews yet."
        total = sum(review.rating for review in self.reviews)
        return total / len(self.reviews)

    def get_review_summary(self):
        if not self.reviews:
            return "No reviews yet."
        summary = [
            f"User: {review.user}, Rating: {review.rating  } , Comment: {  review.comment}"
            for review in self.reviews
        ]
        return "\n".join(summary)


class shopping_cart:
    def __init__(self, items=None):
        self.items = {} if items is None else items

    def add_product(self, product, quantity=1):
        if quantity <= 0:
            print("quantity must be positive")
            return
        if product in self.items:
            self.items[product] += quantity
        else:
            self.items[product] = quantity

    def remove(self, product):
        if product in self.items:
            del self.items[product]

    def total_cart(self):
        total = 0
        for product, quantity in self.items.items():
            total += product.price * quantity
        return total

    def __len__(self):
        return sum(self.items.values())

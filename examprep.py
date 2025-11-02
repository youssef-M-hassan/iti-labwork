import random
import os
import csv
import logging
from functools import wraps
import time
import datetime


logging.basicConfig(
    filename="log2.txt",
    level=logging.INFO,
)


def convertTemperature():
    try:
        temperature = int(input("please input the temperature :"))
    except Exception as e:
        print("please provide a valid integer ")
    name_output = ""
    choice = input(
        """  1. Celsius to Fahrenheit
             2. Fahrenheit to Celsius
             3. Celsius to Kelvin
             4. Kelvin to Celsius
             Choose conversion (1-4):"""
    )
    match choice:
        case "1":
            result = round(temperature * (9 / 5) + 32, 5)
            name_output = "Fahrenheit"
        case "2":
            result = round((temperature - 32) / (9 / 5), 5)
            name_output = "Celsius"
        case "3":
            result = round(temperature + 273.15, 5)
            name_output = "Kelvin"
        case "4":
            result = round(temperature - 273.15, 5)
            name_output = "Celsius"
        case _:
            print("invalid input")
    # Kelvin, Fahrenheit = round(celsius + 273.15, 5), round(celsius * 1.80 + 32.00, 5)
    return print(f"your temp  is {result} {name_output}")


# convertTemperature()
"""list question 2"""


class List_man:
    def __init__(self, lists=None):
        if lists is None:
            lists = []
        self.lists = lists

    @staticmethod
    def summation(arr):
        print(sum(arr))
        return sum(arr)

    @staticmethod
    def avrg(arr):
        print(round(sum(arr) / len(arr), 2))
        return round(sum(arr) / len(arr), 2)

    @staticmethod
    def max_min(arr):
        print(f"the maximum is {max(arr)} and the min is {min(arr)}")
        return max(arr), min(arr)

    @staticmethod
    def unique(arr):
        unique_set = set()
        uniq_list = []

        for numb in arr:
            if numb not in unique_set:
                unique_set.add(numb)
                uniq_list.append(numb)
        print(f" your unique list is {uniq_list}")

        return uniq_list

    @staticmethod
    def sort_asc(arr):
        result = sorted(arr)
        print(f"your sorted array asc is {result}")
        return result

    @staticmethod
    def sort_desc(arr):
        result = sorted(arr, reverse=True)
        print(f"your sorted array desc is {result}")
        return result

    @staticmethod
    def odd_even(arr):
        Odd = []
        even = []
        for numb in arr:
            if numb % 2 == 0:
                even.append(numb)
            elif numb % 3 == 0:
                Odd.append(numb)
        print(f"your even list is {even} and your odd list is {Odd}")
        return Odd, even


# list_manup = List_man()
# og_list = [5, 3, 8, 3, 9, 1, 8, 2]
# list_manup.odd_even(og_list)


class string_anal:
    def __init__(self, text=None):
        if text is None:
            text = ""
        self.str = text.strip

    @staticmethod
    def char_freq(text):
        characters = text.replace(" ", "").lower()
        max_val = 0
        result = {}
        for char in characters:
            result[char] = result.get(char, 0) + 1
        print(result)
        for key in result:
            if result[key] > max_val:
                max_val = result[key]
        most_common = [key for key, value in result.items() if value == max_val]
        print(f"most commin is {most_common}")
        return result

    @staticmethod
    def wordcount(text):
        result = text.split(" ")
        print(f" your word count = {len(result)}")
        return result

    @staticmethod
    def palindromo(text):
        characters = text.replace(" ", "").lower()
        return True if characters[::-1] == characters else False

    @staticmethod
    def reverseee(text):
        return text[::-1]


test = "Python Programming"
wiwi = string_anal()
wiwi.char_freq(test)

print(wiwi.palindromo("uwu"))


class guessguess:
    def __init__(self):
        self.secret = random.randint(1, 100)
        self.attempts = 7
        self.victory = """       _      _                   
                    (_)    | |                  
                __   ___  ___| |_ ___  _ __ _   _ 
                \ \ / / |/ __| __/ _ \| '__| | | |
                \ V /| | (__| || (_) | |  | |_| |
                \_/ |_|\___|\__\___/|_|   \__, |
                                            __/ |
                                            |___/ """

    def game_mech(self):
        hiddennum = self.secret
        while self.attempts > 0:
            try:
                guess = int(input("guess a number"))
            except exception:
                print("pleave provide an integer")
            if guess == hiddennum:
                print("congrats you guessed correctly")
                print(self.victory)
                break
            elif guess > hiddennum:
                self.attempts -= 1
                print(
                    f"too high try again, your guess was {guess} attempts: {self.attempts}"
                )
            elif guess < hiddennum:
                self.attempts -= 1
                print(
                    f"too low try again, your guess was {guess} attempts: {self.attempts}"
                )
            else:
                print("invalid response ")

        play = input("do u want to play again ? y/n")
        if play == "y":
            self.game_mech()

    def autorun(self):
        hiddennum = self.secret
        print("guess a numb from 1-100")
        maxi = 100
        mini = 0

        while True:
            pc_guess = (maxi + mini) // 2
            answer = input(
                f"is your guess = {pc_guess} ? lower/higher or is it correct : l/h/= : "
            )
            if answer == "=":
                print("yay")
                print(self.victory)
                break
            elif answer == "l":
                maxi = (maxi + mini) // 2
                continue
            elif answer == "h":
                mini = (maxi + mini) // 2
                continue
            else:
                print("invalid input")


# guessguess().autorun()
class shopping:
    def __init__(self):
        self.storage = {}
        self.discount = 0.9
        self.menu = """Shopping Cart Menu:
                        1. Add item
                        2. Remove item
                        3. Update quantity
                        4. View cart
                        5. Checkout
                        6. Exit"""

    def Add_item(self):
        while True:
            try:
                item_name = input("enter the name of the item u want to add : ").strip()
                if not item_name.isalpha():
                    raise ValueError
            except Exception as e:
                print("enter a valid name with  no numbers")
                continue
            try:
                item_quantity = int(input(f"enter  the quantity of {item_name}: "))
                if item_quantity <= 0 or not item_quantity:
                    raise ValueError
            except ValueError:
                print("please provide a valid number")
                continue
            try:
                item_price = int(input(f"enter  the price of {item_name} : "))
                if item_price <= 0 or not item_price:
                    raise ValueError
            except ValueError:
                print("please provide a valid number")
                continue
            self.storage[item_name] = {
                "item_quantity": item_quantity,
                "item_price": item_price,
            }
            return

    def remove_item(self):
        while True:
            self.view_cart()
            try:
                choice = int(
                    input("please select the id of the item u want to delete : ")
                )
                if choice < 0 or not choice:
                    raise ValueError
            except Exception:
                print("please select a valid id ")
                continue
            break
            item_removed = list(self.storage.keys())[choice]
            self.storage.pop(item_removed)
            return

    def view_cart(self):
        i = 0
        for key, value in self.storage.items():

            print(f"id={i}: {key} :{value}")
            i += 1

    def update_history(self):
        while True:
            self.view_cart()
            try:
                choice = int(
                    input(
                        "please select the id of the item u want to modify quantity : "
                    )
                )
                if choice < 0 or not choice:
                    raise ValueError
            except Exception:
                print("please select a valid id ")
                continue
            break
        item_modified = list(self.storage.keys())[choice]
        try:
            quantity = int(input("the quantity  to modify quantity : "))
            if quantity < 0 or not quantity:
                raise ValueError
        except Exception:
            print("please select a valid number")

        self.storage[item_modified]["item_quantity"] = quantity
        return

    def checkout(self):
        total = 0
        for key in self.storage:
            total += self.storage[key]["item_price"]
        if total >= 300:
            print("congrats u earned a 10 precent discount")
            total = total * 0.9
            print(f"please pay {total:.2f}")
        else:
            print(f"please pay {total}")

    def run(self):
        while true:
            print(self.menu)
            choice = input("choose  what u want ")
            match choice:
                case "1":
                    self.Add_item()
                case "2":
                    self.remove_item()
                case "3":
                    self.update_history()
                case "4":
                    self.view_cart()
                case "5":
                    self.checkout()
                case "6":
                    break
                case _:
                    print("invalid")


class contact_manager:
    def __init__(self):
        self.contacts = {}
        with open("contacts.csv", mode="w") as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Phone", "Email"])

    def add_contact(self):
        name = input("enter contact name: ")
        try:
            phone = int(input("enter contact phone number: "))
        except ValueError:
            print("please provide a valid phone number")
            return
        email = input("enter contact email: ")
        self.contacts[name] = {"phone": phone, "email": email}
        print(f"contact {name} {phone} {email} added.")
        with open("contacts.csv", mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([name, phone, email])

    def remove_contact(self):
        name = input("enter contact name to remove: ")
        if name in self.contacts:
            del self.contacts[name]
            print(f"contact {name} removed.")
        else:
            print(f"contact {name} not found.")

    def view_contacts(self):
        if not self.contacts:
            print("no contacts available.")
        else:
            for name, phone in self.contacts.items():
                print(f"{name}: {phone}")

    def search_contact(self):
        name = input("enter contact name to search: ")
        if name in self.contacts:
            print(f"{name}: {self.contacts[name]}")
        else:
            print(f"contact {name} not found.")

    def update_contact(self, name, new_phone):
        if name in self.contacts:
            self.contacts[name] = new_phone
            print(f"contact {name} updated.")
        else:
            print(f"contact {name} not found.")

    def run(self):
        while True:
            print(
                """contact manager eenu:
                      1. add Contact
                      2. remove Contact
                     3. view Contacts
                     4. search Contact
                  5. update Contact
                6. Exit"""
            )
            choice = input("chose an option (1-6): ")
            match choice:
                case "1":
                    self.add_contact()
                case "2":
                    name = input("enter contact name to remove: ")
                    self.remove_contact(name)
                case "3":
                    self.view_contacts()
                case "4":
                    name = input("enter contact name to search: ")
                    self.search_contact(name)
                case "5":
                    name = input("Enter contact name to update: ")
                    new_phone = input("Enter new phone number: ")
                    self.update_contact(name, new_phone)
                case "6":
                    break
                case _:
                    print("Invalid option. Please try again.")


# shopify = shopping()
# shopify.Add_item()
# shopify.Add_item()
# shopify.Add_item()
# shopify.remove_item()
# shopify.update_history()
# shopify.remove_item()
# call = contact_manager()
# call.run()
class logfiler:
    def __init__(self):
        pass

    def logging():
        logging.info(f"{datetime.datetime.now()} the user has logged in")


logfiler.logging()

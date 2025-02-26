"""Amazon Expenses Tracker"""

import getpass
import datetime
import re
import time

print("Good day, please register your account on our Website")
username = input("Please enter your username: ")

def pw_valid_check(password):
    if not (6 <= len(password) <= 20):
        print("Your password must be between 6 to 20 characters long.")
        return False
    if not any(char.isdigit() for char in password):
        print("Your password must have at least one number.")
        return False
    if not any(char.isupper() for char in password) or not any(char.islower() for char in password):
        print("Your password must at least contain one lowercase AND at least one uppercase character ")
        return False
    if not any(char in '!"§$%&/()=,.-;:_' for char in password):
        print('Your password must have at least one special symbol. Allowed special symbols:"!"§$%&/()=,.-;:_"')
        return False
    return True, password

def pw_register():
    print("Your password Must have following criteria to be :")
    print("-  Must have at least one number.")
    print("-  Must have at least one uppercase and one lowercase character.")
    print('-  Must have at least one special symbol. Allowed special symbols:"!"§$%&/()=,.-;:_"')
    print("-  Must be between 6 to 20 characters long.")
    while True:
        password = getpass.getpass("Enter your password: ")
        if pw_valid_check(password):
            return password
        
password = pw_register()

def register_number():
    while True:
        user_input = input("Please enter your German mobile number (starting with +49, followed by 10 digits): ")

        if re.match(r"^(?:\+49|0)[1-9]\d{10,14}$", user_input):
            print("Valid German mobile number entered!")
            return user_input
        else:
            print("Invalid number. Please try again.")
            
register_number()

def login():
    attempts = 0

    while attempts < 3:
        check_username = input("Enter your username: ")
        check_password = getpass.getpass("Enter your password: ")

        # Check if the username and password match
        if check_username == username and check_password == password:
            print("Login successful!")
            return True
        else:
            print("Invalid username or password. Please try again.")
            attempts += 1

    # 5 Sec delay, print something about all attempts used.
    print("You have used all your attempts. Please try again in 5 seconds.")
    time.sleep(5)

    # Last chance to login
    check_username = input("Enter your username: ")
    check_password = input("Enter your password: ")

    if username == check_username and password == check_password:
        print("Login successful!")
        return True
    else:
        print("Invalid username or password. Please register again.")
        return False
    
if not login():
    exit()
    
print("Welcome to the Amazon Expense Tracker!")

def purchase_date_formator():
    date_input = input("Enter the date of the purchase (MM/DD/YYYY or MM-DD-YYYY): ")
    if "/" in date_input:
        split = "/"
    elif "-" in date_input:
        split = "-"
    else:
        print("Wrong format. Please use MM/DD/YYYY or MM-DD-YYYY")
        return purchase_date_formator()
        
    date_without_split = date_input.split(split)
        
    if len(date_without_split) == 3:
        month, day, year = date_without_split
        if len(month) == 2 and len(day) == 2 and len(year) == 4:
            if month.isdigit() and day.isdigit() and year.isdigit():
                if split == "/":
                    date_obj = datetime.datetime.strptime(date_input, "%m/%d/%Y")
                else:
                    date_obj = datetime.datetime.strptime(date_input, "%m-%d-%Y")
                return date_obj.strftime("%m/%d/%Y")
    print("Invalid date format. Please use MM/DD/YYYY or MM-DD-YYYY.")
    return purchase_date_formator()
                
def choices():
    print("What do you want to do?")
    print("1. Enter a purchase")
    print("2. Generate a report")
    print("3. Quit.")
    choice = int(input("Enter your choice (1-3): "))
    return choice
    
def collect_info_purchase():
    choice = choices()
    while choice >= 4 and choice == 0:
        print("Invalid number, please enter a number between 1-3.")
        choice = int(input("Enter your choice (1-3): "))
    else:
        pass        
    if choice == 1:
        print("You picked 'Enter a purchase'")
        print("First we would need to have the purchasing date of the item!")
        # call function to check purchase date
        purchase_date = purchase_date_formator()
        # print the verified purchase date
        print(f"Purchased date noted as ({purchase_date})")
        # check that item has min 3 characters in string
        i_name = input("Please enter the name of your purchased item (min 3 characters): ")
        # check whether the item name is at least 3 characters long
        if len(i_name) < 3:
            i_name = input("The items must have at least 3 characters, please try again.")
        else:
            # print the purchased item name
            print(f"Your purchased item name: {i_name}")
        print("We got the purchase date and the item name, next is the total cost including charges for delivery.")
        cost = input("Please enter the total cost of the purchased item including any charges on delivery: ")

        while not (cost.replace('.', '', 1).isdigit() and cost.count('.') <= 1):
            print("Invalid format, please retry.")
            cost = input("Please enter the total cost including any charges on delivery: ")
        cost = float(cost)
        print(f"Thank you, we noted the cost of your purchased item as: {cost} €")          
        # weight of the item 
        print("Now we need the weight of the item")
        # check for pattern as a def
        def check_pattern(text, pattern):
            if re.search(pattern, text):
                return True
            else:
                return False

        weight_check = input("Please enter the total weight of the item in kg: ")
        kg_pattern = "kg$"
        checked_weight = check_pattern(weight_check, kg_pattern)
        weight = weight_check.replace("kg", "", 1).strip()
        while checked_weight != True or not weight.replace('.', '', 1).isdigit() or '.' not in weight:
            print("Please make sure that the weight entered is a float and includes kg at the end!")
            weight_check = input("Please enter the total weight of the item in kg: ")
            checked_weight = check_pattern(weight_check, kg_pattern)
            weight = weight_check.replace("kg", "", 1).strip()
        else:
            print(f"Thank you, your weight has been noted as {weight_check}.")
        print("The last thing we need to note your purchase is the quantity. \nHow many times did you purchase this item?")
        quantity = input("Please enter your number here: ")
        while not quantity.isdigit() or int(quantity) <= 0:
            quantity = input("Please enter your number here (needs to be higher than 0): ")
        quantity = int(quantity)
        print(f"Thank you, we noted the quantity as {quantity}.")
    if choice == 2:
        # TODO
        print("Sorry this option is currently under development")
    if choice == 3:
        print(f"Thank you for visiting Amazon Expenses Tracker {user}!")
        exit()

collect_info_purchase()

    # TODO put everything into a list/dict from choice 1
    # TODO allow choice 2 only if choice 1 was used once
    # TODO calculate everything if choice 2.
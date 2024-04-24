# Task 1
num1 = 10
num2 = 5

print("Multiplication:", num1 * num2)
print("Division:", num1 / num2)
print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)

# Task 2
book1_name = "Book 1"
book1_price = 20
book2_name = "Book 2"
book2_price = 15
book3_name = "Book 3"
book3_price = 25
book4_name = "Book 4"
book4_price = 18
book5_name = "Book 5"
book5_price = 30
book6_name = "Book 6"
book6_price = 22
book7_name = "Book 7"
book7_price = 28
book8_name = "Book 8"
book8_price = 17
book9_name = "Book 9"
book9_price = 21
book10_name = "Book 10"
book10_price = 35

total_price = book1_price + book2_price + book3_price + book4_price + book5_price + book6_price + book7_price + book8_price + book9_price + book10_price

if total_price >= 100:
    total_price_with_discount = total_price * 0.8
    print("Total price with 20% discount:", total_price_with_discount)
elif total_price >= 50:
    total_price_with_discount = total_price * 0.9
    print("Total price with 10% discount:", total_price_with_discount)
else:
    print("Total price without discount:", total_price)

# Task 3
family_members = {
    "Alice": 30,
    "Bob": 45,
    "Charlie": 20,
    "David": 55,
    "Emily": 40
}

for member, age in family_members.items():
    print(member, "will be", age + 25, "years old after 25 years.")

# Task 4
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
age = input("Enter your age: ")
residence = input("Enter your place of residence: ")
profession = input("Enter your profession: ")
hobbies = input("Enter your hobbies: ")

sentence = f"My name is {first_name} {last_name}. I am {age} years old and I live in {residence}. I work as a {profession} and my hobbies include {hobbies}."
print(sentence)

# Task 5
number = int(input("Enter a number: "))

if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")


"""
1)პირველ რიგში DEF-ის გამოყენებით განვსაზღვროთ მათმატიკური ოპერაციები 
2)შემდეგ მომხმარებელს ავარჩევინოთ რომელი ოპერაცია სურს
3)შემდეგ ავარჩვინოთ ორი რიცხვი რომელზეც მოქმედებები სურს მომხმარებელს
4)შემდეგ შებვასრულოთ მოქმედებები 
5)და ბოლოს გამოვიტანოთ საბოლოო შედეგი


"""
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "error"

def calculator():
    print("Choose which one you need:")
    print("1. (+)")
    print("2. (-)")
    print("3. (*)")
    print("4. (/)")

    choice = input("first, second, third or fourth: ")

    num1 = int(input(" first number: "))
    num2 = int(input("second number: "))

    if choice == '1':
        result = int(add(num1, num2))
    elif choice == '2':
        result = int(subtract(num1, num2))
    elif choice == '3':
        result = int(multiply(num1, num2))
    elif choice == '4':
        result = int(divide(num1, num2))
    else:
        result = "error"

    print("Result: ", result)


calculator()


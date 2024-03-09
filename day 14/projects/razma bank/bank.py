balance = 0

def deposit(amount):
    global balance
    balance += amount
    print(f"თანხის შეტანა ${amount}. ახლანდელი ბალანსი: ${balance}")

def withdraw(amount):
    global balance
    if amount > balance:
        print("თნხის გამოტანა ვერ მოხერხდა.")
    else:
        balance -= amount
        print(f"გამოტანილი თანხა${amount}. ახლანდელი ბალანსი: ${balance}")

def display_balance():
    print(f"ახლანდელი ბალანსი: ${balance}")

def main():
    print("მოგესალმებით რაზმა ბანკში!")

    while True:
        print("\nოპერაციები:")
        print("1. თანხის შეტანა")
        print("2. თანხის გამოტანა")
        print("3. ბალანსის ნახვა")
        print("4. გამოსვლა ")

        choice = input("დააფიქსირეთ თქვენი არჩევანი (1/2/3/4): ")

        if choice == '1':
            deposit_amount = float(input("დააფიქსირეთ შეტანილი თნხის რაოდენობა: "))
            deposit(deposit_amount)

        elif choice == '2':
            withdraw_amount = float(input("დააფიქსირეთ გამოტანილი თნხის რაოდენობა: "))
            withdraw(withdraw_amount)

        elif choice == '3':
            display_balance()

        elif choice == '4':
            print("რაზმა ბანკიდან გამოსვლა. მადლობა სარგებლობისთის!")
            break

        else:
            print("არასწორი არჩევანი. გთხოვთ მიუთითოთ ჩამოთვლილთაგან (1/2/3/4).")

if __name__ == "__main__":
    main()

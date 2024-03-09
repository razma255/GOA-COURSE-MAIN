import random
user_name = input("თქვენი სახელი : ")
user_score = 0
computer_score = 0
rounds = int(input("დააფიქსირეთ რაუნდების რაოდენობა : "))

for _ in range(rounds):
    user_roll = random.randint(1, 6)
    computer_roll = random.randint(1, 6)

    print(f"{user_name} გააგორა {user_roll}")
    print(f"კომპიუტერმა გააგორა  {computer_roll}")

    user_score += user_roll
    computer_score += computer_roll

print("\nთამაში დასრულდა")
print(f"{user_name}-ს ჯამური ქულაა: {user_score}")
print(f"კომპიუტერის ჯამური ქულაა: {computer_score}")

if user_score > computer_score:
    print(f"{user_name} მოიგო!")
elif user_score < computer_score:
    print("კომპიუტერმა მოიგო!")
else:
    print("თამაშით ფრედ დასრულდა!")

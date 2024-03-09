import random

account_data = []
bank_money = 0
handmoney = 0
class Account:
    def __init__(self, username, password, account_money, handmoney):
        global individual_data
        self.username = username
        self.password = password
        self.account_money = account_money
        self.handmoney = handmoney
        self.account_id = random.randint(100000000, 200000000)

        individual_data = {}
        individual_data['username'] = username
        individual_data['money'] = int(account_money)
        individual_data['password'] = password
        individual_data['handmoney'] = int(handmoney)
        individual_data['account_id'] = self.account_id
        account_data.append(individual_data)

    def deposit(self, amount):
        if amount > individual_data['handmoney']:
            return 'Sorry, you do not have that much ammount to deposit'
        individual_data['money'] += amount
        individual_data['handmoney'] -= amount
        return f'Succesfuly deposited {amount}$\nBank Account money - {individual_data['money']}$\nHand on money - {individual_data['handmoney']}$'
        
    def withdraw(self, amount):
        if amount > individual_data['money']:
            return 'Sorry, you do not have that much ammount to withdraw'
        individual_data['money'] -= amount
        individual_data['handmoney'] += amount
        return f'Succesfuly withdrawed {amount}$\nBank Account money {individual_data['money']}$\nHand on money - {individual_data['handmoney']}$'
    
    def info(self):
        return f'Bank account money - {self.account_money}\nHand on money - {self.handmoney}\nPassword {self.password}\nAccound ID: {self.account_id}'

    def transmit(self, acc_id, amount):
        for dct in account_data:
            for key, val in dct.items():
                if key == 'accound_id' and val == acc_id:
                    dct['money'] += int(amount)
        return f'Succesfuly deposited {amount} to account id - {acc_id}'


while True:
    user_input = input('> ')
    if user_input == 'register':
        print('Enter Username')
        username = input('> ')
        print('Enter Password')
        password = input('> ')
        print('Enter amount of money you want to have')
        money = input('> ')
        account = Account(username, password, money, 0)
        print('Succesfuly created account for {username}\nPlease enter "login" to login to your account')
    elif user_input == 'login':
        print('Enter your username')
        username = input('>')
        print('Enter your password')
        password = input('>')
        for dct in account_data:
            for key, value in dct.items():
                if key == 'username' and value == username:
                    continue
                elif key == 'password' and value == password:
                    continue
                elif key == 'money' or key == 'handmoney' or key == 'account_idre':
                    continue
                else:
                    print('Password or Username is wrong')


        print('Succesfuly logged in')
        for dct in account_data:
            for key, val in dct.items():
                if val == password:
                    bank_money = individual_data.get('money')
        print(bank_money)
    elif user_input == 'withdraw':
        print('Enter money you want to withdraw from your bank account')
        withdraw_input = int(input('> '))
        print(account.withdraw(withdraw_input))
    elif user_input == 'deposit':
        print('Enter money you want to deposit to your bank account')
        deposit_amount = int(input('> '))
        print(account.deposit(deposit_amount))
    elif user_input == 'info':
        print(account.info())
    
    elif user_input == 'logout':
        bank_money = 0
    
    elif user_input == 'trasmit':
        print('Enter account id')
        acc_id = int(input('> '))
        print('enter amount')
        amount = int(input('> '))
        print(account.transmit(acc_id, amount))
        bank_money -= amount
    
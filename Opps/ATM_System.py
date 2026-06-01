class ATM:
    def __init__(self):
        self.pin = '1234'
        self.balance = 5000
        self.history = []

    def check_balance(self):
        print("Balance : ", self.balance)

    def deposit(self, amt):
        self.balance += amt
        self.history.append(f"Deposit {amt}")
        print("Money Deposit sucessfully...")

    def withdraw(self, amt):
        if amt <= self.balance:
            self.balance -= amt
            self.history.append(f"Withdraw{amt}")
            print("Money withdraw sucessfully....")
        
        else:
            print("Insufficient balance.....")

    def change_pin(self, new_pin):
        self.pin = new_pin
        print("Pin changed !!")

    def bank_history(self):
        print("\n transaction history")

a = ATM()

pin = input("Enter pin")

if pin == a.pin:
    while True:
        print("\n 1. check balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. chnage pin")
        print("5. Transaction history")
        print("6. exit")

        ch = int(input("Enter your choice : "))

        if ch == 1:
            a.check_balance()
        elif ch == 2:
            amt = int(input("Enter amt : "))
            a.deposit(amt)

        elif ch == 3:
            amt = int(input("Enter amt : "))
            a.withdraw(amt)

        elif ch == 4:
            new_pin = input("Enter Pin : ")
            a.change_pin(new_pin)

        elif ch == 5:
            a.bank_history()

        elif ch == 6:
            print("Thank you ...")
            break

        else:
            print("Invalid choice ")

else:
    print("Wrong PIN ")
            

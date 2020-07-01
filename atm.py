class Atm(object): 

    def __init__(self , name , cardnumber , pin):
        self.name = name
        self.cardnumber = cardnumber
        self.pin = pin

    def checkBalance(self):
        print("Your balance is 50000")

    def withdrawal(self , amount):
        new_Amount = 50000 - amount
        print("you have withdrawn" + str(amount) + "your remaining balance is" + str(new_Amount))

def main():
    name = input("Enter your name")
    cardnumber = input("insert your card number")
    pinnumber = input("input your pin number")
    newUser = Atm(name , cardnumber , pinnumber)
    print("choose your option")
    print("1) balanceEnquiry 2) widrawal")
    activity = int(input("enter your activity number"))
    if(activity == 1):
        newUser.checkBalance()
    elif(activity == 2):
        amount = int(input("Enter the amount"))
        newUser.withdrawal(amount)
if __name__=="__main__":
    main()


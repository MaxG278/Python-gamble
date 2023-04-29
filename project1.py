MAX_LINES = 3

def deposit():
    while True:
        amount = input("What do you want to deposit? €")
        if amount.isdigit():
            amoung = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        return amount


def get_number_of_lines():
    while true:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")?")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        return amount



def main():
    balance = deposit()



main()    
        
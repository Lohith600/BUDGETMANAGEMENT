from transaction import Transaction, Income, Expense, Savings
import os

#Text prompt for ID and Pass to be there at the start of program
def login(LoginDict):
    try:
        choice=int(input("Enter 1 For exixting user\n2 For new user\n"))
    except ValueError:
        print("Enter correct value")
    if choice==1:
        while True:
            UserName=input("Enter Username: ")
            Password=input("Enter Password: ")
            flag=UserName in LoginDict.keys()
            if flag==True and LoginDict[UserName]==Password:
                return UserName
            elif flag==False:
                print("User not found!")
            else:
                print("Wrong Combination! Try again...")

    elif choice==2:
        while True:
            UserName=input("Create Username: ")
            Password=input("Enter Password: ")
            ConfirmPassword=input("Confirm Password: ")
            
            flag=UserName in LoginDict.keys()
            if flag==False and Password==ConfirmPassword:
                LoginDict[UserName]=Password
                os.mkdir(UserName)
                open(f'{UserName}/income.csv', mode="w").close()
                open(f'{UserName}/savings.csv', mode="w").close()
                open(f'{UserName}/expenses.csv', mode="w").close()
                print("User added!")
                return UserName
            elif flag==True:
                print("User already exists")
            else:
                print("Both passwords are not same")


def add(listOfTransactions):
    choice = None
    while choice not in [0,1,2,3]:
        try:
            choice = int(input("Enter the type of transaction:\n1. Income\n2. Expense\n3. Savings\n0. Exit\n"))
            if choice not in [0,1,2,3]:
                print("Invalid choice, please enter a correct choice.")
        except ValueError:
            print("Invalid input, please enter a number.")
    if choice == 0:
        return
    amount = float(input("Enter the amount: "))
    date = input("Enter the date in DD-MM-YYYY format: ")
    if choice == 1: # For Income Transaction type
        source = input("Enter the source of income: ")
        obj = Income(amount, date, source)
    elif choice == 2: # For Expense
        category = input("Enter the category of expense: ")
        type = input("Enter the type of expense: ")
        obj = Expense(amount, date, category, type)
    elif choice == 3: # For Savings
        goal = input("Enter the goal of the saving: ")
        target = float(input("Enter the target amount: "))
        obj = Savings(amount, date, goal, target)

    listOfTransactions.append(obj)
    print("Added Transaction: ") # Print newly added task
    print(str(obj))


def edit(listOfTransactions):
    # Get which transaction to edit
    serial = 1
    index = 0
    for transaction in listOfTransactions:
        print(serial, ": ", transaction, sep='')
    
    while  index < 1 or index > len(listOfTransactions):
        try:
            index = int(input("Enter the serial number of the transaction you want to edit: "))
            if index < 1 or index > len(listOfTransactions):
                print("Invalid choice, please enter a correct choice.")
        except ValueError:
            print("Invalid input, please enter a number.")
    index -= 1

    # Print the current transaction
    transaction = listOfTransactions[index]
    print("Editing Transaction: ")
    print(str(transaction))

    # Edit the transaction as per the user's needs
    if isinstance(transaction, Income):
        choice = None
        while choice not in [1,2,3]:
            try:
                choice = int(input("Enter the attribute you want to edit:\n1. Amount\n2. Date\n3.Source\n"))
                if choice not in [1,2,3]:
                    print("Invalid choice, please enter a correct choice.")
            except ValueError:
                print("Invalid input, please enter a number.")
        if choice == 1:
            amount = float(input("Enter the updated amount: "))
            obj = Income(amount, transaction.date, transaction.source)
        elif choice == 2:
            date = input("Enter the updated date in DD-MM-YYYY format: ")
            obj = Income(transaction.amount, date, transaction.source)
        elif choice == 3:
            source = input("Enter updated source of income: ")
            obj = Income(transaction.amount, transaction.date, source)
    elif isinstance(transaction, Expense):
        choice = None
        while choice not in [1,2,3,4]:
            try:
                choice = int(input("Enter the attribute you want to edit:\n1. Amount\n2. Date\n3. Category\n4. Expense Type\n"))
                if choice not in [1,2,3,4]:
                    print("Invalid choice, please enter a correct choice.")
            except ValueError:
                print("Invalid input, please enter a number.")
        if choice == 1:
            amount = float(input("Enter the updated amount: "))
            obj = Expense(amount, transaction.date, transaction.category, transaction.expense_type)
        elif choice == 2:
            date = input("Enter the updated date in DD-MM-YYYY format: ")
            obj = Expense(transaction.amount, date, transaction.category, transaction.expense_type)
        elif choice == 3:
            category = input("Enter the updated category of expense: ")
            obj = Expense(transaction.amount, transaction.date, category, transaction.expense_type)
        elif choice == 4:
            type = input("Enter the updated type of expense: ")
            obj = Expense(transaction.amount, transaction.date, transaction.category, type)
    elif isinstance(transaction, Savings):
        choice = None
        while choice not in [1,2,3,4]:
            try:
                choice = int(input("Enter the attribute you want to edit:\n1. Amount\n2. Date\n3.Goal\n4. Target Amount\n"))
                if choice not in [1,2,3,4]:
                    print("Invalid choice, please enter a correct choice.")
            except ValueError:
                print("Invalid input, please enter a number.")
        if choice == 1:
            amount = float(input("Enter the updated amount: "))
            obj = Savings(amount, transaction.date, transaction.goal, transaction.target_amount)
        elif choice == 2:
            date = input("Enter the updated date in DD-MM-YYYY format: ")
            obj = Savings(transaction.amount, date, transaction.goal, transaction.target_amount)
        elif choice == 3:
            goal = input("Enter the updated goal of the saving: ")
            obj = Savings(transaction.amount, transaction.date, goal, transaction.target_amount)
        elif choice == 4:
            target = float(input("Enter the updated target amount: "))
            obj = Savings(transaction.amount, transaction.date, transaction.goal, target)
    
    listOfTransactions[index] = obj
    print("Updated Transaction: ")
    print(str(obj))


def delete(listOfTransactions):
    # Get which transaction to delete
    serial = 1
    choice = 0
    for transaction in listOfTransactions:
        print(serial, ": ", transaction, sep='')
    
    while choice <1 or choice > len(listOfTransactions):
        try:
            choice = int(input("Enter the serial number of the transaction you want to delete: "))
            if choice < 1 or choice > len(listOfTransactions):
                print("Invalid choice, please enter a correct choice.")
        except ValueError:
            print("Invalid input, please enter a number.")
    choice -= 1

    # Printing transaction before deleting
    print("Deleting Transaction: ")
    print(listOfTransactions[choice])
    del listOfTransactions[choice]


def balance(listOfTransactions):
    totalIncome = sum(transaction.amount for transaction in listOfTransactions if isinstance(transaction, Income))
    totalExpense = sum(transaction.amount for transaction in listOfTransactions if isinstance(transaction, Expense))
    balance = totalIncome - totalExpense
    return [totalIncome, totalExpense, balance]


def categorize(listOfTransactions):
    categoryTotal = {}
    for transaction in listOfTransactions:
        if isinstance(transaction, Expense):
            if transaction.category in categoryTotal:
                categoryTotal[transaction.category] += transaction.amount
            else:
                categoryTotal[transaction.category] = transaction.amount
    return categoryTotal


def progress(listOfTransactions):
    # Need to think about this a bit
    pass


def describeTransactions(listOfTransactions):
    return [str(transaction) for transaction in listOfTransactions]


def findTransactionByDate(listOfTransactions, date):
    return [str(transaction) for transaction in listOfTransactions if transaction.date == date]
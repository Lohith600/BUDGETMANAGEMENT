import budget_logic

LoginDict={}
UserName=budget_logic.login(LoginDict)

listOfTransactions = []     #This list needs to be made from the UserName folder and then 
#                           accessing files

choice = None
choices = [0,1,2,3,4,5,7,8,9]

while True:
    while choice not in choices:
        print("=====Budget Planner=====")
        print("1. Add Transaction")
        print("2. Edit Transaction")
        print("3. Delete Transaction")
        print("4. Calculate Balance")
        print("5. View Expense Categories")
        print("6. Track Savings Progress")
        print("7. List Transactions")
        print("8. Find Transaction by Date")
        print("9. Logout")
        print("0. Exit")
        try:
            choice = int(input())
            if choice not in choices:
                print("Invalid choice, please enter a correct choice.")
        except ValueError:
            print("Invalid input, please enter a number.")
    if choice == 0:
        break
    elif choice == 1:
        budget_logic.add(listOfTransactions)
    elif choice == 2:
        budget_logic.edit(listOfTransactions)
    elif choice == 3:
        budget_logic.delete(listOfTransactions)
    elif choice == 4:
        balance = budget_logic.balance(listOfTransactions)
        print("Total Income:", balance[0])
        print("Total Expense:", balance[1])
        print("Balance:", balance[2])
    elif choice == 5:
        categories = budget_logic.categorize(listOfTransactions)
        print(categories)
    elif choice == 6:
        budget_logic.progress(listOfTransactions)
    elif choice == 7:
        transactions = budget_logic.describeTransactions(listOfTransactions)
        print(transactions)
    elif choice == 8:
        date = input("Enter the date in DD-MM-YYYY format: ")
        transactions = budget_logic.findTransactionByDate(listOfTransactions, date)
        print(transactions)
    elif choice == 9:
        UserName = budget_logic.login(LoginDict)
        listOfTransactions = [] #Now the Transactions need to be again accessed from the csv filesfrom
        #                     the respective UserName folder
    choice = None


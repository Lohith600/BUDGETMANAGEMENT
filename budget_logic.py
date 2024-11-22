from transaction import Transaction, Income, Expense, Savings

def add(listOfTransactions):
    choice=int(input("Enter the type of transaction\n1 for Income\n2 for Expense\n3 for Savings: "))
    amount=int(input("Enter the amount: "))
    date=input("Enter the transaction date: ")
    category=input("Enter the category of purchase: ")
    if choice==1:
        source=input("Enter the source of income: ")
        object=Income(amount,date,category,source)

    elif choice==2:
        expense_type=input("Enter the type of expense: ")
        object=Expense(amount,date,category,expense_type)

    elif choice==3:
        goal_name=input("Enter the name of the goal: ")
        target_amount=input("Enter the target amount: ")
        object=Savings(amount,date,category,goal_name,target_amount)

    listOfTransactions.append(object)

def delete(listOfTransactions):
    print("Index: Transaction:")
    j=1
    for i in listOfTransactions:
        print(j," ",i)
    choice=int(input("Enter the index of transaction to be deleted"))
    del listOfTransactions[choice]

def edit(listOfTransactions):
    print("Index: Transaction:")
    j=1
    for i in listOfTransactions:
        print(j," ",i)
    choice=int(input("Enter the index of transaction to edited"))
    
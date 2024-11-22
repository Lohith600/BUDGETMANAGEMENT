from transaction import Transaction, Income, Expense, Savings

def add():
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

    return object

def print1(index,transactions):
    print(transactions)

transactions=[]
transactions.append(add())
for i in transactions:
    print(i)
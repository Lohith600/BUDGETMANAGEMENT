import os, pickle, csv
from datetime import datetime


class Transaction:
    lst = []
    def __init__(self, amount, date, category):
        """
        Base class to represent a financial transaction.

        :param amount: float - Amount of the transaction.
        :param date: str - Date of the transaction (e.g., "YYYY-MM-DD").
        :param category: str - Category of the transaction (e.g., "Groceries", "Transportation").
        """
        self.amount = amount
        self.date = date
        self.category = category

    def __str__(self):
        """
        String representation of the transaction.
        """
        return f"Date: {self.date}, Category: {self.category}, Amount: Rs.{self.amount:.2f}"
    
    @classmethod
    def addTransaction(cls, transaction):
        cls.lst.append(transaction)

    @classmethod
    def replaceTransaction(cls, transaction, index):
        cls.lst[index] = transaction

    @classmethod
    def deleteTransaction(cls, index):
        return cls.lst.pop(index)

    @classmethod
    def loadTransactions(cls, username):
        file_path = f"{username}"
        if os.path.exists(file_path):
            file = open(file_path + '/transactions.pkl', 'rb')
            cls.lst = pickle.load(file)
        else:
            os.mkdir(file_path)
            file = open(file_path + '/transactions.pkl', 'wb')
            cls.lst = []
    
    @classmethod
    def saveTransactions(cls, username):
        with open(f"{username}/transactions.pkl", 'wb') as file:
            pickle.dump(cls.lst, file)

    @classmethod
    def saveToCSV(cls, username):
        with open(f"{username}/transactions.csv", mode="w", newline="") as file:
            writer = csv.writer(file)
            header = [
                "Transaction Type", 
                "Amount", 
                "Date", 
                "Category/Source", 
                "Expense Type/Goal", 
                "Target Amount"
            ]
            writer.writerow(header)

            for transaction in cls.lst:
                if isinstance(transaction, Income):
                    writer.writerow([
                        "Income",
                        transaction.amount,
                        transaction.date,
                        transaction.source,
                        "",
                        ""
                    ])
                elif isinstance(transaction, Expense):
                    writer.writerow([
                        "Expense",
                        transaction.amount,
                        transaction.date,
                        transaction.category,
                        transaction.expense_type,
                        ""
                    ])
                elif isinstance(transaction, Savings):
                    writer.writerow([
                        "Savings",
                        transaction.amount,
                        transaction.date,
                        transaction.goal,
                        "",
                        transaction.target_amount
                    ])
    
    @classmethod
    def sortByDate(cls):
        cls.lst.sort(
            key=lambda transaction: datetime.strptime(transaction.date, "%d-%m-%Y")
        )

    @classmethod
    def listTransactions(cls):
        if len(cls.lst) == 0:
            text = "No Transactions Yet."
        else:
            text = ""
            for i, transaction in enumerate(cls.lst):
                text += f"{i + 1}. {transaction}\n\n"
        return text

class Income(Transaction):
    def __init__(self, amount, date, source, category="Income"):
        """
        Subclass of Transaction for income.

        :param source: str - Source of income (e.g., "Salary", "Freelance").
        """
        super().__init__(amount, date, category)
        self.source = source

    def __str__(self):
        """
        String representation of the income transaction.
        """
        return f"[Income] Source: {self.source}, " + super().__str__()


class Expense(Transaction):
    def __init__(self, amount, date, category, expense_type):
        """
        Subclass of Transaction for expenses.

        :param expense_type: str - Type of expense (e.g., "Essential", "Non-Essential").
        """
        super().__init__(amount, date, category)
        self.expense_type = expense_type

    def __str__(self):
        """
        String representation of the expense transaction.
        """
        return f"[Expense] Type: {self.expense_type}, " + super().__str__()


class Savings(Transaction):
    def __init__(self, amount, date, goal, target_amount):
        """
        Subclass of Transaction for savings.

        :param goal: str - Name of the savings goal.
        :param target_amount: float - Target amount for the goal.
        """
        super().__init__(amount, date, category="Savings")
        self.goal = goal
        self.target_amount = target_amount

    def __str__(self):
        """
        String representation of the savings transaction.
        """
        #progress = self.progress()
        return f"[Savings] Goal: {self.goal}, " + super().__str__() + f"Target: {self.target_amount:.2f}"


class UserLoginDetail:
    LoginDict={}
    def __init__(self,Username,Password):
        self.username=Username
        self.password=Password

    def __str__(self):
        dict={}
        dict[self.username]=self.password
        return dict

    @classmethod
    def loadDict(cls):
        file_path = 'user_data.pkl'
        if os.path.exists(file_path):
            with open(file_path, 'rb') as file:
                cls.LoginDict = pickle.load(file)
        else:
            file = open(file_path, 'wb')
            cls.LoginDict = {}
    
    @classmethod
    def saveDict(cls):
        with open('user_data.pkl', 'wb') as file:
            pickle.dump(cls.LoginDict, file)

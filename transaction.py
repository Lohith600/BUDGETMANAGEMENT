class Transaction:
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
        return f"[Savings] Goal: {self.goal}, Target: {self.target_amount:.2f}, " + super().__str__()

class UserLoginDetail:
    LoginDict={}
    def __init__(self,Username,Password):
        self.username=Username
        self.password=Password
        UserLoginDetail.LoginDict[Username]=Password
    
    def __str__(self):
        dict={}
        dict[self.username]=self.password
        return dict

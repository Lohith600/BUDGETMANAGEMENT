from transaction import Transaction, Income, Expense, Savings
import os, pickle
import customtkinter as ctk
import tkinter.messagebox as tkmsg

def add_transaction_window(app,main_frame,listOfTransactions):
    
    # Hide the main frame
    main_frame.place_forget()

    # Create a new frame for Add Transaction
    add_transaction_frame = ctk.CTkFrame(app, width=400, height=500)
    add_transaction_frame.place(relx=0.4, rely=0.55, anchor="center")

    heading_label = ctk.CTkLabel(add_transaction_frame, text="Add Transaction", font=("Helvetica", 20, "bold"))
    heading_label.pack(pady=20)

    transaction_type_label = ctk.CTkLabel(add_transaction_frame, text="Transaction Type:")
    transaction_type_label.pack(pady=5)

    transaction_type_var = ctk.StringVar()
    transaction_type_dropdown = ctk.CTkOptionMenu(add_transaction_frame, values=["Income", "Expense", "Savings"],
                                                  variable=transaction_type_var)
    transaction_type_dropdown.pack(pady=5)

    amount_label = ctk.CTkLabel(add_transaction_frame, text="Amount:")
    amount_label.pack(pady=5)
    amount_entry = ctk.CTkEntry(add_transaction_frame, width=300)
    amount_entry.pack(pady=5)

    date_label = ctk.CTkLabel(add_transaction_frame, text="Date (DD-MM-YYYY):")
    date_label.pack(pady=5)
    date_entry = ctk.CTkEntry(add_transaction_frame, width=300)
    date_entry.pack(pady=5)

    details_label = ctk.CTkLabel(add_transaction_frame, text="Details (Source/Category/Goal):")
    details_label.pack(pady=5)
    details_entry = ctk.CTkEntry(add_transaction_frame, width=300)
    details_entry.pack(pady=5)

    additional_label = ctk.CTkLabel(add_transaction_frame, text="Type (for Expense) / Target (for Savings):")
    additional_label.pack(pady=5)
    additional_entry = ctk.CTkEntry(add_transaction_frame, width=300)
    additional_entry.pack(pady=5)

    def getList(username):
        file_path = f"{username}"
        if os.path.exists(file_path):
            file = open(file_path+'/transactions.pkl', 'rb')
            listOfTransactions = pickle.load(file)
        else:
            file = open(file_path+'/transactions.pkl', 'wb')
            listOfTransactions = []
        return listOfTransactions


    def save_transaction():
        transaction_type = transaction_type_var.get()
        amount = amount_entry.get()
        date = date_entry.get()
        details = details_entry.get()
        additional = additional_entry.get()

        try:
            amount = float(amount)
        except ValueError:
            tkmsg.showerror("Error", "Invalid amount entered!")
            return

        if not date or not transaction_type:
            tkmsg.showerror("Error", "Please fill all required fields!")
            return
        if transaction_type == "Income":
            transaction = Income(amount, date, details)
        elif transaction_type == "Expense":
            if not additional:
                tkmsg.showerror("Error", "Please specify the type of Expense!")
                return
            transaction = Expense(amount, date, details, additional)
        elif transaction_type == "Savings":
            try:
                target = float(additional)
                transaction = Savings(amount, date, details, target)
            except ValueError:
                tkmsg.showerror("Error", "Invalid target entered for Savings!")
                return
        else:
            tkmsg.showerror("Error", "Invalid transaction type!")
            return

        listOfTransactions.append(transaction)
        tkmsg.showinfo("Success", "Transaction added successfully!")
        back_to_main()

    save_button = ctk.CTkButton(add_transaction_frame, text="Save Transaction", height=40, width=200,
                                fg_color="#fff5ea", text_color="#924444", command=save_transaction)
    save_button.pack(pady=20)

    def back_to_main():
        add_transaction_frame.place_forget()
        main_frame.place(relx=0.4, rely=0.55, anchor="center")

    back_button = ctk.CTkButton(add_transaction_frame, text="Back", height=40, width=200,
                                fg_color="#fff5ea", text_color="#924444", command=back_to_main)
    back_button.pack(pady=10)
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
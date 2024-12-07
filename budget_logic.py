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

    heading_label = ctk.CTkLabel(add_transaction_frame, text="Edit Transaction", font=("Helvetica", 20, "bold"))
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
def edit_transaction(listofTransactions, app, main_frame):
    main_frame.place_forget()

    
    edit_transaction_frame = ctk.CTkFrame(app, width=810, height=600)
    edit_transaction_frame.place(relx=0.5, rely=0.6, anchor="center")  # Center the frame

    
    text1 = ""
    for i, transaction in enumerate(listofTransactions):
        text1 += f"{i + 1}. {transaction}\n"

    
    textbox_frame = ctk.CTkFrame(edit_transaction_frame, width=800, height=400)
    textbox_frame.pack(fill="both", expand=True, padx=10, pady=10)

    
    edit_textbox = ctk.CTkTextbox(textbox_frame, width=780, height=400)
    edit_textbox.grid(row=0, column=0, sticky="nsew")
    edit_textbox.insert("0.0", text1)
    edit_textbox.configure(state="disabled")

    
    textbox_frame.grid_rowconfigure(0, weight=1)
    textbox_frame.grid_columnconfigure(0, weight=1)

    
    scrollbar = ctk.CTkScrollbar(textbox_frame, command=edit_textbox.yview)
    scrollbar.grid(row=0, column=1, sticky="ns")
    edit_textbox.configure(yscrollcommand=scrollbar.set)

    
    input_frame = ctk.CTkFrame(edit_transaction_frame, width=800, height=100)
    input_frame.pack(fill="x", pady=(0, 10))  # Place directly below the textbox

    
    label1 = ctk.CTkLabel(input_frame, text="Enter the transaction number you want to edit:")
    label1.grid(row=0, column=0, padx=(20, 10), pady=10, sticky="w")

    
    trans_entry = ctk.CTkEntry(input_frame, width=50)
    trans_entry.place(relx=0.4, rely=0.2)

    
    def edit_trans(app, x, listOfTransactions):
        
        edit_transaction_frame.place_forget()

        
        add_transaction_frame = ctk.CTkFrame(app, width=400, height=500)
        add_transaction_frame.place(relx=0.4, rely=0.55, anchor="center")

        heading_label = ctk.CTkLabel(add_transaction_frame, text="Edit Transaction", font=("Helvetica", 20, "bold"))
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

            listOfTransactions[x-1] = transaction
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

    # Check input and proceed on enter press
    def check():
        num = trans_entry.get()
        try:
            num = int(num)
            if num <= 0 or num > len(listofTransactions):
                tkmsg.showinfo("Transaction not found", "The transaction number you entered does not exist.")
            else:
                edit_trans(app, num, listofTransactions)
        except ValueError:
            tkmsg.showinfo("Invalid input", "Please enter a valid number.")

    trans_entry.bind('<Return>', lambda event: check())
    
def delete_transaction(app,main_frame,listofTransactions):
    main_frame.place_forget()
    del_transaction_frame = ctk.CTkFrame(app, width=810, height=600)
    del_transaction_frame.place(relx=0.5, rely=0.6, anchor="center")  # Center the frame

    
    text1 = ""
    for i, transaction in enumerate(listofTransactions):
        text1 += f"{i + 1}. {transaction}\n"

    
    textbox_frame = ctk.CTkFrame(del_transaction_frame, width=800, height=400)
    textbox_frame.pack(fill="both", expand=True, padx=10, pady=10)

    
    edit_textbox = ctk.CTkTextbox(textbox_frame, width=780, height=400)
    edit_textbox.grid(row=0, column=0, sticky="nsew")
    edit_textbox.insert("0.0", text1)
    edit_textbox.configure(state="disabled")

    
    textbox_frame.grid_rowconfigure(0, weight=1)
    textbox_frame.grid_columnconfigure(0, weight=1)

    
    scrollbar = ctk.CTkScrollbar(textbox_frame, command=edit_textbox.yview)
    scrollbar.grid(row=0, column=1, sticky="ns")
    edit_textbox.configure(yscrollcommand=scrollbar.set)

    
    input_frame = ctk.CTkFrame(del_transaction_frame, width=800, height=100)
    input_frame.pack(fill="x", pady=(0, 10))  # Place directly below the textbox

    
    label1 = ctk.CTkLabel(input_frame, text="Enter the transaction number you want to delete:")
    label1.grid(row=0, column=0, padx=(20, 10), pady=10, sticky="w")

    
    trans_entry = ctk.CTkEntry(input_frame, width=50)
    trans_entry.place(relx=0.4, rely=0.2)

    
    def del_trans( x, listOfTransactions):
        del(listOfTransactions[x-1])
        tkmsg.showinfo("Deleted","Successfully deleted transaction")
        def back_to_main():
            del_transaction_frame.place_forget()
            main_frame.place(relx=0.4, rely=0.55, anchor="center")
        back_to_main()



    # Check input and proceed on enter press
    def check():
        num = trans_entry.get()
        try:
            num = int(num)
            if num <= 0 or num > len(listofTransactions):
                tkmsg.showinfo("Transaction not found", "The transaction number you entered does not exist.")
            else:
                del_trans( num, listofTransactions)
        except ValueError:
            tkmsg.showinfo("Invalid input", "Please enter a valid number.")

    trans_entry.bind('<Return>', lambda event: check())
def list_transactions(app, main_frame, listofTransactions):
    main_frame.place_forget()

    list_transaction_frame = ctk.CTkFrame(app, width=810, height=600)
    list_transaction_frame.place(relx=0.5, rely=0.6, anchor="center")  # Center the frame

    text1 = ""
    for i, transaction in enumerate(listofTransactions):
        text1 += f"{i + 1}. {transaction}\n"

    textbox_frame = ctk.CTkFrame(list_transaction_frame, width=800, height=400)
    textbox_frame.pack(fill="both", expand=True, padx=10, pady=10)

    edit_textbox = ctk.CTkTextbox(textbox_frame, width=780, height=400)
    edit_textbox.grid(row=0, column=0, sticky="nsew")
    edit_textbox.insert("0.0", text1)
    edit_textbox.configure(state="disabled")

    textbox_frame.grid_rowconfigure(0, weight=1)
    textbox_frame.grid_columnconfigure(0, weight=1)

    scrollbar = ctk.CTkScrollbar(textbox_frame, command=edit_textbox.yview)
    scrollbar.grid(row=0, column=1, sticky="ns")
    edit_textbox.configure(yscrollcommand=scrollbar.set)

    input_frame = ctk.CTkFrame(list_transaction_frame, width=800, height=100)
    input_frame.pack(fill="x", pady=(0, 10))

    def back_to_main():
        list_transaction_frame.place_forget()
        main_frame.place(relx=0.4, rely=0.55, anchor="center")

    button = ctk.CTkButton(input_frame, text="Back", command=back_to_main)
    button.pack(pady=10)  # Place directly below the textbox

    
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
    ############should be worked upon
    pass


def describeTransactions(listOfTransactions):
    return [str(transaction) for transaction in listOfTransactions]


def findTransactionByDate(listOfTransactions, date):
    return [str(transaction) for transaction in listOfTransactions if transaction.date == date]
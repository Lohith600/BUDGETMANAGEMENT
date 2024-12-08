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

    if len(listofTransactions) == 0:
        text1 = "no transaction yet"
    else:
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
    trans_entry.grid(row=0, column=1, padx=(10, 20), pady=10)

    def back_to_main():
        edit_transaction_frame.place_forget()
        main_frame.place(relx=0.4, rely=0.55, anchor="center")

    # Back button to return to main frame
    back_button = ctk.CTkButton(input_frame, text="Back", command=back_to_main)
    back_button.grid(row=0, column=2, padx=30, pady=10)

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

            listOfTransactions[x - 1] = transaction
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

def delete_transaction(app, main_frame, listofTransactions):
    main_frame.place_forget()

    # Main frame for delete transaction
    del_transaction_frame = ctk.CTkFrame(app, width=810, height=600)
    del_transaction_frame.place(relx=0.5, rely=0.6, anchor="center")  # Center the frame

    # Display list of transactions or a message if none exist
    if len(listofTransactions) == 0:
        text1 = "No transactions yet."
    else:
        text1 = ""
        for i, transaction in enumerate(listofTransactions):
            text1 += f"{i + 1}. {transaction}\n"

    # Textbox frame
    textbox_frame = ctk.CTkFrame(del_transaction_frame, width=800, height=400)
    textbox_frame.pack(fill="both", expand=True, padx=10, pady=10)

    # Textbox for displaying transactions
    edit_textbox = ctk.CTkTextbox(textbox_frame, width=780, height=400)
    edit_textbox.grid(row=0, column=0, sticky="nsew")
    edit_textbox.insert("0.0", text1)
    edit_textbox.configure(state="disabled")

    textbox_frame.grid_rowconfigure(0, weight=1)
    textbox_frame.grid_columnconfigure(0, weight=1)

    # Scrollbar for the textbox
    scrollbar = ctk.CTkScrollbar(textbox_frame, command=edit_textbox.yview)
    scrollbar.grid(row=0, column=1, sticky="ns")
    edit_textbox.configure(yscrollcommand=scrollbar.set)

    # Input frame for entering transaction number and back button
    input_frame = ctk.CTkFrame(del_transaction_frame, width=800, height=100)
    input_frame.pack(fill="x", pady=(0, 10))

    # Label for transaction input
    label1 = ctk.CTkLabel(input_frame, text="Enter the transaction number you want to delete:")
    label1.grid(row=0, column=0, padx=(20, 10), pady=10, sticky="w")

    # Entry widget for transaction input
    trans_entry = ctk.CTkEntry(input_frame, width=200)
    trans_entry.grid(row=0, column=1, padx=10, pady=10, sticky="w")

    # Function to return to the main frame
    def back_to_main():
        del_transaction_frame.place_forget()
        main_frame.place(relx=0.4, rely=0.55, anchor="center")

    # Back button to return to main frame
    back_button = ctk.CTkButton(input_frame, text="Back", command=back_to_main)
    back_button.grid(row=0, column=2, padx=10, pady=10)


def list_transactions(app, main_frame, listofTransactions):
    main_frame.place_forget()

    list_transaction_frame = ctk.CTkFrame(app, width=810, height=600)
    list_transaction_frame.place(relx=0.5, rely=0.6, anchor="center")  # Center the frame
    if len(listofTransactions)==0:
        text1="no transaction yet"
    else:
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

def calculate_balance(app, main_frame, listofTransactions):
    # Hide the main frame
    main_frame.place_forget()

    # Function to calculate total income, expenses, and balance
    def calculate_totals(transactions):
        totalIncome = sum(transaction.amount for transaction in transactions if isinstance(transaction, Income))
        totalExpense = sum(transaction.amount for transaction in transactions if isinstance(transaction, Expense))
        return totalIncome, totalExpense, totalIncome - totalExpense

    # Perform the calculation
    totalIncome, totalExpense, netBalance = calculate_totals(listofTransactions)

    # Create a new frame for displaying the balance
    balance_frame = ctk.CTkFrame(app, height=600, width=500)
    balance_frame.place(relx=0.35, rely=0.5, anchor="center")

    # Create the textbox to display the balance details
    box = ctk.CTkTextbox(balance_frame, width=400, height=300)
    box.place(relx=0.5, rely=0.3, anchor="center")
    box.configure(font=("Arial", 22))  # Center the textbox
    box.insert(
        "0.0",
        f"Your total income is: {totalIncome}\n\n\n"
        f"Your total expense is: {totalExpense}\n\n\n"
        f"Your net balance is: {netBalance}"
    )
    box.configure(state="disabled")  # Make the textbox read-only

    # Function to go back to the main frame
    def back_to_main():
        balance_frame.place_forget()
        main_frame.place(relx=0.4, rely=0.55, anchor="center")

    # Add a "Back" button to return to the main frame
    back_button = ctk.CTkButton(balance_frame, text="Back", command=back_to_main)
    back_button.place(relx=0.5, rely=0.8, anchor="center")  # Center the button
def transaction_by_date(app, main_frame, listofTransactions):
    # Hide the main frame
    main_frame.place_forget()

    # Create the display frame
    display = ctk.CTkFrame(app, width=700, height=600)
    display.place(relx=0.5, rely=0.5, anchor="center")

    # Instruction textbox at the top
    instruction_textbox = ctk.CTkTextbox(display, height=50, width=600,font=("Arial", 16))
    instruction_textbox.place(relx=0.5, rely=0.1, anchor="center")
    instruction_textbox.insert("0.0", "                      Enter  the  date  in  the  DD-MM-YYYY  format")
    instruction_textbox.configure(state="disabled")

    # Label for entering the date
    label1 = ctk.CTkLabel(display, text="Enter the transaction date:")
    label1.place(relx=0.3, rely=0.2, anchor="center")

    # Entry for the user to input the date
    date_entry = ctk.CTkEntry(display, width=200)
    date_entry.place(relx=0.6, rely=0.2, anchor="center")

    # Function to display transactions by date
    def print_transaction():
        x = date_entry.get()  # Get user input
        text1 = ""

        # Search for transactions with the given date
        for transaction in listofTransactions:
            if transaction.date == x:
                text1 += str(transaction) + "\n"

        # If no transactions found, show a message
        if not text1:
            text1 = "Transaction on the date does not exist."

        # Display results in a textbox
        result_textbox = ctk.CTkTextbox(display, width=600, height=300)
        result_textbox.place(relx=0.5, rely=0.6, anchor="center")
        result_textbox.insert("0.0", text1)
        result_textbox.configure(state="disabled")  # Make textbox read-only

    # Button to trigger the search
    search_button = ctk.CTkButton(display, text="Search", command=print_transaction)
    search_button.place(relx=0.5, rely=0.3, anchor="center")

    # Function to return to the main frame
    def back_to_main():
        display.place_forget()
        main_frame.place(relx=0.4, rely=0.55, anchor="center")

    # Button to go back to the main frame
    back_button = ctk.CTkButton(display, text="Back", command=back_to_main)
    back_button.place(relx=0.5, rely=0.9, anchor="center")

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
    ########tell akshat to work on this 
    pass


def describeTransactions(listOfTransactions):
    return [str(transaction) for transaction in listOfTransactions]


def findTransactionByDate(listOfTransactions, date):
    return [str(transaction) for transaction in listOfTransactions if transaction.date == date]
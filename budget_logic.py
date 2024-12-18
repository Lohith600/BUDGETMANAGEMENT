from transaction import Transaction, Income, Expense, Savings
import os, pickle
import customtkinter as ctk
import tkinter.messagebox as tkmsg

import re

class BudgetPlanner:
    def checkDate(date):
        if re.match(r'^\d{2}\d{2}\d{4}$', date):  
            s = date
            day = int(s[0:2])
            month = int(s[2:4])
            year = int(s[4:8])
            if year % 4 == 0:
                if year % 100 == 0:
                    if year % 400 == 0:
                        leap = 1
                    else:
                        leap = 0 
                else:
                    leap = 1
            else:
                leap = 0 

            if month in [1,3,5,7,8,10,12]:
                if day in range(1,32):
                    return s[0:2] + '-' + s[2:4] + '-' + s[4:8]
            elif month in [4,6,9,11]:
                if day in range(1,31):
                    return s[0:2] + '-' + s[2:4] + '-' + s[4:8]
            elif month == 2:
                if day in range(1,29+leap):
                    return s[0:2] + '-' + s[2:4] + '-' + s[4:8]
        return None

    def add_transaction_window(app, main_frame):
        
        
        main_frame.place_forget()

        
        add_transaction_frame = ctk.CTkFrame(app, width=400, height=600)
        add_transaction_frame.place(relx=0.4, rely=0.5, anchor="center")
        def Income1():
            add_transaction_frame.place_forget()
            Incomeframe=ctk.CTkFrame(app,width=400,height=500)
            Incomeframe.place(relx=0.4, rely=0.675, anchor="center")
            amount_label = ctk.CTkLabel(Incomeframe, text="Amount:")
            amount_label.pack(pady=5)
            amount_entry = ctk.CTkEntry(Incomeframe, width=300)
            amount_entry.pack(pady=5)

            date_label = ctk.CTkLabel(Incomeframe, text="Date (DDMMYYYY):")
            date_label.pack(pady=5)
            date_entry = ctk.CTkEntry(Incomeframe, width=300)
            date_entry.pack(pady=5)

            details_label = ctk.CTkLabel(Incomeframe, text="Details (Source/Category/Goal):")
            details_label.pack(pady=5)
            details_entry = ctk.CTkEntry(Incomeframe, width=300)
            details_entry.pack(pady=5)

            


            def save_transaction():
                transaction_type="Income"
                amount = amount_entry.get()
                date = date_entry.get()
                details = details_entry.get()
                

                try:
                    amount = float(amount)
                except ValueError:
                    tkmsg.showerror("Error", "Invalid amount entered!")
                    return

                if not date or not transaction_type:
                    tkmsg.showerror("Error", "Please fill all required fields!")
                    return

                
                validated_date = BudgetPlanner.checkDate(date)
                if not validated_date:
                    tkmsg.showerror("Error", "Invalid date format! Please use DDMMYYYY.")
                    return

                if transaction_type == "Income":
                    transaction = Income(amount, validated_date, details)
                else:
                    tkmsg.showerror("Error", "Invalid transaction type!")
                    return

                Transaction.addTransaction(transaction)
                tkmsg.showinfo("Success", "Transaction added successfully!")
                back_to_main()

            save_button = ctk.CTkButton(Incomeframe, text="Save Transaction", height=40, width=200,
                                        fg_color="#fff5ea", text_color="#924444", command=save_transaction)
            save_button.pack(pady=20)

            def back_to_main():
                Incomeframe.place_forget()
                main_frame.place(relx=0.4, rely=0.55, anchor="center")

            back_button = ctk.CTkButton(Incomeframe, text="Back", height=40, width=200,
                                        fg_color="#fff5ea", text_color="#924444", command=back_to_main)
            back_button.pack(pady=10)
        def Expense1():
            add_transaction_frame.place_forget()
            Incomeframe=ctk.CTkFrame(app,width=400,height=500)
            Incomeframe.place(relx=0.4, rely=0.675, anchor="center")
            amount_label = ctk.CTkLabel(Incomeframe, text="Amount:")
            amount_label.pack(pady=5)
            amount_entry = ctk.CTkEntry(Incomeframe, width=300)
            amount_entry.pack(pady=5)

            date_label = ctk.CTkLabel(Incomeframe, text="Date (DDMMYYYY):")
            date_label.pack(pady=5)
            date_entry = ctk.CTkEntry(Incomeframe, width=300)
            date_entry.pack(pady=5)

            details_label = ctk.CTkLabel(Incomeframe, text="Details (Source/Category/Goal):")
            details_label.pack(pady=5)
            details_entry = ctk.CTkEntry(Incomeframe, width=300)
            details_entry.pack(pady=5)

            additional_label = ctk.CTkLabel(Incomeframe, text="Type (for Expense) / Target (for Savings):")
            additional_label.pack(pady=5)
            additional_entry = ctk.CTkEntry(Incomeframe, width=300)
            additional_entry.pack(pady=5)


            def save_transaction():
                transaction_type="Expense"
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

                
                validated_date = BudgetPlanner.checkDate(date)
                if not validated_date:
                    tkmsg.showerror("Error", "Invalid date format! Please use DDMMYYYY.")
                    return

                if transaction_type == "Income":
                    transaction = Income(amount, validated_date, details)
                elif transaction_type == "Expense":
                    if not additional:
                        tkmsg.showerror("Error", "Please specify the type of Expense!")
                        return
                    transaction = Expense(amount, validated_date, details, additional)
                elif transaction_type == "Savings":
                    try:
                        target = float(additional)
                        transaction = Savings(amount, validated_date, details, target)
                        for obj in Transaction.lst:
                                if isinstance(obj, Savings):
                                    if obj.goal == details:
                                        obj.target_amount = target
                    except ValueError:
                        tkmsg.showerror("Error", "Invalid target entered for Savings!")
                        return
                else:
                    tkmsg.showerror("Error", "Invalid transaction type!")
                    return

                Transaction.addTransaction(transaction)
                tkmsg.showinfo("Success", "Transaction added successfully!")
                back_to_main()

            save_button = ctk.CTkButton(Incomeframe, text="Save Transaction", height=40, width=200,
                                        fg_color="#fff5ea", text_color="#924444", command=save_transaction)
            save_button.pack(pady=20)

            def back_to_main():
                Incomeframe.place_forget()
                main_frame.place(relx=0.4, rely=0.55, anchor="center")

            back_button = ctk.CTkButton(Incomeframe, text="Back", height=40, width=200,
                                        fg_color="#fff5ea", text_color="#924444", command=back_to_main)
            back_button.pack(pady=10)
        def Savings1():
            add_transaction_frame.place_forget()
            Incomeframe=ctk.CTkFrame(app,width=400,height=500)
            Incomeframe.place(relx=0.4, rely=0.675, anchor="center")
            amount_label = ctk.CTkLabel(Incomeframe, text="Amount:")
            amount_label.pack(pady=5)
            amount_entry = ctk.CTkEntry(Incomeframe, width=300)
            amount_entry.pack(pady=5)

            date_label = ctk.CTkLabel(Incomeframe, text="Date (DDMMYYYY):")
            date_label.pack(pady=5)
            date_entry = ctk.CTkEntry(Incomeframe, width=300)
            date_entry.pack(pady=5)

            details_label = ctk.CTkLabel(Incomeframe, text="Details (Source/Category/Goal):")
            details_label.pack(pady=5)
            details_entry = ctk.CTkEntry(Incomeframe, width=300)
            details_entry.pack(pady=5)

            additional_label = ctk.CTkLabel(Incomeframe, text="Type (for Expense) / Target (for Savings):")
            additional_label.pack(pady=5)
            additional_entry = ctk.CTkEntry(Incomeframe, width=300)
            additional_entry.pack(pady=5)


            def save_transaction():
                transaction_type="Savings"
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

                
                validated_date = BudgetPlanner.checkDate(date)
                if not validated_date:
                    tkmsg.showerror("Error", "Invalid date format! Please use DDMMYYYY.")
                    return

                if transaction_type == "Income":
                    transaction = Income(amount, validated_date, details)
                elif transaction_type == "Expense":
                    if not additional:
                        tkmsg.showerror("Error", "Please specify the type of Expense!")
                        return
                    transaction = Expense(amount, validated_date, details, additional)
                elif transaction_type == "Savings":
                    try:
                        target = float(additional)
                        transaction = Savings(amount, validated_date, details, target)
                    except ValueError:
                        tkmsg.showerror("Error", "Invalid target entered for Savings!")
                        return
                else:
                    tkmsg.showerror("Error", "Invalid transaction type!")
                    return

                Transaction.addTransaction(transaction)
                tkmsg.showinfo("Success", "Transaction added successfully!")
                back_to_main()

            save_button = ctk.CTkButton(Incomeframe, text="Save Transaction", height=40, width=200,
                                        fg_color="#fff5ea", text_color="#924444", command=save_transaction)
            save_button.pack(pady=20)

            def back_to_main():
                Incomeframe.place_forget()
                main_frame.place(relx=0.4, rely=0.55, anchor="center")

            back_button = ctk.CTkButton(Incomeframe, text="Back", height=40, width=200,
                                        fg_color="#fff5ea", text_color="#924444", command=back_to_main)
            back_button.pack(pady=10)
        def back_button1():
            add_transaction_frame.place_forget()
            main_frame.place(relx=0.4, rely=0.55, anchor="center")

        back_button=ctk.CTkButton(add_transaction_frame,text="Back",command=back_button1)
        button1=ctk.CTkButton(add_transaction_frame,text="Income",command=Income1)
        button2=ctk.CTkButton(add_transaction_frame,text="Expense",command=Expense1)
        button3=ctk.CTkButton(add_transaction_frame,text="Savings",command=Savings1)
        button1.place(relx=0.35,rely=0.3)
        button2.place(relx=0.35,rely=0.5)
        button3.place(relx=0.35,rely=0.7)
        back_button.place(relx=0.35,rely=0.9)


    def edit_transaction(app, main_frame):
        main_frame.place_forget()

        edit_transaction_frame = ctk.CTkFrame(app, width=810, height=600)
        edit_transaction_frame.place(relx=0.5, rely=0.6, anchor="center")  # Center the frame

        Transaction.sortByDate()
        text1 = Transaction.listTransactions()

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
        input_frame.pack(fill="x", pady=(0, 10))  

        label1 = ctk.CTkLabel(input_frame, text="Enter the transaction number you want to edit:")
        label1.grid(row=0, column=0, padx=(20, 10), pady=10, sticky="w")

        trans_entry = ctk.CTkEntry(input_frame, width=50)
        trans_entry.grid(row=0, column=1, padx=(10, 20), pady=10)

        def check():
            num = trans_entry.get()
            try:
                num = int(num)
                if num <= 0 or num > len(Transaction.lst):
                    tkmsg.showinfo("Transaction not found", "The transaction number you entered does not exist.")
                else:
                    edit_trans(app, num)
            except ValueError:
                tkmsg.showinfo("Invalid input", "Please enter a valid number.")

        check_button = ctk.CTkButton(input_frame, text="Edit", command=check)
        check_button.grid(row=0, column=3, padx=(10, 20), pady=10)

        def back_to_main():
            edit_transaction_frame.place_forget()
            main_frame.place(relx=0.4, rely=0.55, anchor="center")

        
        back_button = ctk.CTkButton(input_frame, text="Back", command=back_to_main)
        back_button.grid(row=0, column=2, padx=30, pady=10)

        def edit_trans(app, x):
            edit_transaction_frame.place_forget()

        
            add_transaction_frame = ctk.CTkFrame(app, width=400, height=600)
            add_transaction_frame.place(relx=0.4, rely=0.5, anchor="center")
            def Income1():
                add_transaction_frame.place_forget()
                Incomeframe=ctk.CTkFrame(app,width=400,height=500)
                Incomeframe.place(relx=0.4, rely=0.675, anchor="center")
                amount_label = ctk.CTkLabel(Incomeframe, text="Amount:")
                amount_label.pack(pady=5)
                amount_entry = ctk.CTkEntry(Incomeframe, width=300)
                amount_entry.pack(pady=5)

                date_label = ctk.CTkLabel(Incomeframe, text="Date (DDMMYYYY):")
                date_label.pack(pady=5)
                date_entry = ctk.CTkEntry(Incomeframe, width=300)
                date_entry.pack(pady=5)

                details_label = ctk.CTkLabel(Incomeframe, text="Details (Source/Category/Goal):")
                details_label.pack(pady=5)
                details_entry = ctk.CTkEntry(Incomeframe, width=300)
                details_entry.pack(pady=5)

                


                def save_transaction():
                    transaction_type="Income"
                    amount = amount_entry.get()
                    date = date_entry.get()
                    details = details_entry.get()
                    

                    try:
                        amount = float(amount)
                    except ValueError:
                        tkmsg.showerror("Error", "Invalid amount entered!")
                        return

                    if not date or not transaction_type:
                        tkmsg.showerror("Error", "Please fill all required fields!")
                        return

                    
                    validated_date = BudgetPlanner.checkDate(date)
                    if not validated_date:
                        tkmsg.showerror("Error", "Invalid date format! Please use DDMMYYYY.")
                        return

                    if transaction_type == "Income":
                        transaction = Income(amount, validated_date, details)
                    else:
                        tkmsg.showerror("Error", "Invalid transaction type!")
                        return

                    Transaction.replaceTransaction(transaction, x-1)
                    tkmsg.showinfo("Success", "Transaction edited successfully!")
                    back_to_main()

                save_button = ctk.CTkButton(Incomeframe, text="Save Transaction", height=40, width=200,
                                            fg_color="#fff5ea", text_color="#924444", command=save_transaction)
                save_button.pack(pady=20)

                def back_to_main():
                    Incomeframe.place_forget()
                    main_frame.place(relx=0.4, rely=0.55, anchor="center")

                back_button = ctk.CTkButton(Incomeframe, text="Back", height=40, width=200,
                                            fg_color="#fff5ea", text_color="#924444", command=back_to_main)
                back_button.pack(pady=10)
            def Expense1():
                add_transaction_frame.place_forget()
                Incomeframe=ctk.CTkFrame(app,width=400,height=500)
                Incomeframe.place(relx=0.4, rely=0.675, anchor="center")
                amount_label = ctk.CTkLabel(Incomeframe, text="Amount:")
                amount_label.pack(pady=5)
                amount_entry = ctk.CTkEntry(Incomeframe, width=300)
                amount_entry.pack(pady=5)

                date_label = ctk.CTkLabel(Incomeframe, text="Date (DDMMYYYY):")
                date_label.pack(pady=5)
                date_entry = ctk.CTkEntry(Incomeframe, width=300)
                date_entry.pack(pady=5)

                details_label = ctk.CTkLabel(Incomeframe, text="Details (Source/Category/Goal):")
                details_label.pack(pady=5)
                details_entry = ctk.CTkEntry(Incomeframe, width=300)
                details_entry.pack(pady=5)

                additional_label = ctk.CTkLabel(Incomeframe, text="Type (for Expense) / Target (for Savings):")
                additional_label.pack(pady=5)
                additional_entry = ctk.CTkEntry(Incomeframe, width=300)
                additional_entry.pack(pady=5)


                def save_transaction():
                    transaction_type="Expense"
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
                    
                    validated_date = BudgetPlanner.checkDate(date)
                    if not validated_date:
                        tkmsg.showerror("Error", "Invalid date format! Please use DDMMYYYY.")
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
                            for obj in Transaction.lst:
                                if isinstance(obj, Savings):
                                    if obj.goal == details:
                                        obj.target_amount = target
                        except ValueError:
                            tkmsg.showerror("Error", "Invalid target entered for Savings!")
                            return
                    else:
                        tkmsg.showerror("Error", "Invalid transaction type!")
                        return
                    
                    Transaction.replaceTransaction(transaction, x-1)
                    tkmsg.showinfo("Success", "Transaction edited successfully!")
                    back_to_main()

                save_button = ctk.CTkButton(Incomeframe, text="Save Transaction", height=40, width=200,
                                            fg_color="#fff5ea", text_color="#924444", command=save_transaction)
                save_button.pack(pady=20)

                def back_to_main():
                    Incomeframe.place_forget()
                    main_frame.place(relx=0.4, rely=0.55, anchor="center")

                back_button = ctk.CTkButton(Incomeframe, text="Back", height=40, width=200,
                                            fg_color="#fff5ea", text_color="#924444", command=back_to_main)
                back_button.pack(pady=10)
            def Savings1():
                add_transaction_frame.place_forget()
                Incomeframe=ctk.CTkFrame(app,width=400,height=500)
                Incomeframe.place(relx=0.4, rely=0.675, anchor="center")
                amount_label = ctk.CTkLabel(Incomeframe, text="Amount:")
                amount_label.pack(pady=5)
                amount_entry = ctk.CTkEntry(Incomeframe, width=300)
                amount_entry.pack(pady=5)

                date_label = ctk.CTkLabel(Incomeframe, text="Date (DDMMYYYY):")
                date_label.pack(pady=5)
                date_entry = ctk.CTkEntry(Incomeframe, width=300)
                date_entry.pack(pady=5)

                details_label = ctk.CTkLabel(Incomeframe, text="Details (Source/Category/Goal):")
                details_label.pack(pady=5)
                details_entry = ctk.CTkEntry(Incomeframe, width=300)
                details_entry.pack(pady=5)

                additional_label = ctk.CTkLabel(Incomeframe, text="Type (for Expense) / Target (for Savings):")
                additional_label.pack(pady=5)
                additional_entry = ctk.CTkEntry(Incomeframe, width=300)
                additional_entry.pack(pady=5)


                def save_transaction():
                    transaction_type="Savings"
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

                    
                    validated_date = BudgetPlanner.checkDate(date)
                    if not validated_date:
                        tkmsg.showerror("Error", "Invalid date format! Please use DDMMYYYY.")
                        return

                    if transaction_type == "Income":
                        transaction = Income(amount, validated_date, details)
                    elif transaction_type == "Expense":
                        if not additional:
                            tkmsg.showerror("Error", "Please specify the type of Expense!")
                            return
                        transaction = Expense(amount, validated_date, details, additional)
                    elif transaction_type == "Savings":
                        try:
                            target = float(additional)
                            transaction = Savings(amount, validated_date, details, target)
                        except ValueError:
                            tkmsg.showerror("Error", "Invalid target entered for Savings!")
                            return
                    else:
                        tkmsg.showerror("Error", "Invalid transaction type!")
                        return

                    Transaction.replaceTransaction(transaction,x-1)
                    tkmsg.showinfo("Success", "Transaction edited successfully!")
                    back_to_main()

                save_button = ctk.CTkButton(Incomeframe, text="Save Transaction", height=40, width=200,
                                            fg_color="#fff5ea", text_color="#924444", command=save_transaction)
                save_button.pack(pady=20)

                def back_to_main():
                    Incomeframe.place_forget()
                    main_frame.place(relx=0.4, rely=0.55, anchor="center")

                back_button = ctk.CTkButton(Incomeframe, text="Back", height=40, width=200,
                                            fg_color="#fff5ea", text_color="#924444", command=back_to_main)
                back_button.pack(pady=10)
            def back_button1():
                add_transaction_frame.place_forget()
                main_frame.place(relx=0.4, rely=0.55, anchor="center")

            back_button=ctk.CTkButton(add_transaction_frame,text="Back",command=back_button1)
            button1=ctk.CTkButton(add_transaction_frame,text="income",command=Income1)
            button2=ctk.CTkButton(add_transaction_frame,text="expense",command=Expense1)
            button3=ctk.CTkButton(add_transaction_frame,text="savings",command=Savings1)
            button1.place(relx=0.35,rely=0.3)
            button2.place(relx=0.35,rely=0.5)
            button3.place(relx=0.35,rely=0.7)
            back_button.place(relx=0.35,rely=0.9)


    def delete_transaction(app, main_frame):
        main_frame.place_forget()

        
        del_transaction_frame = ctk.CTkFrame(app, width=810, height=600)
        del_transaction_frame.place(relx=0.5, rely=0.6, anchor="center")  

        Transaction.sortByDate
        text1 = Transaction.listTransactions()

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
        input_frame.pack(fill="x", pady=(0, 10))

        
        label1 = ctk.CTkLabel(input_frame, text="Enter the transaction number you want to delete:")
        label1.grid(row=0, column=0, padx=(20, 10), pady=10, sticky="w")

        
        trans_entry = ctk.CTkEntry(input_frame, width=200)
        trans_entry.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        
        def delete_trans():
            num = trans_entry.get()
            try:
                num = int(num)
                if num <= 0 or num > len(Transaction.lst):
                    tkmsg.showinfo("Transaction not found", "The transaction number you entered does not exist.")
                else:
                    deleted_transaction = Transaction.deleteTransaction(num-1)
                    tkmsg.showinfo("Success", f"Transaction {num} deleted: {deleted_transaction}")
                    back_to_main()
            except ValueError:
                tkmsg.showinfo("Invalid input", "Please enter a valid number.")

        
        delete_button = ctk.CTkButton(input_frame, text="Delete", command=delete_trans)
        delete_button.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

        
        def back_to_main():
            del_transaction_frame.place_forget()
            main_frame.place(relx=0.4, rely=0.55, anchor="center")

        
        back_button = ctk.CTkButton(input_frame, text="Back", command=back_to_main)
        back_button.grid(row=1, column=2, padx=10, pady=10, sticky="ew")

        
        input_frame.grid_columnconfigure(0, weight=1)
        input_frame.grid_columnconfigure(1, weight=1)
        input_frame.grid_columnconfigure(2, weight=1)

    def calculate_balance(app, main_frame):
        
        main_frame.place_forget()

        
        def calculate_totals(transactions):
            totalIncome = sum(transaction.amount for transaction in transactions if isinstance(transaction, Income))
            totalExpense = sum(transaction.amount for transaction in transactions if isinstance(transaction, Expense))
            totalSavings = sum(transaction.amount for transaction in transactions if isinstance(transaction, Savings))
            return totalIncome, totalExpense, totalIncome - totalExpense - totalSavings, totalSavings

        
        totalIncome, totalExpense, netBalance, totalSavings = calculate_totals(Transaction.lst)

        
        balance_frame = ctk.CTkFrame(app, height=600, width=500)
        balance_frame.place(relx=0.35, rely=0.5, anchor="center")

        
        box = ctk.CTkTextbox(balance_frame, width=400, height=300)
        box.place(relx=0.5, rely=0.3, anchor="center")
        box.configure(font=("Arial", 22))  
        box.insert(
            "0.0",
            f"Your Total Income is: {totalIncome}\n\n\n"
            f"Your Total Expense is: {totalExpense}\n\n\n"
            f"Your Total Savings are: {totalSavings}\n\n\n"
            f"Your Net Balance is: {netBalance}"
        )
        box.configure(state="disabled")  

        
        def back_to_main():
            balance_frame.place_forget()
            main_frame.place(relx=0.4, rely=0.55, anchor="center")

        
        back_button = ctk.CTkButton(balance_frame, text="Back", command=back_to_main)
        back_button.place(relx=0.5, rely=0.8, anchor="center")  
    def transaction_by_date(app, main_frame):
        main_frame.place_forget()

        
        display = ctk.CTkFrame(app, width=700, height=600)
        display.place(relx=0.5, rely=0.5, anchor="center")


        instruction_textbox = ctk.CTkTextbox(display, height=50, width=600,font=("Arial", 16))
        instruction_textbox.place(relx=0.5, rely=0.1, anchor="center")
        instruction_textbox.insert("0.0", "                      Enter  the  date  in  the  DDMMYYYY  format")
        instruction_textbox.configure(state="disabled")


        label1 = ctk.CTkLabel(display, text="Enter the transaction date:")
        label1.place(relx=0.3, rely=0.2, anchor="center")

        
        date_entry = ctk.CTkEntry(display, width=200)
        date_entry.place(relx=0.6, rely=0.2, anchor="center")

        
        def print_transaction():
            x = date_entry.get() 
            x=x[0:2]+"-"+x[2:4]+"-"+x[4:8]
            text1 = ""

            
            for transaction in Transaction.lst:
                if transaction.date == x:
                    text1 += str(transaction) + "\n"

            
            if not text1:
                text1 = "Transaction on the date does not exist."

            
            result_textbox = ctk.CTkTextbox(display, width=600, height=300)
            result_textbox.place(relx=0.5, rely=0.6, anchor="center")
            result_textbox.insert("0.0", text1)
            result_textbox.configure(state="disabled")  

        
        search_button = ctk.CTkButton(display, text="Search", command=print_transaction)
        search_button.place(relx=0.5, rely=0.3, anchor="center")


        def back_to_main():
            display.place_forget()
            main_frame.place(relx=0.4, rely=0.55, anchor="center")


        back_button = ctk.CTkButton(display, text="Back", command=back_to_main)
        back_button.place(relx=0.5, rely=0.9, anchor="center")
    def list_transactions(app, main_frame):
        main_frame.place_forget()

        list_transaction_frame = ctk.CTkFrame(app, width=810, height=600)
        list_transaction_frame.place(relx=0.5, rely=0.6, anchor="center")  
        
        Transaction.sortByDate()
        text1 = Transaction.listTransactions()

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
        button.pack(pady=10)  
    def cat_display(app, main_frame):
        main_frame.place_forget()

        frame = ctk.CTkFrame(app, width=810, height=600)
        frame.place(relx=0.5, rely=0.6, anchor="center")


        def categorize():
            categoryTotal = {}
            for transaction in Transaction.lst:
                if isinstance(transaction, Expense):
                    if transaction.category in categoryTotal:
                        categoryTotal[transaction.category] += transaction.amount
                    else:
                        categoryTotal[transaction.category] = transaction.amount
            return categoryTotal

        x = categorize()
        if not x:
            text1 = "No Expenses Yet"
        else:
            
            text1 = f"{'EXPENSE CATEGORY'.ljust(30)}{'AMOUNT'.rjust(10)}\n\n"
            for key, value in x.items():
                text1 += f"{str(key).ljust(30)}{str(value).rjust(10)}\n"

        
        textbox_frame = ctk.CTkFrame(frame, width=800, height=400)
        textbox_frame.pack(fill="both", expand=True, padx=10, pady=10)

        
        larger_font = ("Courier New", 16)  
        edit_textbox = ctk.CTkTextbox(textbox_frame, width=780, height=400, font=larger_font)
        edit_textbox.grid(row=0, column=0, sticky="nsew")
        edit_textbox.insert("0.0", text1)
        edit_textbox.configure(state="disabled")

        textbox_frame.grid_rowconfigure(0, weight=1)
        textbox_frame.grid_columnconfigure(0, weight=1)

        scrollbar = ctk.CTkScrollbar(textbox_frame, command=edit_textbox.yview)
        scrollbar.grid(row=0, column=1, sticky="ns")
        edit_textbox.configure(yscrollcommand=scrollbar.set)

        
        input_frame = ctk.CTkFrame(frame, width=800, height=100)
        input_frame.pack(fill="x", pady=(0, 10))

        
        def back_to_main():
            frame.place_forget()
            main_frame.place(relx=0.4, rely=0.55, anchor="center")

        
        back_button = ctk.CTkButton(input_frame, text="Back", command=back_to_main)
        # back_button.pack(side="left", padx=20, pady=10)
        back_button.place(relx=0.375,rely=0.5)


    def progress(app, main_frame):
        main_frame.place_forget()

        progress_frame = ctk.CTkFrame(app, width=810, height=600)
        progress_frame.place(relx=0.5, rely=0.6, anchor="center")  
        
        goals = {}
        for transaction in Transaction.lst:
            if isinstance(transaction, Savings):
                if transaction.goal in goals.keys():
                    goals[transaction.goal][1] += transaction.amount
                else:
                    goals[transaction.goal] = [transaction.target_amount, transaction.amount]

        text = ''
        for goal in goals:
            text += f"Goal : {goal}, Target : {goals[goal][0]}, Progress : {round(goals[goal][1]/goals[goal][0]*100,2)}%\n"
        
        if not text:
            text = "No Saving Transactions found."

        textbox_frame = ctk.CTkFrame(progress_frame, width=800, height=400)
        textbox_frame.pack(fill="both", expand=True, padx=10, pady=10)

        edit_textbox = ctk.CTkTextbox(textbox_frame, width=780, height=400)
        edit_textbox.grid(row=0, column=0, sticky="nsew")
        edit_textbox.insert("0.0", text)
        edit_textbox.configure(state="disabled")

        textbox_frame.grid_rowconfigure(0, weight=1)
        textbox_frame.grid_columnconfigure(0, weight=1)

        scrollbar = ctk.CTkScrollbar(textbox_frame, command=edit_textbox.yview)
        scrollbar.grid(row=0, column=1, sticky="ns")
        edit_textbox.configure(yscrollcommand=scrollbar.set)

        input_frame = ctk.CTkFrame(progress_frame, width=800, height=100)
        input_frame.pack(fill="x", pady=(0, 10))

        def back_to_main():
            progress_frame.place_forget()
            main_frame.place(relx=0.4, rely=0.55, anchor="center")

        button = ctk.CTkButton(input_frame, text="Back", command=back_to_main)
        button.pack(pady=10)  
    
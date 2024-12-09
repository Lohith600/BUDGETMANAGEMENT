import customtkinter as ctk
from PIL import Image, ImageTk
import os, pickle, budget_logic, csv
import tkinter.messagebox as tkmsg
from transaction import Transaction, Income, Expense, Savings

username = None
listOfTransactions = []
file_path = 'user_data.pkl'
if os.path.exists(file_path):
    with open(file_path, 'rb') as file:
        LoginDict = pickle.load(file)
else:
    file = open(file_path, 'wb')
    LoginDict = {}

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("BUDGET_MANAGEMENT")
app.geometry("810x700")

current_directory = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(current_directory, "../BUDGETMANAGEMENT/pictures/picture.jpg")


bg_photo = None


def load_background():
    global bg_photo
    try:
        bg_image = Image.open(image_path)
        bg_image = bg_image.resize((1100, 1100))
        bg_photo = ImageTk.PhotoImage(bg_image)

        bg_label = ctk.CTkLabel(app, image=bg_photo, text="")
        bg_label.place(relx=0, rely=0, relwidth=1, relheight=1)
    except Exception as e:
        print(f"Error loading image: {e}")



load_background()

# Heading frame for "MONTHLY BUDGET PLANNER"
heading = ctk.CTkTextbox(app, width=400, height=100, bg_color="#dbdbdb", text_color="#ae897c")
heading.insert("0.0", "        MONTHLY BUDGET\n               PLANNER")
heading.configure(font=("Helvetica", 28, "bold"))
heading.configure(state="disabled")

# Login Frame
login_frame = ctk.CTkFrame(app, width=400, height=500)
login_frame.place(relx=0.4, rely=0.6, anchor="center")

main_frame = None


def show_heading():
    """Display the heading widget on the login page."""
    heading.place(relx=0.4, rely=0.07, anchor="center")


def hide_heading():
    """Hide the heading widget when switching to other pages."""
    heading.place_forget()


def login_action():
    global username, listOfTransactions
    username = username_entry.get()
    password = password_entry.get()

    if username in LoginDict and LoginDict[username] == password:
        tkmsg.showinfo("Login Successful", f"Welcome, {username}!")
        hide_heading()  
        load_main_frame(username)

        # Load transactions for the logged-in user
        file_path = f"{username}"
        if os.path.exists(file_path):
            file = open(file_path + '/transactions.pkl', 'rb')
            listOfTransactions = pickle.load(file)
        else:
            os.mkdir(file_path)
            file = open(file_path + '/transactions.pkl', 'wb')
            listOfTransactions = []
    else:
        tkmsg.showerror("Invalid Login", "Invalid Username or Password.")
        username_entry.delete(0, "end")
        password_entry.delete(0, "end")


def signup_action():
    hide_heading()

    login_frame.place_forget()
    signup_button.place_forget()

    signup_frame = ctk.CTkFrame(app, width=400, height=500)
    signup_frame.place(relx=0.4, rely=0.6, anchor="center")

    signup_label = ctk.CTkLabel(signup_frame, text="Signup", font=("Helvetica", 24, "bold"))
    signup_label.pack(pady=20)

    new_username_label = ctk.CTkLabel(signup_frame, text="New Username:")
    new_username_label.pack(pady=5)

    new_username_entry = ctk.CTkEntry(signup_frame, width=300)
    new_username_entry.pack(pady=5)

    new_password_label = ctk.CTkLabel(signup_frame, text="New Password:")
    new_password_label.pack(pady=5)

    new_password_entry = ctk.CTkEntry(signup_frame, width=300, show="*")
    new_password_entry.pack(pady=5)

    def handle_signup():
        new_username = new_username_entry.get()
        new_password = new_password_entry.get()

        if new_username in LoginDict:
            tkmsg.showerror("Signup Failed", "Username already exists!")
        elif not new_username or not new_password:
            tkmsg.showerror("Signup Failed", "Both fields are required!")
        else:
            LoginDict[new_username] = new_password
            tkmsg.showinfo("Signup Successful", "Account created successfully!")
            signup_frame.place_forget()
            show_heading()
            login_frame.place(relx=0.4, rely=0.5, anchor="center")
            signup_button.place(relx=0.4, rely=0.90, anchor="center")

    signup_ok_button = ctk.CTkButton(signup_frame, text="OK", command=handle_signup, height=40, width=150,
                                     fg_color="#fff5ea", text_color="#924444")
    signup_ok_button.pack(pady=20)

    back_button = ctk.CTkButton(signup_frame, text="Back", height=40, width=150,
                                fg_color="#fff5ea", text_color="#924444",
                                command=lambda: switch_to_login(signup_frame))
    back_button.pack(pady=10)


def switch_to_login(frame_to_hide):
    print(LoginDict)
    frame_to_hide.place_forget()
    login_frame.place(relx=0.4, rely=0.5, anchor="center")
    show_heading()
    signup_button.place(relx=0.4, rely=0.90, anchor="center")


def load_main_frame(username):
    global main_frame
    if main_frame:
        main_frame.destroy()

    login_frame.place_forget()

    main_frame = ctk.CTkFrame(app, width=400, height=500)
    main_frame.place(relx=0.4, rely=0.55, anchor="center")

    greeting_label = ctk.CTkLabel(main_frame, text=f"Welcome, {username}!", font=("Helvetica", 20, "bold"))
    greeting_label.pack(pady=20)

    options = [
        ("Add Transaction", 1),
        ("Edit Transaction", 2),
        ("Delete Transaction", 3),
        ("Calculate Balance", 4),
        ("View Expense Categories", 5),
        ("Track Savings Progress", 6),
        ("List Transactions", 7),
        ("Find Transaction by Date", 8),
        ("Generate Monthly Report", 10),
        ("Logout", 9),
        ("Exit", 0)
    ]

    for text, option in options:
        button = ctk.CTkButton(main_frame, text=text, height=40, width=250,
                               fg_color="#fff5ea", text_color="#924444",
                               command=lambda opt=option: button_action(opt,username))
        button.pack(pady=5)


def button_action(option,username):
    if option == 1:
        from budget_logic import add_transaction_window
        add_transaction_window(app, main_frame, listOfTransactions)
        print(listOfTransactions)
    elif option == 9:
        main_frame.place_forget()
        login_frame.place(relx=0.4, rely=0.5, anchor="center")
        show_heading()
    elif option == 0:
        app.destroy()
    elif option == 2:
        from budget_logic import edit_transaction
        edit_transaction(listOfTransactions, app, main_frame)
    elif option == 3:
        from budget_logic import delete_transaction
        delete_transaction(app,main_frame,listOfTransactions)
    elif option == 4:
        from budget_logic import calculate_balance
        calculate_balance(app,main_frame,listOfTransactions)
    elif option == 6:
        from budget_logic import progress
        progress(app,main_frame,listOfTransactions)
    elif option == 7:
        from budget_logic import list_transactions
        list_transactions(app,main_frame,listOfTransactions)
    elif option == 8:
        from budget_logic import transaction_by_date
        transaction_by_date(app,main_frame,listOfTransactions)
    elif option == 5:
        from budget_logic import cat_display
        cat_display(app,main_frame,listOfTransactions)
    elif option == 10:
        from report_generator import saveToCSV
        saveToCSV(username, listOfTransactions)
    else:
        tkmsg.showinfo("No Feature")


username_label = ctk.CTkLabel(login_frame, text="Username:")
username_label.pack(pady=5)

username_entry = ctk.CTkEntry(login_frame, width=300)
username_entry.pack(pady=5)

password_label = ctk.CTkLabel(login_frame, text="Password:")
password_label.pack(pady=5)

password_entry = ctk.CTkEntry(login_frame, show="*", width=300)
password_entry.pack(pady=5)

login_button = ctk.CTkButton(login_frame, text="Login", height=40, width=150, fg_color="#fff5ea", text_color="#924444",
                             command=login_action)
login_button.pack(pady=20)

signup_button = ctk.CTkButton(app, text="Signup", height=40, width=150, fg_color="#fff5ea", text_color="#924444",
                              command=signup_action)
signup_button.place(relx=0.4, rely=0.90, anchor="center")

show_heading()
app.mainloop()

with open(file_path, 'wb') as file:
    pickle.dump(LoginDict, file)

file_path1 = f"{username}/transactions.pkl"
with open(file_path1, 'wb') as file:
    pickle.dump(listOfTransactions, file)

    header = [
        "Transaction Type", 
        "Amount", 
        "Date", 
        "Category/Source", 
        "Expense Type/Goal", 
        "Target Amount"
    ]
    
with open(f"{username}/transactions.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(header)

    for transaction in listOfTransactions:
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

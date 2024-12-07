import customtkinter as ctk
from PIL import Image, ImageTk
import os
import tkinter.messagebox as tkmsg
from transaction import Transaction, Income, Expense, Savings
#add the contents into the csv file at the end of the program
listOfTransactions = []
LoginDict = {"panda": "1234"}

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("BUDGET_MANAGEMENT")
app.geometry("810x700")

current_directory = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(current_directory, "../BUDGETMANAGEMENT/pictures/picture.jpg")

# Global variable for background image reference
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


# Load background for the app
load_background()

# Heading frame for "MONTHLY BUDGET PLANNER"
heading = ctk.CTkTextbox(app, width=400, height=100, bg_color="#dbdbdb", text_color="#ae897c")
heading.place(relx=0.4, rely=0.07, anchor="center")
heading.insert("0.0", "        MONTHLY BUDGET\n               PLANNER")
heading.configure(font=("Helvetica", 28, "bold"))
heading.configure(state="disabled")

# Login Frame
login_frame = ctk.CTkFrame(app, width=400, height=500)
login_frame.place(relx=0.4, rely=0.6, anchor="center")

main_frame = None


def login_action():
    username = username_entry.get()
    password = password_entry.get()

    if username in LoginDict and LoginDict[username] == password:
        tkmsg.showinfo("Login Successful", f"Welcome, {username}!")
        load_main_frame(username)
    else:
        tkmsg.showerror("Invalid Login", "Invalid Username or Password.")
        username_entry.delete(0, "end")
        password_entry.delete(0, "end")


def signup_action():
    # Hide the login frame and signup button
    login_frame.place_forget()
    signup_button.place_forget()

    # Create the signup frame
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

    # Function to handle the signup process
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
            signup_frame.place_forget()  # Hide the signup frame
            login_frame.place(relx=0.4, rely=0.5, anchor="center")  # Show the login frame
            signup_button.place(relx=0.4, rely=0.90, anchor="center")  # Show the signup button again

    # OK button for Signup
    signup_ok_button = ctk.CTkButton(signup_frame, text="OK", command=handle_signup, height=40, width=150,
                                     fg_color="#fff5ea", text_color="#924444")
    signup_ok_button.pack(pady=20)

    # Back button to return to the login screen
    back_button = ctk.CTkButton(signup_frame, text="Back", height=40, width=150,
                                fg_color="#fff5ea", text_color="#924444",
                                command=lambda: switch_to_login(signup_frame))
    back_button.pack(pady=10)


# Function to switch back to the login frame
def switch_to_login(frame_to_hide):
    print(LoginDict)
    frame_to_hide.place_forget()
    login_frame.place(relx=0.4, rely=0.5, anchor="center")
    signup_button.place(relx=0.4, rely=0.90, anchor="center")  # Show the signup button again


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
        ("Logout", 9),
        ("Exit", 0)
    ]

    for text, option in options:
        button = ctk.CTkButton(main_frame, text=text, height=40, width=250,
                               fg_color="#fff5ea", text_color="#924444",
                               command=lambda opt=option: button_action(opt))
        button.pack(pady=5)


def add_transaction_window():
    global main_frame

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


def button_action(option):
    if option == 1: 
         # Add Transaction
        add_transaction_window()
    elif option == 9:  # Logout
        main_frame.place_forget()
        login_frame.place(relx=0.4, rely=0.5, anchor="center")
    elif option == 0:  # Exit
        app.destroy()
    else:
        tkmsg.showinfo("no feature")


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

app.mainloop()

import customtkinter as ctk
from PIL import Image, ImageTk
import os

# Set appearance mode and color theme
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

# Initialize the main app
app = ctk.CTk()
app.title("BUDGET_MANAGEMENT")
app.geometry("810x700")

# Get the current directory of the script and build the relative path for the image
current_directory = os.path.dirname(os.path.abspath(__file__))  # Get the current script directory
image_path = os.path.join(current_directory, "../BUDGETMANAGEMENT/pictures/picture.jpg")

# Try loading the image
try:
    bg_image = Image.open(image_path)
    bg_image = bg_image.resize((1100, 1100))  # Resize the image to fit the background
    bg_photo = ImageTk.PhotoImage(bg_image)

    # Set the image as the background
    bg_label = ctk.CTkLabel(app, image=bg_photo, text="")
    bg_label.place(relx=0, rely=0, relwidth=1, relheight=1)
except Exception as e:
    print(f"Error loading image: {e}")
    bg_photo = None

# Create the textbox with the title
text = "             MONTHLY BUDGET\n\n                     PLANNER"
textbox = ctk.CTkTextbox(app, width=450, height=120, fg_color="#fff5ea", text_color="#924444")
textbox.place(relx=0.08)
textbox.configure(font=("Helvetica", 27, "bold"))
textbox.insert("0.0", text)
textbox.configure(state="disabled")

# Button 1 Action
def button1_action():
    pass

# Button 2 Action
def button2_action():
    pass

# Button 1
button1 = ctk.CTkButton(master=bg_label, text="Login", command=button1_action, height=50, width=200, fg_color="#fff5ea", text_color="#924444")
button1.place(relx=0.03, rely=0.8)

# Button 2
button2 = ctk.CTkButton(master=bg_label, text="Signup", command=button2_action, height=50, width=200, fg_color="#fff5ea", text_color="#924444")
button2.place(relx=0.45, rely=0.8)

# Run the application
app.mainloop()

import customtkinter as ctk
from PIL import Image,ImageTk

ctk.set_appearance_mode("System")  
ctk.set_default_color_theme("blue")  

app = ctk.CTk()
app.title("BUDGET_MANAGEMENT")
app.geometry("810x700")
image_path = "c:/Users/G lohith praopoorna/Desktop/codebro/image/picture.jpg"
bg_image = Image.open(image_path)
bg_image = bg_image.resize((1100, 1100))  
bg_photo = ImageTk.PhotoImage(bg_image)

bg_label = ctk.CTkLabel(app, image=bg_photo, text="")  
bg_label.place(relx=0, rely=0, relwidth=1, relheight=1)


text="             MONTHLY BUDGET\n\n                     PLANNER"
textbox = ctk.CTkTextbox(app, width=450, height=120,fg_color="#fff5ea",text_color="#924444")
textbox.place(relx=0.08)
textbox.configure(font=("Helvetica", 27, "bold"))
textbox.insert("0.0",text)
textbox.configure(state="disabled")



# Button 1 Action
def button1_action():
    pass

# Button 2 Action
def button2_action():
    pass

# Button 1
button1 = ctk.CTkButton(master=bg_label, text="Login", command=button1_action,height=50,width=200,fg_color="#fff5ea",text_color="#924444")
button1.place(relx=0.07,rely=0.8)

button2 = ctk.CTkButton(master=bg_label, text="Signup", command=button2_action,height=50,width=200,fg_color="#fff5ea",text_color="#924444")
button2.place(relx=0.45,rely=0.8)

app.mainloop()

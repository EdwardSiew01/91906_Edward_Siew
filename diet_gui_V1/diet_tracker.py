import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk  

# Create FirstPage class
class FirstPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Open image
        load = Image.open("Asset/diet_4.png")
        # Resize image to fit the GUI page
        resized_image = load.resize((800, 800))
        photo = ImageTk.PhotoImage(resized_image)
        # Create a label
        label = tk.Label(self, image=photo)
        label.image = photo
        label.place(x=0, y=0)
        # Border 
        border = tk.LabelFrame(self, text='Welcome', bg='black', bd=10, font=("Arial", 20), relief=tk.SUNKEN)

        border.pack(fill="both", expand="yes", padx=150, pady=300)
        # Label as username
        Label_1 = tk.Label(border, text="Username", font=("Arial Bold", 15), bg='black')
        Label_1.place(x=50, y=20)
        # Username textfield
        Textfield_1 = tk.Entry(border, width=30, bd=5)
        Textfield_1.place(x=180, y=20)
        # Label as password
        Label_2 = tk.Label(border, text="Password", font=("Arial Bold", 15), bg='black')
        Label_2.place(x=50, y=80)
        # Password textfield
        Textfield_2 = tk.Entry(border, width=30, show='*', bd=5)
        Textfield_2.place(x=180, y=80)

        def verify():
            try:
                with open("Textfile/login.txt", "r") as f:
                    info = f.readlines()
                    i = 0
                    for e in info:
                        uid, u, p = e.strip().split(",")
                        if u.strip() == Textfield_1.get() and p.strip() == Textfield_2.get() and uid.strip() != "":
                            controller.show_frame(SecondPage)
                            i = 1
                            break
                    if i == 0:
                        messagebox.showinfo("Error", "Please provide correct username and password!!")
            except:
                messagebox.showinfo("Error", "Please provide correct username and password!!")

        # Log in button 
        Button_1 = tk.Button(border, text="Log in", font=("Arial", 15), command=verify)
        Button_1.place(x=320, y=115)

###Register_page###
        # Register page
        def register():
            window = tk.Tk()
            window.resizable(0,0)
            window.configure(bg="black")
            window.title("Register")
            label_1 = tk.Label(window, text="Username:", font=("Arial",15), bg="black")
            label_1.place(x=10, y=10)
            textfield_1 = tk.Entry(window, width=30, bd=5)
            textfield_1.place(x = 200, y=10)
            
            label_2 = tk.Label(window, text="Password:", font=("Arial",15), bg="black")
            label_2.place(x=10, y=60)
            textfield_2 = tk.Entry(window, width=30, show="*", bd=5)
            textfield_2.place(x = 200, y=60)
            
            label_3 = tk.Label(window, text="Confirm Password:", font=("Arial",15), bg="black")
            label_3.place(x=10, y=110)
            textfield_3 = tk.Entry(window, width=30, show="*", bd=5)
            textfield_3.place(x = 200, y=110)

###Final version
            import uuid

            def generate_uid():
                return str(uuid.uuid4())

            def check():
                    if textfield_1.get() != "" and textfield_2.get() != "" and textfield_3.get() != "":
                        with open("Textfile/login.txt", "r") as f:
                            lines = f.readlines()
                        registered_users = [line.strip().split(",")[1] for line in lines]

                        if textfield_1.get() in registered_users:
                            messagebox.showinfo("Error", "Username already exists. Please choose a different username.")
                        elif textfield_2.get() == textfield_3.get():
                            # generate uid
                            uid = generate_uid()  
                            with open("Textfile/login.txt", "a") as f:
                                f.write(uid + "," + textfield_1.get() + "," + textfield_2.get() + "\n")
                            messagebox.showinfo("Welcome", "You are registered successfully!!")
                        else:
                            messagebox.showinfo("Error", "Your password didn't match!!")
                    else:
                            messagebox.showinfo("Error", "Please fill in all the fields!!")

            # Sign up button        
            button_1 = tk.Button(window, text="Sign up", font=("Arial",15), bg="#ffc22a", command=check)
            button_1.place(x=170, y=150)

            #Resize the window geometry to make it more artistic
            window.geometry("500x220")
            window.mainloop()
        # Register button    
        Button_2 = tk.Button(self, text="Register",font=("Arial",15) ,command=register)
        Button_2.place(x=650, y=20)

# Create SecondPage class
class SecondPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Carbs image
        # Open image
        load = Image.open("Asset/carbs.png")
        # Resize image to fit the GUI page
        resized_image = load.resize((400, 400))
        photo = ImageTk.PhotoImage(resized_image)
        # Create a label
        label = tk.Label(self, image=photo)
        label.image=photo
        label.place(x=0,y=0)

        # Fat image
        # Open image
        load = Image.open("Asset/fat.png")
        # Resize image to fit the GUI page
        resized_image = load.resize((400, 400))
        photo = ImageTk.PhotoImage(resized_image)
        # Create a label
        label = tk.Label(self, image=photo)
        label.image=photo
        label.place(x=400,y=0)

        # Protein image
        # Open image
        load = Image.open("Asset/protein.png")
        # Resize image to fit the GUI page
        resized_image = load.resize((400, 400))
        photo = ImageTk.PhotoImage(resized_image)
        # Create a label
        label = tk.Label(self, image=photo)
        label.image=photo
        label.place(x=0,y=400)

        # Protein image
        # Open image
        load = Image.open("Asset/macro.png")
        # Resize image to fit the GUI page
        resized_image = load.resize((400, 400))
        photo = ImageTk.PhotoImage(resized_image)
        # Create a label
        label = tk.Label(self, image=photo)
        label.image=photo
        label.place(x=400,y=400)

        text = """
        Maintaining a healthy and well-balanced diet is not only important for physical well-being but also for mental health. A nutritious diet can enhance cognitive function, improve concentration, and support overall mental well-being. On the other hand, consuming processed foods high in sugar and unhealthy fats can contribute to fatigue, impaired decision-making, and even worsen stress and depression.
        
        Making conscious choices about the foods we eat can positively impact our mental health. Incorporating plenty of fruits, vegetables, omega-3 fatty acids, lean proteins, and complex carbohydrates into our meals can provide the necessary nutrients for optimal brain function. Additionally, paying attention to our eating habits, practicing mindful eating, and seeking professional help when necessary are important steps towards maintaining a healthy relationship with food.
        
        By prioritizing a nutritious diet, we can nourish our bodies and minds, leading to improved mental clarity, mood stability, and overall well-being.
        """

        label = tk.Label(self, text=text, font=("Arial", 18), wraplength=700, justify="left", fg="black", bg="white", highlightthickness=0, highlightbackground="grey")
        label.place(x=50, y=200)
        
        # Button to thridpage
        Button = tk.Button(self, text="Next", font=("Arial", 15), command=lambda: controller.show_frame(ThirdPage), bd=0, relief="flat")
        Button.place(x=650, y=650)
        # Button to previous page
        Button = tk.Button(self, text="Back", font=("Arial", 15), command=lambda: controller.show_frame(FirstPage), bd=0, relief="flat")
        Button.place(x=100, y=650)

# Create ThirdPage class    
class ThirdPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        self.configure(bg='white')
        """
        label = tk.Label(self, text=".... \n ???", bg="orange", font=("Arial Bold", 25))
        label.place(x=40, y=150)
        """
        # Title for the Calories Calculator section
        calories_title = tk.Label(self, text="Calories Calculator", font=("Arial Bold", 25), bg="black")
        calories_title.place(x=350, y=20, anchor=tk.CENTER)

        # Title for the Food Energy Converter section
        converter_title = tk.Label(self, text="Food Energy Converter", font=("Arial Bold", 25), bg="black")
        converter_title.place(x=350, y=400, anchor=tk.CENTER)

        # Logo image
        # Open image
        load = Image.open("Asset/diet_logo_1.png")
        # Resize image to fit the GUI page
        resized_image = load.resize((80, 50))
        photo = ImageTk.PhotoImage(resized_image)
        # Create a label
        label = tk.Label(self, image=photo)
        label.image=photo
        label.place(x=0,y=0)

        # Conversion functions
        def convert_calories_to_joules():
            calories = int(entry.get())  # Get the input value from the entry widget
            joules = calories * 4.184  # Conversion factor: 1 calorie = 4.184 joules
            result_label.configure(text=f"{calories} calories is equal to {joules} joules.")

        def convert_joules_to_calories():
            joules = int(entry.get())  # Get the input value from the entry widget
            calories = joules / 4.184  # Conversion factor: 1 calorie = 4.184 joules
            result_label.configure(text=f"{joules} joules is equal to {calories} calories.")

        # Entry widget to input energy value
        entry = tk.Entry(self, font=("Arial", 15))
        entry.place(x=100, y=450)

        # Button to convert calories to joules
        convert_calories_button = tk.Button(self, text="Convert Calories to Joules", font=("Arial", 15), command=convert_calories_to_joules, bd=0, relief="flat")
        convert_calories_button.place(x=100, y=500)

        # Button to convert joules to calories
        convert_joules_button = tk.Button(self, text="Convert Joules to Calories", font=("Arial", 15), command=convert_joules_to_calories, bd=0, relief="flat")
        convert_joules_button.place(x=300, y=500)

        # Label to display the result
        result_label = tk.Label(self, text="", font=("Arial Bold", 18), fg="white")
        result_label.place(x=100, y=550)

        # Calories calculator function
        def calculate_calories():
            gender = gender_entry.get()
            weight = int(weight_entry.get())
            height = int(height_entry.get())
            age = int(age_entry.get())
            activity_level = activity_level_var.get().lower()


            if gender.lower() == "male":
                bmr = 66 + (13.75 * weight) + (5 * height) - (6.75 * age)
            elif gender.lower() == "female":
                bmr = 655 + (9.56 * weight) + (1.85 * height) - (4.68 * age)
            else:
                print("Invalid gender input.")
                return

            activity_levels = {
                "sedentary": 1.2,
                "lightly active": 1.375,
                "moderately active": 1.55,
                "very active": 1.725
            }

            if activity_level in activity_levels:
                calories_needed = bmr * activity_levels[activity_level]
                calories_result.configure(text=str(calories_needed))
            else:
                print("Invalid activity level input.")

        # Create input fields
        gender_label = tk.Label(self, text="Gender:", font=("Arial", 15))
        gender_label.place(x=100, y=50)
        gender_entry = tk.Entry(self, font=("Arial", 15))
        gender_entry.place(x=250, y=50)

        weight_label = tk.Label(self, text="Weight (kg):", font=("Arial", 15))
        weight_label.place(x=100, y=100)
        weight_entry = tk.Entry(self, font=("Arial", 15))
        weight_entry.place(x=250, y=100)

        height_label = tk.Label(self, text="Height (cm):", font=("Arial", 15))
        height_label.place(x=100, y=150)
        height_entry = tk.Entry(self, font=("Arial", 15))
        height_entry.place(x=250, y=150)

        age_label = tk.Label(self, text="Age (years):", font=("Arial", 15))
        age_label.place(x=100, y=200)
        age_entry = tk.Entry(self, font=("Arial", 15))
        age_entry.place(x=250, y=200)

        # Create dropdown menu for activity level
        activity_level_label = tk.Label(self, text="Activity Level:", font=("Arial", 15))
        activity_level_label.place(x=100, y=250)
        activity_levels = ["Sedentary", "Lightly Active", "Moderately Active", "Very Active"]
        activity_level_var = tk.StringVar(self)
        activity_level_var.set("Select Activity Level")
        activity_level_dropdown = tk.OptionMenu(self, activity_level_var, *activity_levels)
        activity_level_dropdown.config(font=("Arial", 15))
        activity_level_dropdown.place(x=250, y=250)

        # Create label for displaying calories needed
        calories_label = tk.Label(self, text="Calories needed per day:", font=("Arial", 15))
        calories_label.place(x=100, y=300)
        calories_result = tk.Label(self, text="", font=("Arial Bold", 18), fg="white")
        calories_result.place(x=100, y=350)

        # Button to calculate calories
        calculate_button = tk.Button(self, text="Calculate Calories", font=("Arial", 15), command=calculate_calories, bd=0, relief="flat")
        calculate_button.place(x=400, y=300)
        
        # Button to homepage
        home_button = tk.Button(self, text="Home", font=("Arial", 15), command=lambda: controller.show_frame(FirstPage), bd=0, relief="flat")
        home_button.place(x=650, y=650)

        # Button to previous page
        back_button = tk.Button(self, text="Back", font=("Arial", 15), command=lambda: controller.show_frame(SecondPage), bd=0, relief="flat")
        back_button.place(x=100, y=650)

# Main function        
class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # Creating a window
        window = tk.Frame(self)
        window.pack()
        # Size of window
        window.grid_rowconfigure(0, minsize = 800)
        window.grid_columnconfigure(0, minsize = 800)
        # Store the frames for each page
        self.frames = {}
        for F in (FirstPage, SecondPage, ThirdPage):
            frame = F(window, self)
            self.frames[F] = frame
            frame.grid(row = 0, column=0, sticky="nsew")
        
        # Display the firstpage frame    
        self.show_frame(FirstPage)
        
    def show_frame(self, page):
        frame = self.frames[page]
        # Raises the frame to the top, making it visible in the GUI
        frame.tkraise()
        # Title
        self.title("Diet_gui")

          
app = Application()
app.maxsize(800,800)
# Run the main event loop
app.mainloop()

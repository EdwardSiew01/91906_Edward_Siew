import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk

# Create FirstPage class
class FirstPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Open image
        load = Image.open("asset/diet_4.png")
        # Resize image to fit the GUI page
        resized_image = load.resize((800, 800))
        photo = ImageTk.PhotoImage(resized_image)
        # Create a label
        label = tk.Label(self, image=photo)
        label.image = photo
        label.place(x=0, y=0)
        # Border 
        border = tk.LabelFrame(
            self,
            text='Welcome',
            bg='black',
            bd=10,
            font=("Arial", 20),
            relief=tk.SUNKEN
        )
        border.pack(fill="both", expand="yes", padx=150, pady=300)
        # Label as username
        label__1 = tk.Label(
            border,
            text="Username",
            font=("Arial Bold", 15),
            bg='black'
        )
        label__1.place(x=50, y=20)
        # Username textfield
        textfield__1 = tk.Entry(border, width=30, bd=5)
        textfield__1.place(x=180, y=20)
        # Label as password
        label__2 = tk.Label(
            border,
            text="Password",
            font=("Arial Bold", 15),
            bg='black'
        )
        label__2.place(x=50, y=80)
        # Password textfield
        textfield__2 = tk.Entry(border, width=30, show='*', bd=5)
        textfield__2.place(x=180, y=80)
        # Implementing a login function


        def verify():
            try:
                with open("textfile/login.txt", "r") as f:
                    info = f.readlines()
                    i = 0
                    for e in info:
                        uid, u, p = e.strip().split(",")
                        if (
                            u.strip() == textfield__1.get()
                            and p.strip() == textfield__2.get()
                            and uid.strip() != ""
                        ):
                            controller.show_frame(SecondPage)
                            i = 1
                            break
                    if i == 0:
                        messagebox.showinfo(
                            "Error",
                            "Please provide correct username and password!!"
                        )
            except:
                messagebox.showinfo(
                    "Error",
                    "Please provide correct username and password!!"
                )
        # Log in button
        login_button = tk.Button(
            border,
            text="Log in",
            font=("Arial", 15),
            command=verify
        )
        login_button.place(x=320, y=115)

        # Register page


        def register():
            window = tk.Tk()
            window.resizable(0, 0)
            window.configure(bg="black")
            window.title("Register")
            
            username_label = tk.Label(
                window,
                text="Username:",
                font=("Arial", 15),
                bg="black"
            )
            username_label.place(x=10, y=10)
            
            username_textfield = tk.Entry(window, width=30, bd=5)
            username_textfield.place(x=200, y=10)
            
            password_label = tk.Label(
                window,
                text="Password:",
                font=("Arial", 15),
                bg="black"
            )
            password_label.place(x=10, y=60)
            
            password_textfield = tk.Entry(window, width=30, show="*", bd=5)
            password_textfield.place(x=200, y=60)
            
            confirm_password_label = tk.Label(
                window,
                text="Confirm Password:",
                font=("Arial", 15),
                bg="black"
            )
            confirm_password_label.place(x=10, y=110)
            
            confirm_password_textfield = tk.Entry(window, width=30, show="*", bd=5)
            confirm_password_textfield.place(x=200, y=110)

            import uuid
            import re
            # Generate a unique ID using UUID (Universally Unique Identifier)


            def generate_uid():
                return str(uuid.uuid4())
            # Function to check the user input for registration


            def check():
                # Check if all three textfields are not empty
                if (
                    username_textfield.get() != ""
                    and password_textfield.get() != ""
                    and confirm_password_textfield.get() != ""
                ):
                    # Read the existing registered users from a text file
                    with open("textfile/login.txt", "r") as f:
                        lines = f.readlines()
                    registered_users = [
                        line.strip().split(",")[1]
                        for line in lines
                    ]
                    # Check if the entered username already exists in the list of registered users
                    if username_textfield.get() in registered_users:
                        messagebox.showinfo(
                            "Error",
                            "Username already exists. Please choose a different username."
                        )
                    # Check if the entered passwords match
                    elif (
                        password_textfield.get() == confirm_password_textfield.get()
                    ):
                        # Check password condition
                        if check_password_condition(password_textfield.get()):
                            # generate uid
                            uid = generate_uid()
                            # Append the new user's details (UID, username, password) to the login.txt file
                            with open("textfile/login.txt", "a") as f:
                                f.write(
                                    uid + ","
                                    + username_textfield.get() + ","
                                    + password_textfield.get() + "\n"
                                )
                                # Show a successful registration message
                            messagebox.showinfo(
                                "Welcome",
                                "You are registered successfully!!"
                            )
                        else:
                            # Show an error message if the password doesn't meet the condition
                            messagebox.showinfo(
                                "Error",
                                "Password must contain at least 4 numbers and 1 special character!"
                            )
                    else:
                        # Show an error message if the entered passwords don't match
                        messagebox.showinfo("Error", "Your password didn't match!!")
                else:
                    # Show an error message if any of the fields are empty
                    messagebox.showinfo("Error", "Please fill in all the fields!!")
            
            # Function to check the password condition


            def check_password_condition(password):
                if len(re.findall(r"\d", password)) < 4:
                    # Minimum 4 numbers
                    return False
                # Minimum 1 special character
                if len(re.findall(r"[!@#$%^&*()_+\-=[\]{};':\"\\|,.<>/?]", password)) < 1:
                    return False
                return True
            
            # Sign up button
            sign_up_button = tk.Button(
                window,
                text="Sign up",
                font=("Arial", 15),
                bg="#ffc22a",
                command=check
            )
            sign_up_button.place(x=170, y=150)

            #Resize the window geometry to make it more artistic
            window.geometry("500x220")
            window.mainloop()

        # Register button
        register_button = tk.Button(
            self,
            text="Register",
            font=("Arial", 15),
            command=register
        )
        register_button.place(x=650, y=20)

# Create SecondPage class
class SecondPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Carbs image
        # Open image
        load = Image.open("asset/carbs.png")
        # Resize image to fit the GUI page
        resized_image = load.resize((400, 400))
        photo = ImageTk.PhotoImage(resized_image)
        # Create a label
        label = tk.Label(self, image=photo)
        label.image = photo
        label.place(x=0, y=0)

        # Fat image
        # Open image
        load = Image.open("asset/fat.png")
        # Resize image to fit the GUI page
        resized_image = load.resize((400, 400))
        photo = ImageTk.PhotoImage(resized_image)
        # Create a label
        label = tk.Label(self, image=photo)
        label.image = photo
        label.place(x=400, y=0)

        # Protein image
        # Open image
        load = Image.open("asset/protein.png")
        # Resize image to fit the GUI page
        resized_image = load.resize((400, 400))
        photo = ImageTk.PhotoImage(resized_image)
        # Create a label
        label = tk.Label(self, image=photo)
        label.image = photo
        label.place(x=0, y=400)

        # Macro image
        # Open image
        load = Image.open("asset/macro.png")
        # Resize image to fit the GUI page
        resized_image = load.resize((400, 400))
        photo = ImageTk.PhotoImage(resized_image)
        # Create a label
        label = tk.Label(self, image=photo)
        label.image = photo
        label.place(x=400, y=400)

        text = (
            "Maintaining a healthy and well-balanced diet is not only important for physical well-being"
            " but also for mental health. A nutritious diet can enhance cognitive function, improve concentration,"
            " and support overall mental well-being. On the other hand, consuming processed foods high in sugar"
            " and unhealthy fats can contribute to fatigue, impaired decision-making, and even worsen stress"
            " and depression.\n\nMaking conscious choices about the foods we eat can positively impact our mental"
            " health. Incorporating plenty of fruits, vegetables, omega-3 fatty acids, lean proteins, and complex"
            " carbohydrates into our meals can provide the necessary nutrients for optimal brain function."
            " Additionally, paying attention to our eating habits, practicing mindful eating, and seeking professional"
            " help when necessary are important steps towards maintaining a healthy relationship with food."
            "\n\nBy prioritizing a nutritious diet, we can nourish our bodies and minds, leading to improved"
            " mental clarity, mood stability, and overall well-being."
        )

        label = tk.Label(
            self,
            text=text,
            font=("Arial", 18),
            wraplength=700,
            justify="left",
            fg="black",
            bg="white",
            highlightthickness=0,
            highlightbackground="grey"
        )
        label.place(x=50, y=200)

        # Button to thridpage
        Button = tk.Button(
            self,
            text="Next",
            font=("Arial", 15),
            command=lambda: controller.show_frame(ThirdPage),
            bd=0,
            relief="flat"
        )
        Button.place(x=650, y=650)

        # Button to previous page
        Button = tk.Button(
            self,
            text="Back",
            font=("Arial", 15),
            command=lambda: controller.show_frame(FirstPage),
            bd=0,
            relief="flat"
        )
        Button.place(x=100, y=650)

# Create ThirdPage class
class ThirdPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Set a colorful background for the page
        self.configure(bg='#F4F1E9')

        # Title for the Calories Calculator section with a colorful background
        calories_title = tk.Label(
            self,
            text="Calories Calculator",
            font=("Arial Bold", 25),
            bg="#FFD700",
            fg="black"
        )
        calories_title.place(x=350, y=20, anchor=tk.CENTER)

        # Open logo image
        load = Image.open("asset/diet_logo_1.png")
        # Resize image to fit the GUI page
        resized_image = load.resize((80, 50))
        photo = ImageTk.PhotoImage(resized_image)
        # Create a label
        label = tk.Label(self, image=photo)
        label.image = photo
        label.place(x=0, y=0)

         # Diet plan function


        def read_diet_plan_from_file(file_path):
            with open(file_path, 'r') as file:
                diet_plan = file.read()
            return diet_plan


             # Diet plan generate function


        def generate_diet_plan(calories):
            if calories <= 1500:
                return read_diet_plan_from_file("textfile/diet_plan_1500_calories.txt")
            elif 1500 < calories <= 2000:
                return read_diet_plan_from_file("textfile/diet_plan_2000_calories.txt")
            else:
                return read_diet_plan_from_file("textfile/diet_plan_2500_calories.txt")

        # Calories calculator function


        def calculate_calories():
            gender = gender_var.get()
            weight = weight_entry.get()
            height = height_entry.get()
            age = age_entry.get()
            activity_level = activity_level_var.get().lower()

            # Check if any of the fields are empty or not selected
            if not gender or not weight or not height or not age or not activity_level:
                # Display an error message using a pop-up dialog box
                messagebox.showerror("Error", "Please enter all the information required.")
                return

            try:
                weight = int(weight)
                height = int(height)
                age = int(age)
            except ValueError:
                # Display an error message using a pop-up dialog box
                messagebox.showerror("Error", "Invalid input for weight, height, or age.")
                return

            # Check if weight, height & age are within the specified range
            if weight < 0.1:
                messagebox.showerror("Error", "Invalid input for weight. Weight must be at least 0.1 kg.")
                return
            elif weight > 300:
                messagebox.showinfo("Warning", "Are you a giant? Please make sure to enter a reasonable weight.")
                return
            if height < 1:
                messagebox.showerror("Error", "Invalid input for height. Height must be at least 1 cm.")
                return
            elif height > 300:
                messagebox.showinfo("Warning", "Are you a giant? Please make sure to enter a reasonable height.")
                return
            if age < 1:
                messagebox.showerror("Error", "Invalid input for age. Age must be at least 1 years.")
                return
            elif age > 300:
                messagebox.showinfo("Warning", "Please make sure to enter a reasonable age.")
                return
            # Check if the activity level is valid
            valid_activity_levels = ["sedentary", "lightly active", "moderately active", "very active", "extra active"]
            if activity_level.lower() not in valid_activity_levels:
                # Display an error message using a pop-up dialog box
                messagebox.showerror("Error", "Invalid activity level input.")
                return

            # If everything is valid, calculate the calories as before
            if gender.lower() == "male":
                bmr = 66 + (13.75 * weight) + (5 * height) - (6.75 * age)
            elif gender.lower() == "female":
                bmr = 655 + (9.56 * weight) + (1.85 * height) - (4.68 * age)
            else:
                # Display an error message using a pop-up dialog box
                messagebox.showerror("Error", "Invalid gender input.")
                return
            
            activity_levels = {
                "sedentary": 1.2,
                "lightly active": 1.375,
                "moderately active": 1.55,
                "very active": 1.725
            }

            if activity_level in activity_levels:
                calories_needed = bmr * activity_levels[activity_level]
                # Convert the calories_needed to an integer (whole number)
                calories_needed = int(calories_needed)
                calories_result.configure(text=str(calories_needed))
                
                # Generate diet plan based on the calculated calories
                diet_plan = generate_diet_plan(calories_needed)
                # Write the diet plan to a text file
                with open("textfile/diet_plan.txt", "w") as file:
                    file.write(diet_plan)

                # Display the generated diet plan in the label
                diet_plan_label.configure(text=diet_plan)

                # Check if there are previously stored calories and diet plan
                try:
                    with open("textfile/previous_calories.txt", "r") as cal_file:
                        previous_calories_data = cal_file.read().strip()
                        if previous_calories_data:
                            previous_calories = float(previous_calories_data)
                        else:
                            previous_calories = None
                except FileNotFoundError:
                    previous_calories = None

                try:
                    with open("textfile/previous_diet_plan.txt", "r") as diet_file:
                        previous_diet_plan = diet_file.read()
                except FileNotFoundError:
                    previous_diet_plan = None

                # Compare and display the comparison results
                if previous_calories is not None:
                    comparison_text = "Comparison with the previous calculation:\n"
                    if calories_needed > previous_calories:
                        comparison_text += "Your current calorie needs are higher than the previous calculation.\n"
                    elif calories_needed < previous_calories:
                        comparison_text += "Your current calorie needs are lower than the previous calculation.\n"
                    else:
                        comparison_text += "Your current calorie needs are the same as the previous calculation.\n"

                    if previous_diet_plan:
                        if diet_plan == previous_diet_plan:
                            comparison_text += "Your diet plan remains the same as the previous one."
                        else:
                            comparison_text += "Your diet plan has changed since the previous calculation."

                    comparison_label.configure(text=comparison_text)

                # Store the current calories for future comparison
                with open("textfile/previous_calories.txt", "w") as cal_file:
                    cal_file.write(str(calories_needed))
                # Store the current diet plan for future comparison
                with open("textfile/previous_diet_plan.txt", "w") as diet_file:
                    diet_file.write(diet_plan)
            else:
                print("Invalid activity level input.")

        # Create input fields
        gender_label = tk.Label(self, text="Gender:", font=("Arial", 15))
        gender_label.place(x=100, y=50)
        # Create a variable to store the selected gender
        gender_var = tk.StringVar(self)
        # Set the default value for the dropdown menu
        gender_var.set("Select Gender")
        gender_options = ["Male", "Female"]
        gender_dropdown = tk.OptionMenu(self, gender_var, *gender_options)
        gender_dropdown.config(font=("Arial", 15))
        gender_dropdown.place(x=250, y=50)

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
        calculate_button = tk.Button(
            self,
            text="Calculate Calories",
            font=("Arial", 15),
            command=calculate_calories,
            fg="black",
            bd=0,
            relief="flat"
        )
        calculate_button.place(x=400, y=300)

        # Label to display the generated diet plan
        diet_plan_label = tk.Label(self, text="Diet Plan", font=("Arial", 15))
        diet_plan_label.place(x=100, y=400)

        # Label to display the comparison results
        comparison_label = tk.Label(self, text="Compare", font=("Arial", 15))
        comparison_label.place(x=100, y=550)

        # Button to homepage
        home_button = tk.Button(
            self,
            text="Home",
            font=("Arial", 15),
            command=lambda: controller.show_frame(FirstPage),
            fg="black",
            bd=0,
            relief="flat"
        )
        home_button.place(x=650, y=650)

        # Button to previous page
        back_button = tk.Button(
            self,
            text="Back",
            font=("Arial", 15),
            command=lambda: controller.show_frame(SecondPage),
            fg="black",
            bd=0,
            relief="flat"
        )
        back_button.place(x=100, y=650)

# Main function        
class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # Creating a window
        window = tk.Frame(self)
        window.pack()
        # Size of window
        window.grid_rowconfigure(0, minsize=800)
        window.grid_columnconfigure(0, minsize=800)
        # Store the frames for each page
        self.frames = {}
        for F in (FirstPage, SecondPage, ThirdPage):
            frame = F(window, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        
        # Display the firstpage frame
        self.show_frame(FirstPage)
        

    def show_frame(self, page):
        frame = self.frames[page]
        # Raises the frame to the top, making it visible in the GUI
        frame.tkraise()
        # Title
        self.title("Diet_gui")

app = Application()
app.maxsize(800, 800)
app.mainloop()
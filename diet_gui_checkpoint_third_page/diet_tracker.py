import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk


# Create NextButton class
class NextButton(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Button to thridpage
        button = tk.Button(self, text="Next", font=("Arial", 15), command=lambda: controller.show_frame(ThirdPage))
        button.place(x=650, y=450)

# Create BackButton class
class BackButton(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Button to previous page
        button = tk.Button(self, text="Back", font=("Arial", 15), command=lambda: controller.show_frame(FirstPage))
        button.place(x=100, y=450)

# Create SecondPage class
class SecondPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

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

        # Carbs image
        # Open image
        load = Image.open("Asset/diet_logo_1.png")
        # Resize image to fit the GUI page
        resized_image = load.resize((80, 50))
        photo = ImageTk.PhotoImage(resized_image)
        # Create a label
        label = tk.Label(self, image=photo)
        label.image=photo
        label.place(x=0,y=0)

        # Button to homepage
        home_button = tk.Button(self, text="Home", font=("Arial", 15), command=lambda: controller.show_frame(FirstPage))
        home_button.place(x=650, y=650)
        # Button to previous page
        back_button = tk.Button(self, text="Back", font=("Arial", 15), command=lambda: controller.show_frame(SecondPage))
        back_button.place(x=100, y=650)

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
        convert_calories_button = tk.Button(self, text="Convert Calories to Joules", font=("Arial", 15), command=convert_calories_to_joules)
        convert_calories_button.place(x=100, y=500)

        # Button to convert joules to calories
        convert_joules_button = tk.Button(self, text="Convert Joules to Calories", font=("Arial", 15), command=convert_joules_to_calories)
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
        calculate_button = tk.Button(self, text="Calculate Calories", font=("Arial", 15), command=calculate_calories)
        calculate_button.place(x=400, y=300)



# Create FirstPage class
class FirstPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

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
        self.show_frame(ThirdPage)

    def show_frame(self, page):
        frame = self.frames[page]
        # Raises the frame to the top, making it visible in the GUI
        frame.tkraise()
        # Title
        self.title("Diet_gui")

app = Application()
app.maxsize(800, 800)
# Run the main event loop
app.mainloop()
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

        self.configure(bg='grey')
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

        label = tk.Label(self, text=text, font=("Arial", 18), wraplength=700, justify="left", fg="black", bg="grey", highlightthickness=0, highlightbackground="grey")
        label.place(x=50, y=200)
        
        # Add NextButton frame
        next_button = NextButton(self, controller)
        next_button.place(x=0, y=0)

        # Add BackButton frame
        back_button = BackButton(self, controller)
        back_button.place(x=0, y=0)

# Create ThirdPage class
class ThirdPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

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
        self.show_frame(SecondPage)

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
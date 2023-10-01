import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime, timedelta
import main  # Import your main script as a module

# Create a custom font
custom_font = ("Times New Roman", 20)

# Function to generate a graph based on the selected crop
def generate_graph():
    selected_crop = crop_var.get()

    if selected_crop in crop_data:
        data = crop_data[selected_crop]
        y = data["y"]

        today = datetime.now()
        future_year = today.year + years_into_future
        x = list(range(today.year, future_year + 1))

        plt.figure(figsize=(8, 4))
        plt.plot(x, y)
        plt.xlabel("Year")
        plt.ylabel("Growing Degree Days")
        plt.title(f"Future Growing Degree Days for {selected_crop}")
        plt.grid(True)
        plt.show()


# Function to update plant and harvest date labels
def update_dates():
    plant_date_label.config(text=f"Plant Date: {main.plant_date}")
    harvest_date_label.config(text=f"Harvest Date: {main.harvest_date}")

# Create the main window
root = tk.Tk()
root.title("Crop Harvest Analysis")

# Load the background image (corn.jpg) from the project directory
bg_image = Image.open('corn.jpg')
bg_photo = ImageTk.PhotoImage(bg_image)

# Create a label to display the background image
bg_label = tk.Label(root, image=bg_photo)
bg_label.place(relwidth=1, relheight=1)

# Create a list of available crops
crops = ["Corn", "Wheat", "Rice", "Soybeans"]

# Dictionary to map crops to their data (replace with your actual data)
crop_data = {
    "Corn": {"y": [10, 15, 7, 12, 9, 0]},
    "Wheat": {"y": [8, 11, 6, 9, 7, 0]},
    "Rice": {"y": [12, 17, 10, 14, 11, 0]},
    "Soybeans": {"y": [9, 14, 8, 11, 10, 0]},
}

# Define the number of years into the future to display on the graph
years_into_future = 5

# Create and configure the crop selection combobox
crop_label = ttk.Label(root, text="Select Crop:", font=custom_font)
crop_label.pack()

crop_var = tk.StringVar()
crop_combobox = ttk.Combobox(root, textvariable=crop_var, values=crops, font=custom_font)
crop_combobox.pack()

# Create a custom style for the buttons
button_style = ttk.Style()
button_style.configure("Custom.TButton", font=custom_font)

# Create and configure the submit button with the custom style
submit_button = ttk.Button(root, text="Submit", command=generate_graph, style="Custom.TButton")
submit_button.pack()

# Create and configure the label for best day
best_day_label = ttk.Label(root, text="Best Day of Harvest:", font=custom_font)
best_day_label.pack()

# Create labels for plant date and harvest date
plant_date_label = ttk.Label(root, text="Plant Date:", font=custom_font)
plant_date_label.pack()

harvest_date_label = ttk.Label(root, text="Harvest Date:", font=custom_font)
harvest_date_label.pack()

# Create and configure the update dates button
update_dates_button = ttk.Label(root, text="Update Dates", font=custom_font)
update_dates_button.pack()

# Run the Tkinter main loop
root.mainloop()


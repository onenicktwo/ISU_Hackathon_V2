import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime, timedelta

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

# Function to update the best day label to the future year
# Function to calculate optimal GDD for the selected crop
def calculate_optimal_gdd():
    selected_crop = crop_var.get()

    if selected_crop in crop_data:
        data = crop_data[selected_crop]
        high_temp = data["high_temp"]
        low_temp = data["low_temp"]
        base_temp = data["base_temp"]

        # Calculate optimal GDD using the GDD calculator module
        gdd_values = [gdd_calculator.get_gdd(high, low, base_temp) for high, low in zip(high_temp, low_temp)]
        optimal_gdd = sum(gdd_values)  # You can customize how you want to calculate the optimal GDD

        # Update the label to display the optimal GDD
        optimal_gdd_label.config(text=f"Optimal GDD for {selected_crop}: {optimal_gdd:.2f}")


# Create and configure the label for displaying optimal GDD
optimal_gdd_label = ttk.Label(main_frame, text="", font=custom_font)
optimal_gdd_label.pack(pady=10)  # Add vertical space

# ... (Rest of your UI code) ...

# Modify the "Submit" button command to call the calculate_optimal_gdd function
submit_button = ttk.Button(main_frame, text="Calculate Optimal GDD", command=calculate_optimal_gdd,
                           style="Custom.TButton")
submit_button.pack(pady=20)  # Add vertical space

# Create the main window
root = tk.Tk()
root.title("Crop Harvest Analysis")

# Load the background image (corn.jpg) from the project directory
bg_image = Image.open('corn.jpg')
bg_photo = ImageTk.PhotoImage(bg_image)

# Create a label to display the background image
bg_label = tk.Label(root, image=bg_photo)
bg_label.pack(fill="both", expand=True)  # Expand to fill the entire window

# Create and configure a frame for better spacing
main_frame = ttk.Frame(root)
main_frame.pack(padx=20, pady=20)  # Add padding around the frame

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

# Create and configure the crop selection combobox with space gaps
crop_label = ttk.Label(main_frame, text="Select Crop:", font=custom_font)
crop_label.pack(pady=10)  # Add vertical space

crop_var = tk.StringVar()
crop_combobox = ttk.Combobox(main_frame, textvariable=crop_var, values=crops, font=custom_font)
crop_combobox.pack(pady=10)  # Add vertical space

# Create a custom style for the buttons
button_style = ttk.Style()
button_style.configure("Custom.TButton", font=custom_font)

# Create and configure the submit button with space gaps
submit_button = ttk.Button(main_frame, text="Submit", command=generate_graph, style="Custom.TButton")
submit_button.pack(pady=20)  # Add vertical space

# Create and configure the label for best day with space gaps
best_day_label = ttk.Label(main_frame, text="Best Day of Harvest:", font=custom_font)
best_day_label.pack(pady=10)  # Add vertical space

# Create and configure the update best day button with space gaps
update_best_day_button = ttk.Button(main_frame, text="Update Best Day", command=update_best_day, style="Custom.TButton")
update_best_day_button.pack(pady=20)  # Add vertical space

# Run the Tkinter main loop
root.mainloop()

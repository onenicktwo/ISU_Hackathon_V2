import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime, timedelta  # Import the datetime module

# Create a custom font
custom_font = ("Times New Roman", 20)


# Function to generate a graph based on the selected crop
def generate_graph():
    selected_crop = crop_var.get()

    # Check if the selected crop exists in the data dictionary
    if selected_crop in crop_data:
        data = crop_data[selected_crop]
        y = data["y"]

        # Calculate x-axis values from the current year to the current year plus the future years
        today = datetime.now()
        future_year = today.year + years_into_future
        x = list(range(today.year, future_year + 1))

        plt.figure(figsize=(8, 4))
        plt.plot(x, y)
        plt.xlabel("Year")
        plt.ylabel("Growing Degree Days")  # Change the y-axis label
        plt.title(f"Future Growing Degree Days for {selected_crop}")  # Change the graph title
        plt.grid(True)
        plt.show()


# Function to update the best day label to the future year
# Function to update the best day label to the future year
def update_best_day():
    selected_crop = crop_var.get()  # Get the selected crop from the combobox

    # Check if the selected crop exists in the data dictionary
    if selected_crop in crop_data:
        data = crop_data[selected_crop]
        max_yield = max(data["y"])  # Find the maximum yield
        peak_day_index = np.argmax(data["y"])  # Find the index of the peak day

        # Calculate the future year based on today's date and the peak day index
        today = datetime.now()
        future_year = today.year + peak_day_index  # Calculate the future year

        best_day_label.config(text=f"Best Day of Harvest for {selected_crop}: Year {future_year}, Yield {max_yield}")


# Create the main window
root = tk.Tk()
root.title("Crop Harvest Analysis")

# Create a list of available crops
crops = ["Corn", "Wheat", "Rice", "Soybeans"]  # Add more crops as needed

# Dictionary to map crops to their data (replace with your actual data)
# Dictionary to map crops to their data (replace with your actual data)
crop_data = {
    "Corn": {"y": [10, 15, 7, 12, 9, 0]},  # Add an extra year of data for consistency
    "Wheat": {"y": [8, 11, 6, 9, 7, 0]},  # Add an extra year of data for consistency
    "Rice": {"y": [12, 17, 10, 14, 11, 0]},  # Add an extra year of data for consistency
    "Soybeans": {"y": [9, 14, 8, 11, 10, 0]},  # Add an extra year of data for consistency
}


# Define the number of years into the future to display on the graph
years_into_future = 5  # Change this value as needed

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

# Create and configure the update best day button
update_best_day_button = ttk.Button(root, text="Update Best Day", command=update_best_day, style="Custom.TButton")
update_best_day_button.pack()

# Run the Tkinter main loop
root.mainloop()

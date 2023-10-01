import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import main  # Import your main script as a module

# Create a custom font
custom_font = ("Times New Roman", 20)

# Function to generate the graph based on the selected crop
def generate_graph():
    selected_crop = crop_var.get()

    if selected_crop:
        # Retrieve year and GDD values from your main script
        years = main.year
        gdd_values = main.gdd_values

        # Create a new figure
        fig = plt.figure(figsize=(8, 4))
        ax = fig.add_subplot(111)
        ax.plot(years, gdd_values)
        ax.set_xlabel("Year")
        ax.set_ylabel("Growing Degree Days")
        ax.set_title(f"Growing Degree Days for {selected_crop}")
        ax.grid(True)

        # Embed the Matplotlib figure in the Tkinter window
        canvas = FigureCanvasTkAgg(fig, master=graph_frame)
        canvas.get_tk_widget().pack()

        # Update the canvas
        canvas.draw()

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

# Create a list of available crops (you can modify this if needed)
crops = ["Crop 1", "Crop 2", "Crop 3"]

# Create and configure the crop selection combobox
crop_label = ttk.Label(root, text="Select Crop:", font=custom_font)
crop_label.pack(pady=10)

crop_var = tk.StringVar()
crop_combobox = ttk.Combobox(root, textvariable=crop_var, values=crops, font=custom_font)
crop_combobox.pack(pady=10)

# Create a custom style for the buttons
button_style = ttk.Style()
button_style.configure("Custom.TButton", font=custom_font)

# Create and configure the submit button with the custom style
submit_button = ttk.Button(root, text="Generate Graph", command=generate_graph, style="Custom.TButton")
submit_button.pack(pady=10)

# Create and configure the label for best day
best_day_label = ttk.Label(root, text="Best Day of Harvest:", font=custom_font)
best_day_label.pack(pady=10)

# Create labels for plant date and harvest date
plant_date_label = ttk.Label(root, text="Plant Date:", font=custom_font)
plant_date_label.pack(pady=10)

harvest_date_label = ttk.Label(root, text="Harvest Date:", font=custom_font)
harvest_date_label.pack(pady=10)

# Create and configure the update dates button
update_dates_button = ttk.Button(root, text="Update Dates", command=update_dates, style="Custom.TButton")
update_dates_button.pack(pady=10)

# Create a frame to contain the graph
graph_frame = tk.Frame(root)
graph_frame.pack(pady=10)

# Run the Tkinter main loop
root.mainloop()

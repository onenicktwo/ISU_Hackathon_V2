import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from datetime import datetime, timedelta
import main  # Import your main script as a module

# Create a custom font
custom_font = ("Times New Roman", 20)


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

# Create a canvas for plotting the GDD data
gdd_canvas = tk.Canvas(root, width=800, height=400)
gdd_canvas.pack(pady=10)


# Function to generate the GDD graph
def generate_gdd_graph():
    # Get GDD data from main.py (replace with your actual data)
    years = main.years  # List of years
    gdd_data = main.gdd_data  # List of GDD values

    # Create a canvas for the graph
    gdd_canvas.delete("all")

    # Calculate the canvas dimensions
    canvas_width = 800
    canvas_height = 400
    padding = 20
    x_scale = (canvas_width - 2 * padding) / len(years)
    max_gdd = max(gdd_data)
    y_scale = (canvas_height - 2 * padding) / max_gdd

    # Draw x and y axes
    gdd_canvas.create_line(padding, canvas_height - padding, canvas_width - padding, canvas_height - padding)
    gdd_canvas.create_line(padding, padding, padding, canvas_height - padding)

    # Draw data points and lines
    for i in range(len(years)):
        x = padding + i * x_scale
        y = canvas_height - padding - gdd_data[i] * y_scale
        gdd_canvas.create_oval(x - 5, y - 5, x + 5, y + 5, fill="blue")
        if i < len(years) - 1:
            x_next = padding + (i + 1) * x_scale
            y_next = canvas_height - padding - gdd_data[i + 1] * y_scale
            gdd_canvas.create_line(x, y, x_next, y_next, fill="blue")

    # Add labels
    for i in range(len(years)):
        x = padding + i * x_scale
        gdd_canvas.create_text(x, canvas_height - padding + 10, text=str(years[i]))

    gdd_canvas.create_text(padding - 30, canvas_height - padding, text="GDD", anchor="w", fill="blue")
    gdd_canvas.create_text(padding, padding - 10, text="Year", anchor="n", fill="blue")


# Create and configure the generate GDD graph button
generate_graph_button = ttk.Button(root, text="Generate GDD Graph", command=generate_gdd_graph, style="Custom.TButton")
generate_graph_button.pack(pady=10)

# Run the Tkinter main loop
root.mainloop()

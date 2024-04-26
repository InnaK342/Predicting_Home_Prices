import tkinter as tk
from tkinter import ttk
import util

def calculate_price():
    location = location_var.get()
    sqft = float(sqft_entry.get())
    rooms = int(rooms_entry.get())
    baths = int(baths_entry.get())

    estimated_price = util.get_estimated_price(location, sqft, rooms, baths)
    result_label.config(text=f"Estimated Price: {estimated_price} units")

# Load saved artifacts
util.load_saved_artifacts()

# Create main window
root = tk.Tk()
root.title("House Price Estimator")

# Create labels and entries for user input
sqft_label = tk.Label(root, text="Square Feet:")
sqft_label.grid(row=0, column=0, padx=10, pady=5)
sqft_entry = tk.Entry(root)
sqft_entry.grid(row=0, column=1, padx=10, pady=5)

rooms_label = tk.Label(root, text="Number of Rooms:")
rooms_label.grid(row=1, column=0, padx=10, pady=5)
rooms_entry = tk.Entry(root)
rooms_entry.grid(row=1, column=1, padx=10, pady=5)

baths_label = tk.Label(root, text="Number of Bathrooms:")
baths_label.grid(row=2, column=0, padx=10, pady=5)
baths_entry = tk.Entry(root)
baths_entry.grid(row=2, column=1, padx=10, pady=5)

location_label = tk.Label(root, text="Location:")
location_label.grid(row=3, column=0, padx=10, pady=5)
location_var = tk.StringVar()
location_combobox = ttk.Combobox(root, textvariable=location_var, state='readonly')
location_combobox['values'] = util.get_location_names()
location_combobox.grid(row=3, column=1, padx=10, pady=5)

calculate_button = tk.Button(root, text="Calculate Price", command=calculate_price)
calculate_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

result_label = tk.Label(root, text="")
result_label.grid(row=5, column=0, columnspan=2)

root.mainloop()

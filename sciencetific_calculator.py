
import tkinter as tk
import math

# Function to perform calculation
def calculate():
    try:
        result = eval(entry.get())  # Evaluating the mathematical expression
        entry.delete(0, tk.END)     # Clearing the entry field
        entry.insert(tk.END, result)  # Displaying the result
    except:
        entry.delete(0, tk.END)     # Clearing the entry field
        entry.insert(tk.END, "Error")  # Displaying "Error" in case of invalid expression

# Function to perform square root calculation
def square_root():
    try:
        result = math.sqrt(float(entry.get()))  # Calculating square root
        entry.delete(0, tk.END)     # Clearing the entry field
        entry.insert(tk.END, result)  # Displaying the result
    except:
        entry.delete(0, tk.END)     # Clearing the entry field
        entry.insert(tk.END, "Error")  # Displaying "Error" in case of invalid input

# Creating the main window
window = tk.Tk()
window.title("Scientific Calculator")

# Creating the entry field
entry = tk.Entry(window, width=30, justify=tk.RIGHT)
entry.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

# Creating the calculator buttons
buttons = [
    "7", "8", "9", "/", "sqrt",
    "4", "5", "6", "*", "^",
    "1", "2", "3", "-", "pi",
    "0", ".", "=", "+", "C"
]

# Function to handle button clicks
def button_click(text):
    if text == "=":
        calculate()
    elif text == "sqrt":
        square_root()
    elif text == "C":
        entry.delete(0, tk.END)
    elif text == "pi":
        entry.insert(tk.END, math.pi)
    elif text == "^":
        entry.insert(tk.END, "**")
    else:
        entry.insert(tk.END, text)

# Creating and placing the calculator buttons
row = 1
col = 0
for button in buttons:
    tk.Button(window, text=button, width=10, command=lambda btn=button: button_click(btn)).grid(row=row, column=col, padx=5, pady=5)
    col += 1
    if col > 4:
        col = 0
        row += 1

# Running the main window's event loop
window.mainloop()

import tkinter as tk

# Function to perform calculation
def calculate():
    try:
        result = eval(entry.get())  # Evaluating the mathematical expression
        entry.delete(0, tk.END)     # Clearing the entry field
        entry.insert(tk.END, result)  # Displaying the result
    except:
        entry.delete(0, tk.END)     # Clearing the entry field
        entry.insert(tk.END, "Error")  # Displaying "Error" in case of invalid expression

# Creating the main window
window = tk.Tk()
window.title("Calculator")

# Creating the entry field
entry = tk.Entry(window, width=30, justify=tk.RIGHT)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Creating the calculator buttons
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+"
]

# Function to handle button clicks
def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(number))

# Creating and placing the calculator buttons
row = 1
col = 0
for button in buttons:
    if button == "=":
        tk.Button(window, text=button, width=10, command=calculate).grid(row=row, column=col, padx=5, pady=5)
    else:
        tk.Button(window, text=button, width=10, command=lambda num=button: button_click(num)).grid(row=row, column=col, padx=5, pady=5)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Running the main window's event loop
window.mainloop()


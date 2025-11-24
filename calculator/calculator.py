import tkinter as tk
#----------------------------------------------------------------
# Create main window
root = tk.Tk()
root.title("Cute Calculator")
root.geometry("350x500")  # Adjusted size for a compact design
root.configure(bg="#FFC0CB")  # Light pink background

#----------------------------------------------------------------
# Define colors
button_bg = "#FF69B4"  # Hot pink
button_fg = "white"
display_bg = "#FFB6C1"  # Light pink for display
display_fg = "black"

#----------------------------------------------------------------
## Create a display screen
display = tk.Entry(root, font=("Arial", 20), bg=display_bg, fg=display_fg, bd=10, relief="flat", justify="right")
display.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=15, pady=10)

#----------------------------------------------------------------
# Function to handle button clicks
def on_click(value):
    if value == "=":
        try:
            expression = display.get()
            expression = expression.replace("%", "/100")  # Convert % to divide by 100
            result = eval(expression)  # Evaluate the updated expression
            display.delete(0, tk.END)
            display.insert(tk.END, result)
        except Exception:
            display.delete(0, tk.END)
            display.insert(tk.END, "Error")
    
    elif value == "C":
        display.delete(0, tk.END)  # Clear display
    
    elif value == "(":
        # Automatically insert * before ( if previous character is a number or )
        if display.get() and (display.get()[-1].isdigit() or display.get()[-1] == ")"):
            display.insert(tk.END, "*(")
        else:
            display.insert(tk.END, "(")
    
    else:
        display.insert(tk.END, value)  # Insert clicked button value
        
#----------------------------------------------------------------
# Button layout
buttons = [
    ("(", 1, 0), (")", 1, 1), ("%", 1, 2), ("C", 1, 3),
    ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("/", 2, 3),
    ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("*", 3, 3),
    ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("-", 4, 3),
    ("0", 5, 0), (".", 5, 1), ("=", 5, 2), ("+", 5, 3)  
    # Clear button (row 5, column 0)
]

#----------------------------------------------------------------
# Function to create buttons
for text, row, col in buttons:
    btn = tk.Button(root, text=text, font=("Arial", 15), bg=button_bg, fg=button_fg,
                    width=5, height=2, bd=4, relief="raised", cursor="hand2",
                    command=lambda t=text: on_click(t))  # Make button clickable
    btn.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

#----------------------------------------------------------------
# Run the GUI
root.mainloop()
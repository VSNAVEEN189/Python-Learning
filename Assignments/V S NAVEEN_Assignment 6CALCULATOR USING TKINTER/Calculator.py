from tkinter import *

# Create window
root = Tk()
root.title("Simple Calculator")
root.geometry("300x400")

# Variable to store calculation
calculation = ""

# Function to add numbers/operators
def click(value):
    global calculation
    calculation = calculation + str(value)
    entry.delete(0, END)
    entry.insert(END, calculation)

# Function to calculate result
def answer():
    global calculation

    try:
        result = eval(calculation)
        entry.delete(0, END)
        entry.insert(END, result)
        calculation = str(result)

    except:
        entry.delete(0, END)
        entry.insert(END, "Error")
        calculation = ""

# Function to clear screen
def clear():
    global calculation
    calculation = ""
    entry.delete(0, END)

# Entry box
entry = Entry(root, font=("Arial", 20), justify="right")
entry.pack(fill=BOTH, ipadx=8, ipady=15, padx=10, pady=10)

# Buttons Frame
frame = Frame(root)
frame.pack()

# Row 1
Button(frame, text="7", width=5, height=2,
       command=lambda: click(7)).grid(row=0, column=0)

Button(frame, text="8", width=5, height=2,
       command=lambda: click(8)).grid(row=0, column=1)

Button(frame, text="9", width=5, height=2,
       command=lambda: click(9)).grid(row=0, column=2)

Button(frame, text="/", width=5, height=2,
       command=lambda: click("/")).grid(row=0, column=3)

# Row 2
Button(frame, text="4", width=5, height=2,
       command=lambda: click(4)).grid(row=1, column=0)

Button(frame, text="5", width=5, height=2,
       command=lambda: click(5)).grid(row=1, column=1)

Button(frame, text="6", width=5, height=2,
       command=lambda: click(6)).grid(row=1, column=2)

Button(frame, text="*", width=5, height=2,
       command=lambda: click("*")).grid(row=1, column=3)

# Row 3
Button(frame, text="1", width=5, height=2,
       command=lambda: click(1)).grid(row=2, column=0)

Button(frame, text="2", width=5, height=2,
       command=lambda: click(2)).grid(row=2, column=1)

Button(frame, text="3", width=5, height=2,
       command=lambda: click(3)).grid(row=2, column=2)

Button(frame, text="-", width=5, height=2,
       command=lambda: click("-")).grid(row=2, column=3)

# Row 4
Button(frame, text="0", width=5, height=2,
       command=lambda: click(0)).grid(row=3, column=0)

Button(frame, text=".", width=5, height=2,
       command=lambda: click(".")).grid(row=3, column=1)

Button(frame, text="=", width=5, height=2,
       command=answer).grid(row=3, column=2)

Button(frame, text="+", width=5, height=2,
       command=lambda: click("+")).grid(row=3, column=3)

# Clear button
Button(root, text="Clear", width=20, height=2,
       command=clear).pack(pady=10)

# Run window
root.mainloop()
from tkinter import *

# Function to update the input field
def button_click(item):
    global expression
    expression += str(item)
    input_text.set(expression)

# Function to clear the input field
def button_clear():
    global expression
    expression = ""
    input_text.set("")

# Function to calculate the result
def button_equal():
    try:
        global expression
        result = str(eval(expression))  # Evaluate the expression
        input_text.set(result)  # Update the input field with the result
        expression = result  # Store the result as the new expression
    except:
        input_text.set("Error")
        expression = ""

# Main program
window = Tk()
window.geometry('400x500')
window.title('Calculator')

expression = ""
input_text = StringVar()

# Input field
input_frame = Frame(window, width=312, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=1)
input_frame.pack(side=TOP)

input_field = Entry(input_frame, font=('arial', 18, 'bold'), textvariable=input_text, width=50, bg="#eee", bd=0, justify=RIGHT)
input_field.grid(row=0, column=0)
input_field.pack(ipady=10)  # 'ipady' is internal padding to increase the height of the input field

# Button frame
btns_frame = Frame(window, width=400, height=450, bg="grey")
btns_frame.pack()

# First row
clear = Button(btns_frame, text="C", fg="black", width=32, height=3, bd=0, bg="#eee", cursor="hand2", command=lambda: button_clear())
clear.grid(row=0, column=0, columnspan=3)
divide = Button(btns_frame, text="/", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: button_click("/"))
divide.grid(row=0, column=3)

# Second row
seven = Button(btns_frame, text="7", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: button_click(7))
seven.grid(row=1, column=0)
eight = Button(btns_frame, text="8", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: button_click(8))
eight.grid(row=1, column=1)
nine = Button(btns_frame, text="9", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: button_click(9))
nine.grid(row=1, column=2)
multiply = Button(btns_frame, text="*", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: button_click("*"))
multiply.grid(row=1, column=3)

# Third row
four = Button(btns_frame, text="4", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: button_click(4))
four.grid(row=2, column=0)
five = Button(btns_frame, text="5", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: button_click(5))
five.grid(row=2, column=1)
six = Button(btns_frame, text="6", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: button_click(6))
six.grid(row=2, column=2)
subtract = Button(btns_frame, text="-", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: button_click("-"))
subtract.grid(row=2, column=3)

# Fourth row
one = Button(btns_frame, text="1", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: button_click(1))
one.grid(row=3, column=0)
two = Button(btns_frame, text="2", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: button_click(2))
two.grid(row=3, column=1)
three = Button(btns_frame, text="3", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: button_click(3))
three.grid(row=3, column=2)
add = Button(btns_frame, text="+", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: button_click("+"))
add.grid(row=3, column=3)

# Fifth row
zero = Button(btns_frame, text="0", fg="black", width=21, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: button_click(0))
zero.grid(row=4, column=0, columnspan=2)
decimal = Button(btns_frame, text=".", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: button_click("."))
decimal.grid(row=4, column=2)
equals = Button(btns_frame, text="=", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2", command=lambda: button_equal())
equals.grid(row=4, column=3)

window.mainloop()

from tkinter import *

calc = Tk()
calc.title("Simple Calculator")
font_size = ("Verdana", 30)
e = Entry(calc, width=10, borderwidth=5, font=font_size)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def button_clear():
    e.delete(0, END)

def button_equal():
    second_number = e.get()
    e.delete(0, END)

    if math == "addition":
        e.insert(0, f_num + int(second_number))
    if math == "subtraction":
        e.insert(0, f_num - int(second_number))
    if math == "multiplication":
        e.insert(0, f_num * int(second_number))
    if math == "division":
        e.insert(0, f_num / int(second_number))

def button_add():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    e.delete(0, END)

def button_subtract():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    e.delete(0, END)
    
def button_multiply():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    e.delete(0, END)

def button_divide():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    e.delete(0, END)


#define buttons
button_1 = Button(calc, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(calc, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(calc, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(calc, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(calc, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(calc, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(calc, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(calc, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(calc, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(calc, text="0", padx=40, pady=20, command=lambda: button_click(0))

button_add = Button(calc, text="+", padx=40, pady=20, command=button_add)
button_subtract = Button(calc, text="-", padx=41, pady=20, command=button_subtract)
button_multiply = Button(calc, text="*", padx=41, pady=20, command=button_multiply)
button_divide = Button(calc, text="/", padx=41, pady=20, command=button_divide)
button_equal = Button(calc, text="=", padx=88, pady=20, command=button_equal)
button_clear = Button(calc, text="Clear", padx=75, pady=20, command=button_clear)

#put buttons on screen
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)
button_clear.grid(row=4, column=1, columnspan=2)

button_subtract.grid(row=6, column=0)
button_multiply.grid(row=6, column=1)
button_divide.grid(row=6, column=2)

calc.mainloop()

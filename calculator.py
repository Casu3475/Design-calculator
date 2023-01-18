from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import tkinter as tk
import math 

window = tk.Tk()
window.title('Scientific calculator')
window.geometry('383x570+470+20')
window.config(bg="gray11")
window.resizable(False, False)

# -------------------------------------------------------------------------------------------------
#------------------------------------calculator main functions-------------------------------------
# -------------------------------------------------------------------------------------------------
# i create the clear function and its works!
def quit():
    window.destroy() 

# the clear function works too, it claer the whole textarea
def clear():
    entry.delete(0, END)

# the backstage function clear the number you choose
def back():
    last_number = len(entry.get())-1
    entry.delete(last_number)

# the press function write the number you choose in the textarea, all the buttons are linked to this function
def press(input):
    length = len(entry.get())
    entry.insert(length, input)

# define a function for each mathematical operation
def add(x, y, base):
    return x + y

def sub(x, y, base):
    return x - y

def mult(x, y, base):
    return x * y

def div(x, y, base):
    return x / y

def scientific(calculation):
    data = calculation_break("(",calculation)
    if data[0] == 'tan':
        result = math.tan(data[1])
    elif data[0] == 'cos':
        result = math.cos(data[1])
    elif data[0] == 'sin':
        result = math.sin(data[1])

# define the result for each mathematical operation
def equal():
    calculation = entry.get()
    clear()
    # try:

    #     if calculation.find("(") >0:
    #         result = scientific(calculation)
        
    #     elif calculation.find("x") >0:
    #         data = calculation_break("x",calculation)
    #         result = mult(data[0], data[1], 10)

    #     elif calculation.find("/") >0:
    #         data = calculation_break("/",calculation)
    #         result = div(data[0], data[1], 10)

    #     elif calculation.find("+") >0:
    #         data = calculation_break("+",calculation)
    #         result = add(data[0], data[1], 10)

    #     elif calculation.find("-") >0:
    #         data = calculation_break("-",calculation)
    #         result = sub(data[0], data[1], 10)








# -------------------------------------------------------------------------------------------------
#---------------------------------------calculator design------------------------------------------
# -------------------------------------------------------------------------------------------------
#here is the textarea of the calculator-----
entry_string = StringVar()
entry = Entry(window, textvariable = entry_string, foreground="white", background="gray20",border=0, font=("Bahnscrift Semibold", 26))
entry.grid(columnspan=4, ipady=15)

#here are the buttons----------------------
# 1st row
font_value = ("Calibari, 18")
btn_tan = Button(window, text="tan", background="gray11", foreground="spring green", font=font_value, borderwidth=1, relief= SOLID, command=lambda:press("tan(") and tan)  #when you click on the button, it will write tan in the textarea
btn_tan.grid(row=1, column=0, sticky=E+W, ipady=5)

btn_cos = Button(window, text="cos", background="gray11", foreground="spring green", font=font_value, borderwidth=1, relief= SOLID, command=lambda:press("cos("and cos))
btn_cos.grid(row=1, column=1, sticky=E+W, ipady=5)

btn_sin = Button(window, text="sin", background="gray11", foreground="spring green", font=font_value, borderwidth=1, relief= SOLID, command=lambda:press("sin(") and sin)
btn_sin.grid(row=1, column=2, sticky=E+W, ipady=5)

btn_pi = Button(window, text="pi", background="gray11", foreground="spring green", font=font_value, borderwidth=1, relief= SOLID, command=lambda:press("3.141592"))
btn_pi.grid(row=1, column=3, sticky=E+W, ipady=5)

# 2nd row
btn_log = Button(window, text="log", background="gray11", foreground="spring green", font=font_value, borderwidth=1, relief= SOLID, command=lambda:press("Log("))
btn_log.grid(row=2, column=0, sticky=E+W, ipady=5)

btn_ln = Button(window, text="ln", background="gray11", foreground="spring green", font=font_value, borderwidth=1, relief= SOLID, command=lambda:press("Ln("))
btn_ln.grid(row=2, column=1, sticky=E+W, ipady=5)

btn_deg = Button(window, text="deg", background="gray11", foreground="spring green", font=font_value, borderwidth=1, relief= SOLID, command=lambda:press("deg("))
btn_deg.grid(row=2, column=2, sticky=E+W, ipady=5)

btn_rad = Button(window, text="rad", background="gray11", foreground="spring green", font=font_value, borderwidth=1, relief= SOLID, command=lambda:press("rad("))
btn_rad.grid(row=2, column=3, sticky=E+W, ipady=5)


# 3th row
btn_clear = Button(window, text="C", background="gray5", foreground="red", font=font_value, borderwidth=1, relief= SOLID, command=clear)
btn_clear.grid(row=4, columnspan=2, column=0, sticky=E+W, ipady=5)

btn_backspace = Button(window, text="B", background="gray5", foreground="yellow", font=font_value, borderwidth=1, relief= SOLID, command=back)
btn_backspace.grid(row=4, columnspan=2, column=2, sticky=E+W, ipady=5)

# 4th row
btn_7 = Button(window, text="7", background="gray11", foreground="spring green", font=font_value, borderwidth=1, relief= SOLID, command=lambda:press(7))
btn_7.grid(row=5, column=0, sticky=E+W, ipady=5)

btn_8 = Button(window, text="8", background="gray11", foreground="spring green", font=font_value, borderwidth=1, relief= SOLID, command=lambda:press(8))
btn_8.grid(row=5, column=1, sticky=E+W, ipady=5)

btn_9 = Button(window, text="9", background="gray11", foreground="spring green", font=font_value, borderwidth=1, relief= SOLID, command=lambda:press(9))
btn_9.grid(row=5, column=2, sticky=E+W, ipady=5)

btn_div = Button(window, text="/", background="gray5", foreground="spring green", font=font_value, borderwidth=1, relief= SOLID, command=lambda:press("/") and div)
btn_div.grid(row=5, column=3, sticky=E+W, ipady=5)

# 5th row
btn_4 = Button(window, text="4", background="gray11", foreground="spring green", font=font_value, borderwidth=1, relief= SOLID, command=lambda:press(4))
btn_4.grid(row=6, column=0, sticky=E+W, ipady=5)

btn_5 = Button(window, text="5", background="gray11", foreground="spring green", font=font_value, borderwidth=1, relief= SOLID, command=lambda:press(5))
btn_5.grid(row=6, column=1, sticky=E+W, ipady=5)

btn_6 = Button(window, text="6", background="gray11", foreground="spring green", font=font_value, borderwidth=1, relief= SOLID, command=lambda:press(6))
btn_6.grid(row=6, column=2, sticky=E+W, ipady=5)

btn_mul = Button(window, text="x", background="gray5", foreground="spring green", font=font_value, borderwidth=1, relief= SOLID, command=lambda:press("*") and mult)
btn_mul.grid(row=6, column=3, sticky=E+W, ipady=5)

# 6th row
btn_1 = Button(window, text="1", background="gray11", foreground="spring green", font=font_value, borderwidth=1, relief= SOLID, command=lambda:press(1))
btn_1.grid(row=7, column=0, sticky=E+W, ipady=5)

btn_2 = Button(window, text="2", background="gray11", foreground="spring green", font=font_value, borderwidth=1, relief= SOLID, command=lambda:press(2))
btn_2.grid(row=7, column=1, sticky=E+W, ipady=5)

btn_3 = Button(window, text="3", background="gray11", foreground="spring green", font=font_value, borderwidth=1, relief= SOLID, command=lambda:press(3))
btn_3.grid(row=7, column=2, sticky=E+W, ipady=5)

btn_sub = Button(window, text="-", background="gray5", foreground="spring green", font=font_value, borderwidth=1, relief= SOLID, command=lambda:press("-") and sub)
btn_sub.grid(row=7, column=3, sticky=E+W, ipady=5)

# 7th row
btn_dot = Button(window, text=".", background="gray11", foreground="spring green", font=font_value, borderwidth=1, relief= SOLID, command=lambda:press("."))
btn_dot.grid(row=8, column=0, sticky=E+W, ipady=5)

btn_0 = Button(window, text="0", background="gray11", foreground="spring green", font=font_value, borderwidth=1, relief= SOLID, command=lambda:press(0))
btn_0.grid(row=8, column=1, sticky=E+W, ipady=5)

btn_e = Button(window, text="e", background="gray11", foreground="spring green", font=font_value, borderwidth=1, relief= SOLID, command=lambda:press("2.71828"))
btn_e.grid(row=8, column=2, sticky=E+W, ipady=5)

btn_add = Button(window, text="+", background="gray5", foreground="spring green", font=font_value, borderwidth=1, relief= SOLID, command=lambda:press("+") and add)
btn_add.grid(row=8, column=3, sticky=E+W, ipady=5)

# 8th row
btn_equal = Button(window, text="=", background="spring green", foreground="white", font=font_value, borderwidth=1, relief= SOLID, command=equal)
btn_equal.grid(row=9, column=0, columnspan=3, sticky=E+W, ipady=5)

btn_close = Button(window, text="exit", background="gray5", foreground="spring green", font=font_value, borderwidth=1, relief= SOLID, command = quit) #i add the close command, previously defined
btn_close.grid(row=9, column=3, sticky=E+W, ipady=5)



mainloop()
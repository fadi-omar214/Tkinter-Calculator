import tkinter as tk
from tkinter import *

def button_click(num):
  print("Button clicked")
  global equation

  if num != "+/-":
    equation = equation + str(num)
    equationVar.set(equation)
  else:
    number = float(equation)
    if number > 0:
      equation = "-" + equation
      equationVar.set(equation)
    else:
      equation = equation.replace("-", "")
      equationVar.set(equation)

def equate():
  print("Equals")
  global equation
  try:
    total = str(eval(equation))
    equationVar.set(total)
    equation = total
  except (ZeroDivisionError, SyntaxError):
    equationVar.set("Dumbass")
    equation = ""

def clearView():
  global equation 
  print("Clear")
  equation = ""
  equationVar.set("")

def remove():
  global equation
  print("Backspace")
  equation = equation[:-1]
  equationVar.set(equation)

window = tk.Tk()
window.title("Calculator")
window.geometry("400x700")

equation = ""
equationVar = StringVar()

equationDisplay = tk.Entry(window, textvariable=equationVar, state="readonly")
equationDisplay.grid(row=0, column=0, sticky=tk.W+tk.E, pady=5)

buttonframe = tk.Frame(window)
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=1)
buttonframe.columnconfigure(3, weight=1)

backspace = tk.Button(buttonframe, text="X", command=lambda:remove())
backspace.grid(row=0, column=0, sticky=tk.W+tk.E)
clear = tk.Button(buttonframe, text="C", command=clearView)
clear.grid(row=0, column=1, sticky=tk.W+tk.E)
modulus = tk.Button(buttonframe, text="%", command=lambda:button_click("%"))
modulus.grid(row=0, column=2, sticky=tk.W+tk.E)
divide = tk.Button(buttonframe, text="/",  command=lambda:button_click("/"))
divide.grid(row=0, column=3, sticky=tk.W+tk.E)
seven = tk.Button(buttonframe, text="7", command=lambda:button_click("7"))
seven.grid(row=1, column=0, sticky=tk.W+tk.E)
eight = tk.Button(buttonframe, text="8", command=lambda:button_click("8"))
eight.grid(row=1, column=1, sticky=tk.W+tk.E)
nine = tk.Button(buttonframe, text="9", command=lambda:button_click("9"))
nine.grid(row=1, column=2, sticky=tk.W+tk.E)
multiply = tk.Button(buttonframe, text="x", command=lambda:button_click("*"))
multiply.grid(row=1, column=3, sticky=tk.W+tk.E)
four = tk.Button(buttonframe, text="4", command=lambda:button_click("4"))
four.grid(row=2, column=0, sticky=tk.W+tk.E)
five = tk.Button(buttonframe, text="5", command=lambda:button_click("5"))
five.grid(row=2, column=1, sticky=tk.W+tk.E)
six = tk.Button(buttonframe, text="6", command=lambda:button_click("6"))
six.grid(row=2, column=2, sticky=tk.W+tk.E)
subtract = tk.Button(buttonframe, text="-", command=lambda:button_click("-"))
subtract.grid(row=2, column=3, sticky=tk.W+tk.E)
one = tk.Button(buttonframe, text="1", command=lambda:button_click("1"))
one.grid(row=3, column=0, sticky=tk.W+tk.E)
two = tk.Button(buttonframe, text="2", command=lambda:button_click("2"))
two.grid(row=3, column=1, sticky=tk.W+tk.E)
three = tk.Button(buttonframe, text="3", command=lambda:button_click("3"))
three.grid(row=3, column=2, sticky=tk.W+tk.E)
add = tk.Button(buttonframe, text="+", command=lambda:button_click("+"))
add.grid(row=3, column=3, sticky=tk.W+tk.E)
switch = tk.Button(buttonframe, text="+/-", command=lambda: button_click("+/-"))
switch.grid(row=4, column=0, sticky=tk.W+tk.E)
zero = tk.Button(buttonframe, text="0", command=lambda:button_click("0"))
zero.grid(row=4, column=1, sticky=tk.W+tk.E)
decimal = tk.Button(buttonframe, text=".", command=lambda:button_click("."))
decimal.grid(row=4, column=2, sticky=tk.W+tk.E)
equals = tk.Button(buttonframe, text="=", command=equate)
equals.grid(row=4, column=3, sticky=tk.W+tk.E)
buttonframe.grid(row=1, column=0)

tk.mainloop()
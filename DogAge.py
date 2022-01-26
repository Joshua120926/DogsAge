import tkinter

window = tkinter.Tk()

label = tkinter.Label(window, text="Enter Dog Age", font=('Calibri 10'))
a = tkinter.Entry(window)

def calc():
    dogage = int(a.get())
    age = 7 * dogage
    label1 = tkinter.Label(window, text=age).grid(row=4, column=1)

calc_button = tkinter.Button(window, text="calculate", command=calc)

label.grid(row=3, column=1)
a.grid(row=3,column=2)
calc_button.grid(row=5, column=2)

window.mainloop()

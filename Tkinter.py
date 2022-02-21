#Importing
import tkinter
from tkinter import *

window = tkinter.Tk()
window.title("Paint Calculator")

def CalculateCost():
    #Global Variables
    global height1
    global length1
    global length2
    global length3
    global length4

    #Reset Labels
    areaCosts.config(text = "")
    undercoatCosts.config(text = "")
    qualityCosts.config(text = "")
    totalCosts.config(text = "")
    errorLabel.config(text = "")

    #Error Checking
    if len(name.get()) == 0:
        errorLabel.config(text = "Name Missing")
    elif name.get().isdigit():
        errorLabel.config(text = "Name Must Not Be Numeric")

    elif len(userEmail.get()) == 0:
        errorLabel.config(text = "Email Address Missing")
    elif "@" not in str(userEmail.get()):
        errorLabel.config(text = "Email Must Contain @")

    elif len(phoneNumber.get()) == 0:
        errorLabel.config(text = "Phone Number Missing")
    elif not phoneNumber.get().isdigit():
        errorLabel.config(text = "Phone Number Must Be Numeric")
    
    elif len(height1.get()) == 0:
        errorLabel.config(text = "Height 1 Missing")
    elif not height1.get().isdigit():
        errorLabel.config(text = "Height 1 Must Be Numeric")
    elif len(height1.get()) > 1:
        errorLabel.config(text = "Height 1 Must Be Shorter Than 2 Digits")
    elif int(height1.get()) < 2 or int(height1.get()) > 6:
        errorLabel.config(text = "Height 1 Must Be Between 2 and 6 metres")

    elif len(length1.get()) == 0:
        errorLabel.config(text = "Length 1 Missing")
    elif not length1.get().isdigit():
        errorLabel.config(text = "Length 1 Must Be Numeric")
    elif len(length1.get()) > 2:
        errorLabel.config(text = "Height 1 Must Be Shorter Than 3 Digits")
    elif int(length1.get()) < 2 or int(length1.get()) > 25:
        errorLabel.config(text = "Height 1 Must Be Between 2 and 25 metres")

    elif len(length2.get()) == 0:
        errorLabel.config(text = "Length 2 Missing")
    elif not length2.get().isdigit():
        errorLabel.config(text = "Length 2 Must Be Numeric")
    elif len(length2.get()) > 2:
        errorLabel.config(text = "Length 2 Must Be Shorter Than 3 Digits")
    elif int(length2.get()) < 2 or int(length2.get()) > 25:
        errorLabel.config(text = "Length 2 Must Be Between 2 and 25 metres")

    elif len(length3.get()) == 0:
        errorLabel.config(text = "Length 3 Missing")
    elif not length3.get().isdigit():
        errorLabel.config(text = "Length 3 Must Be Numeric")
    elif len(length3.get()) > 2:
        errorLabel.config(text = "Length 3 Must Be Shorter Than 3 Digits")
    elif int(length3.get()) < 2 or int(length3.get()) > 25:
        errorLabel.config(text = "Length 3 Must Be Between 2 and 25 metres")
        
    elif len(length4.get()) == 0:
        errorLabel.config(text = "Length 4 Missing")
    elif not length4.get().isdigit():
        errorLabel.config(text = "Length 4 Must Be Numeric")
    elif len(length4.get()) > 2:
        errorLabel.config(text = "Length 4 Must Be Shorter Than 3 Digits")
    elif int(length4.get()) < 2 or int(length4.get()) > 25:
        errorLabel.config(text = "Length 4 Must Be Between 2 and 25 metres")
        #ADD THE REST OF THE ERROR CHECKS
    else:
        #CostCalculator
        height1var = int(height1.get())
        length1var = int(length1.get())
        length2var = int(length2.get())
        length3var = int(length3.get())
        length4var = int(length4.get())
        qualityType = int(quality.get())
        undercoatType = int(undercoat.get())
        if qualityType == 1:
            qualityCost = 1.75
        elif qualityType == 2:
            qualityCost = 1.00
        else:
            qualityCost = 0.45
        areaCost = height1var * length1var + height1var * length2var + height1var * length3var + height1var * length4var
        if undercoatType == 1:
            undercoatCost = 0.50 * areaCost
        else:
            undercoatCost = 0
        
        #Cost Outputs
        areaCostsText.config(text = "Area Cost: £")
        areaCosts.config(text = str(float(areaCost))+"0")
    
        qualityCostsText.config(text = "Quality Cost: £")
        qualityCosts.config(text = str(float(qualityCost * areaCost))+"0")

        undercoatCostsText.config(text = "Undercoat Cost: £")
        undercoatCosts.config(text = str(float(undercoatCost))+"0")

        totalCostsText.config(text = "Total Cost: £")
        totalCosts.config(text = str(float(undercoatCost + (qualityCost * areaCost)) + areaCost)+"0")

#Label Setup
camculatorTitle = tkinter.Label(window, text = "Shipley College Paints").grid(row=0,column=2)

nameText = tkinter.Label(window, text = "Name").grid(row = 1,column=1)
name = tkinter.Entry(window)

userEmailText = tkinter.Label(window, text = "Email Address").grid(row = 2,column=1)
userEmail = tkinter.Entry(window)

phoneNumberText = tkinter.Label(window, text = "Phone Number").grid(row = 3,column=1)
phoneNumber = tkinter.Entry(window)

height1text = tkinter.Label(window, text = "Height 1").grid(row = 4,column=1)
height1 = tkinter.Entry(window)

length1text = tkinter.Label(window, text = "Length 1").grid(row = 5,column=1)
length1 = tkinter.Entry(window)

length2text = tkinter.Label(window, text = "Length 2").grid(row = 6,column=1)
length2 = tkinter.Entry(window)

length3text = tkinter.Label(window, text = "Length 3").grid(row = 7,column=1)
length3 = tkinter.Entry(window)

length4text = tkinter.Label(window, text = "Length 4").grid(row = 8,column=1)
length4 = tkinter.Entry(window)

errorLabel = tkinter.Label(window, text = "")

calculate = tkinter.Button(window, text = "Calculate", command = CalculateCost, fg = "red").grid(row=11,column=2)

quality = IntVar()
qualityButton1 = Radiobutton(window, text = "Luxury", variable = quality, value = 1, indicator = 1)
qualityButton2 = Radiobutton(window, text = "Standard", variable = quality, value = 2, indicator = 1)
qualityButton3 = Radiobutton(window, text = "Economy", variable = quality, value = 3, indicator = 1)
qualityButton2.invoke()

undercoat = IntVar()
undercoatBox = tkinter.Checkbutton(window, text = "Undercoat",onvalue = 1, offvalue = 0, variable = undercoat)

areaCostsText = tkinter.Label(window)
areaCosts = tkinter.Label(window)
    
qualityCostsText = tkinter.Label(window)
qualityCosts = tkinter.Label(window)

undercoatCostsText = tkinter.Label(window)
undercoatCosts = tkinter.Label(window)

totalCostsText = tkinter.Label(window)
totalCosts = tkinter.Label(window)

#Grid
name.grid(row = 1, column = 2)
userEmail.grid(row = 2, column = 2)
phoneNumber.grid(row = 3, column = 2)
height1.grid(row = 4, column = 2)
length1.grid(row = 5, column = 2)
length2.grid(row = 6, column = 2)
length3.grid(row = 7, column = 2)
length4.grid(row = 8, column = 2)
errorLabel.grid(row=9,column=2)
undercoatBox.grid(row=10,column=2)
qualityButton1.grid(row = 11,column=1)
qualityButton2.grid(row = 12,column=1)
qualityButton3.grid(row = 13,column=1)
areaCostsText.grid(row=18,column=1)
areaCosts.grid(row=18,column=2)
qualityCostsText.grid(row=19,column=1)
qualityCosts.grid(row=19,column=2)
undercoatCostsText.grid(row=20,column=1)
undercoatCosts.grid(row=20,column=2)
totalCostsText.grid(row=21,column=1)
totalCosts.grid(row=21,column=2)

window.mainloop()

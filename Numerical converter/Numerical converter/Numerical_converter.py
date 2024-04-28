from tkinter import *
from token import EQUAL

home = Tk()
home.geometry('455x750+400+100')
home.resizable(False , False)
home.title('Numerical Converter')
home.iconbitmap('C:\\Users\\ama52\\Desktop\\icon.ico')
photo = PhotoImage(file= r"C:\\Users\\ama52\\Desktop\\logo.png")
res = photo.subsample(1,1)
bt = Button(home , text='Numerical Converter',font=('Arial', 33, "bold"), bd=1, fg='#fff', bg='#2a2d36' ,image=res ,compound=TOP ,cursor='heart' )
bt.pack()
home['bg']="#2a2d36"

inputfield = Entry(home, font=('Arial', 20), fg='black', bg='white')
inputfield.pack(fill='x', pady=20)

def key(value):
        inputfield.insert(END, value)


def clear():
    inputfield.delete(0,END)
    display.configure(state='normal')
    display.delete(1.0, END)
    display.configure(state='disabled')
    
def key(value):
    if value == "=":
        try:
            result = eval(inputfield.get())
            inputfield.delete(0, END)
            inputfield.insert(END, str(result))
        except Exception as e:
            inputfield.delete(0, END)
            inputfield.insert(END, "Error")
    else:
        inputfield.insert(END, value)


Numeric = LabelFrame(home, text='Numbers', bg='#2a2d36', fg='white')
Numeric.pack(fill='x', pady=10)
button0 = Button(Numeric, text='0', font=('Arial', 20, "bold"), bd=1, fg='#fff', bg='#2a2d36', width=4, command= lambda : key(0))
button0.grid(row=4, column=0)
button1 = Button(Numeric, text='1', font=('Arial', 20, "bold"), bd=1, fg='#fff', bg='#2a2d36', width=4, command= lambda : key(1))
button1.grid(row=4, column=1)
button2 = Button(Numeric, text='2', font=('Arial', 20, "bold"), bd=1, fg='#fff', bg='#2a2d36', width=4, command= lambda : key(2))
button2.grid(row=4,column=2)
button3 = Button(Numeric, text='3', font=('Arial', 20, "bold"), bd=1, fg='#fff', bg='#2a2d36', width=4, command= lambda : key(3))
button3.grid(row=4,column=3)
button4 = Button(Numeric, text='4', font=('Arial', 20, "bold"), bd=1, fg='#fff', bg='#2a2d36', width=4, command= lambda : key(4))
button4.grid(row=3,column=0)
button5 = Button(Numeric, text='5', font=('Arial', 20, "bold"), bd=1, fg='#fff', bg='#2a2d36', width=4, command= lambda : key(5))
button5.grid(row=3,column=1)
button6 = Button(Numeric, text='6', font=('Arial', 20, "bold"), bd=1, fg='#fff', bg='#2a2d36', width=4, command= lambda : key(6))
button6.grid(row=3,column=2)
button7 = Button(Numeric, text='7', font=('Arial', 20, "bold"), bd=1, fg='#fff', bg='#2a2d36', width=4, command= lambda : key(7))
button7.grid(row=3, column=3)
button8 = Button(Numeric, text='8', font=('Arial', 20, "bold"), bd=1, fg='#fff', bg='#2a2d36', width=4, command= lambda : key(8))
button8.grid(row=2,column=0)
button9 = Button(Numeric, text='9', font=('Arial', 20, "bold"), bd=1, fg='#fff', bg='#2a2d36', width=4, command= lambda : key(9))
button9.grid(row=2,column=1)
buttonA = Button(Numeric, text='A', font=('Arial', 20, "bold"), bd=1, fg='#fff', bg='#2a2d36', width=4,command=lambda : key("A"))
buttonA.grid(row=0,column=0)
buttonB = Button(Numeric, text='B', font=('Arial', 20, "bold"), bd=1, fg='#fff', bg='#2a2d36', width=4, command= lambda : key("B"))
buttonB.grid(row=0, column=1)
buttonC = Button(Numeric, text='C', font=('Arial', 20, "bold"), bd=1, fg='#fff', bg='#2a2d36', width=4, command= lambda : key("C"))
buttonC.grid(row=0, column=2)
buttonD = Button(Numeric, text='D', font=('Arial', 20, "bold"), bd=1, fg='#fff', bg='#2a2d36', width=4, command= lambda : key("D"))
buttonD.grid(row=0, column=3)
buttonE = Button(Numeric, text='E', font=('Arial', 20, "bold"), bd=1, fg='#fff', bg='#2a2d36', width=4, command= lambda : key("E"))
buttonE.grid(row=2, column=2)
buttonF = Button(Numeric, text='F', font=('Arial', 20, "bold"), bd=1, fg='#fff', bg='#2a2d36', width=4, command= lambda : key("F"))
buttonF.grid(row=2, column=3)
buttonclear = Button(Numeric, text='Clear', font=('Arial', 20, "bold"), bd=1, fg='#fff', bg='#3697f5', width=9, command= clear)
buttonclear.place(x=304 , y=162)
button_decimal = Button(Numeric, text='.', font=('Arial', 20, "bold"), bd=1, fg='#fff', bg='#fe9037', width=4, command=lambda: key("."))
button_decimal.place(x=304, y=109)
button_addition = Button(Numeric, text='+', font=('Arial', 20, "bold"), bd=1, fg='#fff', bg='#fe9037', width=4, command=lambda: key("+"))
button_addition.grid(row=0, column=4)
button_subtraction = Button(Numeric, text='-', font=('Arial', 20, "bold"), bd=1, fg='#fff', bg='#fe9037', width=4, command=lambda: key("-"))
button_subtraction.grid(row=0, column=5)
button_multiplication = Button(Numeric, text='*', font=('Arial', 20, "bold"), bd=1, fg='#fff', bg='#fe9037', width=4, command=lambda: key("*"))
button_multiplication.grid(row=2, column=4)
button_division = Button(Numeric, text='/', font=('Arial', 20, "bold"), bd=1, fg='#fff', bg='#fe9037', width=4, command=lambda: key("/"))
button_division.grid(row=2, column=5)
button_equal= Button(Numeric, text='=', font=('Arial', 20, "bold"), bd=1, fg='#fff', bg='#fe9037', width=4, command= lambda :  key("="))
button_equal.grid(row=3,column=5)

def Binary():
    display.configure(state='normal')
    display.delete(1.0, END)
    try:
        val = inputfield.get()
        int_part = int(val.split('.')[0], 2)
        frac_part = 0
        if '.' in val:
            frac_bin = val.split('.')[1]
            frac_part = sum(int(digit) / 2**(i+1) for i, digit in enumerate(frac_bin))
        
        display.insert(END, 'Binary      =  ' + bin(int_part)[2:] + '.' + ''.join(str(int(digit)) for digit in bin(int(frac_part * 2**5))[2:]))
        display.insert(END, '\nOctal        =  ' + oct(int_part)[2:] + '.' + ''.join(str(int(digit)) for digit in oct(int(frac_part * 8**5))[2:]))
        display.insert(END, '\nDecimal  = ' + str(int_part + frac_part))
        display.insert(END, '\nHexaDec  = ' + hex(int_part)[2:] + '.' + ''.join(str(int(digit)) for digit in hex(int(frac_part * 16**5))[2:]))
    except:
        display.insert(END, 'Invalid Input')
    display.configure(state='disabled')


def Octal():
    display.configure(state='normal')
    display.delete(1.0, END)
    try:
        val = inputfield.get()
        int_part = int(val.split('.')[0], 8)
        frac_part = 0
        if '.' in val:
            frac_oct = val.split('.')[1]
            frac_part = sum(int(digit, 8) / 8**(i+1) for i, digit in enumerate(frac_oct))
        
        display.insert(END, 'Binary      =  ' + bin(int_part)[2:] + '.' + ''.join(str(int(digit)) for digit in bin(int(frac_part * 2**5))[2:]))
        display.insert(END, '\nOctal        =  ' + oct(int_part)[2:] + '.' + ''.join(str(int(digit)) for digit in oct(int(frac_part * 8**5))[2:]))
        display.insert(END, '\nDecimal  = ' + str(int_part + frac_part))
        display.insert(END, '\nHexaDec  = ' + hex(int_part)[2:] + '.' + ''.join(str(int(digit)) for digit in hex(int(frac_part * 16**5))[2:]))
    except:
        display.insert(END, 'Invalid Input')
    display.configure(state='disabled')


def Decimal():
    display.configure(state='normal')
    display.delete(1.0, END)
    try:
        val = inputfield.get()
        int_part = int(val.split('.')[0])
        frac_part = 0
        if '.' in val:
            frac_part = float('0.' + val.split('.')[1])

        display.insert(END, 'Binary      =  ' + bin(int_part)[2:] + '.' + ''.join(str(int(digit)) for digit in bin(int(frac_part * 2**5))[2:]))
        display.insert(END, '\nOctal        =  ' + oct(int_part)[2:] + '.' + ''.join(str(int(digit)) for digit in oct(int(frac_part * 8**5))[2:]))
        display.insert(END, '\nDecimal  = ' + str(val))
        display.insert(END, '\nHexaDec  = ' + hex(int_part)[2:] + '.' + ''.join(str(int(digit)) for digit in hex(int(frac_part * 16**5))[2:]))
    except:
        display.insert(END, 'Invalid Input')
    display.configure(state='disabled')


def Hexadecimal():
    display.configure(state='normal')
    display.delete(1.0, END)
    try:
        val = inputfield.get().upper()
        int_part = int(val.split('.')[0], 16)
        frac_part = 0
        if '.' in val:
            frac_hex = val.split('.')[1]
            frac_part = sum(int(digit, 16) / 16**(i+1) for i, digit in enumerate(frac_hex))
        result = int_part + frac_part

        display.insert(END,'Binary   =  ' + bin(int(result))[2:])
        display.insert(END,'\nOctal     =  ' + oct(int(result))[2:])
        display.insert(END,'\nDecimal = ' + str(result))
        display.insert(END,'\nHexaDec = ' + hex(int(result))[2:])
    except:
        display.insert(END, 'Invalid Input')
    display.configure(state='disabled')

button = LabelFrame(home, text="Numerical Systems ", bg='#2a2d36', fg='white')
button.pack(fill='both', pady=5)
binaryButton = Button(button, text="Binary", font=('Arial', 15, "bold"), bd=1, fg='#fff', bg='#2a2d36', width=18, command=Binary)
binaryButton.grid(row=0, column=0)
octalButton = Button(button, text="Octal", font=('Arial', 15, "bold"), bd=1, fg='#fff', bg='#2a2d36', width=18, command=Octal)
octalButton.grid(row=0, column=1)
decimalButton = Button(button, text="Decimal", font=('Arial', 15, "bold"), bd=1, fg='#fff', bg='#2a2d36', width=18, command=Decimal)
decimalButton.grid(row=1, column=0)
hexaButton = Button(button, text="Hexa Decimal", font=('Arial', 15, "bold"), bd=1, fg='#fff', bg='#2a2d36', width=18, command=Hexadecimal)
hexaButton.grid(row=1, column=1)

display = Text(home, font=('Arial', 18), fg='white', bg='#17161b', relief='groove', bd=5)
display.pack(fill='x')
display.configure(state='disabled')

home.mainloop()

import tkinter as tk
from tkinter import messagebox as mb
from convert2 import unit_convert

root = tk.Tk()
root.geometry('400x200')


### Functions for conversion

def convert():
    entry = (txt.get(1.0, tk.END)).strip()
    value = 0
    try:
        value = float(entry)

        result = unit_convert(value, unit2.get().strip(), unit1.get().strip())

        # result_field.config(text=result)
        result_field.config(text=f'{result} {unit2.get()}')
    except ValueError:
        txt.delete(1.0,tk.END)
        result_field.config(text='')
        mb.showerror(title= 'Error', message='Please enter a valid number to convert')
    

def reset():
    txt.delete(1.0, tk.END)
    result_field.config(text='')

instructions = tk.Label(root, text='What would you like to convert?')
instructions.grid(row=0, column=0, columnspan=3, pady=5, padx=50)

# Entry field for conversion
txt = tk.Text(root, width=10, height=2)
txt.grid(row=1, column=0)

# Dropdown for unit selection
options = [
    "meters",
    "kilometers",
    "centimeters",
    "millimeters",
    "inches",
    "feet",
    "yards",
    "miles"
]

unit1 = tk.StringVar()
unit1.set('inches')

drop1= tk.OptionMenu(root, unit1, *options)
drop1.grid(row=1, column=1)

# To connection

to = tk.Label(root, text='to')
to.grid(row=1, column=2 )

# result unit selection
unit2 = tk.StringVar()
unit2.set('feet')

drop2= tk.OptionMenu(root, unit2, *options)
drop2.grid(row=1, column=3)



# Convert button
convert_button = tk.Button(root, text='Convert', command = convert)
convert_button.grid(row=2, column=0)

# Result label

result_label = tk.Label(root, text='Result:\t')
result_label.grid(row=3, column=0)

# Result field
result_field = tk.Label(root, text='')
result_field.grid(row=4, column=0)

# Clear button
clear_button = tk.Button(root, text='Clear', command= reset)
clear_button.grid(row=4, column=1)



root.mainloop()


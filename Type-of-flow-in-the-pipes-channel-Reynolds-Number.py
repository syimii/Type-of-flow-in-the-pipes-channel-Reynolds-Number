# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 10:33:25 2022

@author: alyaizzati.harme
"""
import tkinter as tk

print('\n********************************************************************')
print('*                                                                  *')
print('* Calculate te Reynolds number of the fluid flow in Pipes/Channels *')
print('*                                                                  *')
print('********************************************************************\n')

my_w = tk.Tk()
my_w.geometry("400x200")  # Size of the window 
my_w.title("Please select Pipe or Channel?")  # Adding a title

def display_selected(choice):
    choice = options.get()
    print(choice)

pipe_channel = ['Pipe','Channel']

options = tk.StringVar(my_w)
options.set(pipe_channel[0]) # default value

label = tk.Label(my_w,  text='Select One', width=15 )  
label.grid(row=5,column=1) 

om1 =tk.OptionMenu(my_w, options, *pipe_channel, command=display_selected)
om1.grid(row=5,column=2) 
my_w.mainloop()
choice = options.get()

density = float(input("Enter the density of the fluid (kg/m3): "))
velocity = float(input("Enter the velocity of the fluid (m/s): "))
length = float(input("Enter the length or diameter of the fluid (m): "))
viscosity = float(input("Enter the dynamic viscosity of the fluid (kg/m.s): "))

reynolds_no = (density*velocity*length)/viscosity

print("\nThe Reynolds number of the fluid is", reynolds_no)

if choice == "Pipe":
    if reynolds_no < 2000:
        print("\nIt is a Laminar flow.")
    elif reynolds_no >= 2000 and reynolds_no <= 4000:
        print("\nIt is a Transition flow.")
    else:
        print("\nIt is a Turbulent flow.")
else:
    if reynolds_no <= 500:
        print("\nVery slow (shallow flowing water).")
    elif reynolds_no >= 501 and reynolds_no <= 999:
        print("\nIt is a Transition flow.")
    else:
        print("\nIt is an Ordinary flow.")
        
print('\n************************* End of program ***************************')

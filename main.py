#Abdullah Isaacs

import tkinter
from tkinter import *
root= Tk()
root.title("ticket generator")
root.geometry("400x700")
root.config(bg="skyblue")

# define class --- variables 1) cell no, select ticket no, amount of tickets

class TicketSales:
    myresult=StringVar()
    def __init__(self, master):
        self.cell_label=Label(master, text="Enter Cell No: ").place(x=20, y=200)
        self.cell_entry=Entry(master)
        self.cell_entry.place(x=150, y=200)

        self.select_label=Label(master, text="Select ticket Catagory").place(x=20, y=250)
        self.options = ["select", "soccer", "Movie", "theatre"]
        self.op1 = StringVar(root)
        self.op1.set(self.options[0])
        self.select_option= OptionMenu(master, self.op1, *self.options).place(x=200, y=250)
        self.tick_no=Label(master, text="select number of tickets").place(x=20, y=300)
        self.no_entry=Entry(master)
        self.no_entry.place(x=200, y=300, width="30")
        self.calc_price = Button(master, text="Calculate price", command=self.calculate_price).place(x=100, y=370)
        self.clear_but =Button(master, text="clear selection", command=self.clear).place(x=250,y=370)



        # bottom section

        self.xxx1=Label(master, text="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", bg="skyblue").place(x=50,y=480)
        self.bottom_cell=Label(master, text="", bg="skyblue")
        self.bottom_cell.place(x=50, y=530)
        self.bottom_no = Label(master, text="", bg="skyblue")
        self.bottom_no.place(x=50, y=570)
        self.bottom_price = Label(master, text="", bg="skyblue")
        self.bottom_price.place(x=50, y=600)
        self.xxx2=Label(master, text="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", bg="skyblue").place(x=50, y=640)

    #     bottom section


    def calculate_price(self):

        if self.op1.get() == "soccer":
            result = 40 * int(self.no_entry.get())
            self.bottom_price.config(text="Amount Payable" + str(result))
            self.bottom_cell.config(text="Reservation done by: " + str(self.cell_entry.get()))
            self.bottom_no.config(text="Reservation for: " + str(self.no_entry.get()))

        elif self.op1.get() == "Movie":
            result = 75 * int(self.no_entry.get())
            self.bottom_price.config(text="Amount Payable " + str(result))
            self.bottom_cell.config(text="Reservation done by: " + str(self.cell_entry.get()))
            self.bottom_no.config(text="Reservation for: " + str(self.no_entry.get()))


        elif self.op1.get() == "theatre":
            result = 100 * int(self.no_entry.get())
            self.bottom_price.config(text="Amount Payable " + str(result))
            self.bottom_cell.config(text="reservation done by: " + str(self.cell_entry.get()))
            self.bottom_no.config(text="Reservation for: " + str(self.no_entry.get()))

    def clear(self):
        self.cell_entry.delete(0,END)
        self.no_entry.delete(0,END)
        self.bottom_no.config(text="")
        self.bottom_cell.config(text="")
        self.bottom_price.config(text="")
        self.op1.set(self.options[0])



tick=TicketSales(root)
root.mainloop()



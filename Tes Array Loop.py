from netmiko import ConnectHandler

# option = input("What your choice : ")
# if option == "add":
#     router = int(input("Berapa Jumlah Router yang ada : "))
#
#     keepIP= open("keepip.txt", "a")
#
#     for routers in range(0, router):
#         keepIP.write(input("Masukkan IP Address SSH Tiap Router : "))
#         keepIP.write("\n")
#
#     keepIP.close()
#
# elif option == "remove":
#     keepIP= open("keepip.txt", "w")

# with open("IP SSH Connect.txt", "r") as file:
#  content = file.read()
#  for i in file:
#     first_line = content.split()[i]
#     print(first_line)


# from tkinter import *
# from tkinter import messagebox
# import tkinter as tk
#
# winShow = Tk()
# winShow.geometry("600x500")
#
# with open("IP SSH Connect.txt", "r") as ipaddress:
#     content = ipaddress.read()
#     for row_position in enumerate(ipaddress):
#         device_type = 'cisco_ios'
#         username = 'netautomation'
#         password = 'net123'
#         secret = 'net123'
#
#         conn = ConnectHandler(ip=ipaddress, device_type=device_type, username=username, password=password,
#                               secret=secret)
#         labelShow = Label(winShow, text=conn.send_command('show ip int br\n'))
#         labelShow.grid(row=row_position, column=0)
#
# messagebox.showinfo('Show Interface', 'Menu berhasil dijalankan')
#
# winShow.mainloop()

import tkinter as tk
from tkinter import messagebox

# root = tk.Tk()
#
# canvas1 = tk.Canvas(root, width=300, height=300)
# canvas1.pack()
#
#
# def ExitApplication():
#     MsgBox = tk.messagebox.askquestion('Exit Application', 'Are you sure you want to exit the application',
#                                        icon='warning')
#     if MsgBox == 'yes':
#         root.destroy()
#     else:
#         tk.messagebox.showinfo('Return', 'You will now return to the application screen')
#
#
# button1 = tk.Button(root, text='Exit Application', command=ExitApplication, bg='brown', fg='white')
# canvas1.create_window(150, 150, window=button1)
#
# root.mainloop()

# file = open("IP SSH Conncet.txt", "w")
#
# messagebox.showinfo('Remove IP SSH Connect', 'IP Berhasil Dihapus')
#
# file.close()

# students = int(input("Please enter the amount of students registered : "))
# id_number = ""
#
# for a in range (0, students):
#     id_number = (int(input("Please enter student ID numbers : ")))
#     reg_form = open('reg_form.txt', 'a')
#     reg_form.write("Student ID numbers: \n" + str(id_number))
#
# print ("Thank you, ID numbers saved to txt file reg_form")

# import tkinter as tk
#
# def save():
#     file_name = entry.get()
#     with open(file_name + '.txt', 'w') as file_object:
#         file_object.write(file_name)   # it is unclear if writing the file_name in the newly created file is really what you want.
#
# if __name__ == '__main__':
#     entry = open("mikhail.txt", "a")
#
#     top = tk.Tk()
#     entry_field_variable = tk.StringVar()
#     entry = tk.Entry(top, textvariable=entry_field_variable)
#     entry.write(entry.get())
#     entry.pack()
#     tk.Button(top, text="save", command=save).pack()
#
#     top.mainloop()

# from tkinter import *
#
# root = Tk()
# Label(root, text = "Childs First name").grid(row = 0, sticky = W)
# Label(root, text = "Childs Surname").grid(row = 1, sticky = W)
# Label(root, text = "Childs Year of Birth").grid(row = 2, sticky = W)
# Label(root, text = "Childs Month of Birth").grid(row = 3, sticky = W)
# Label(root, text = "Childs Day of Birth").grid(row = 4, sticky = W)
#
# Fname = Entry(root)
# Sname = Entry(root)
# x = Entry(root)
# y = Entry(root)
# z = Entry(root)
#
#
# Fname.grid(row = 0, column = 1)
# Sname.grid(row = 1, column = 1)
# x.grid(row = 3, column = 1)
# y.grid(row = 2, column = 1)
# z.grid(row = 4, column = 1)
#
# def getInput():
#     name = open("Nama.txt", "a")
#     name.write(Fname.get())
#     name.write = Sname.get()
#     name.write = x.get()
#     name.write = y.get()
#     name.write = z.get()
#     root.destroy()
#
#     # global params
#
#
# Button(root, text = "submit",
#            command = getInput).grid(row = 5, sticky = W)
# mainloop()

from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

# with open("ip ssh connect.txt", "r") as file:
#  content = file.read()
#  first_line = content.split('\n', 1)[0]
#
# print(first_line)


# winShow = Tk()
# winShow.geometry("600x500")
#
# with open("SSH Username Connect.txt") as fileSSH:
#     contentSSH = fileSSH.read()
# with open("IP SSH Conncet.txt", "r") as device_list:
#     for row_position, ipaddress in enumerate(device_list):
#         device_list = {
#             'ip': ipaddress
#         }
#
#         conn = ConnectHandler(ip=ipaddress, device_type=contentSSH.split()[0], username=contentSSH.split()[1],
#                               password=contentSSH.split()[2], secret=contentSSH.split()[3])
#         labelShow = Label(winShow, text=conn.send_command('show ip int br\n'))
#         labelShow.grid(row=row_position, column=0)
#
# messagebox.showinfo('Show Interface', 'Menu berhasil dijalankan')
#
# winShow.mainloop()
#
# except NameError:
# messagebox.showinfo('Show Interface', 'Menu gagal dijalankan!!')


class Circle:

    def __init__(self):
        self.radius = 4


    def circumference(self):
        pi = 3.14
        circumferenceValue = pi * self.radius * 2
        return circumferenceValue

    def printCircumference(self):
        myCircumference = self.circumference()
        return ("Circumferencen of a circle with a radius of " + str(self.radius) + " is " + str(myCircumference))


start = Circle()
print(start.printCircumference())





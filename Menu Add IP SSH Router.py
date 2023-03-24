from netmiko import ConnectHandler
from tkinter import *
from tkinter import messagebox
import tkinter as tk
from PIL import ImageTk, Image

# addIP = Toplevel()
# def savefileIP():
#     file = open("IP SSH Connect.txt", "a")
#     filetext = str(inputTextIP.get(1.0, END))
#     file.write(filetext)
#
#     messagebox.showinfo('Add IP SSH Connect', 'IP Berhasil Ditambahkan')
#
#     file.close()
#
# def secondTab():
#     def savefileSSH():
#         file = open("SSH Username Connect.txt", "a")
#         filetext = str(inputTextSSH.get(1.0, END))
#         file.write(filetext)
#
#         messagebox.showinfo('Add SSH Username', 'User SSH Berhasil Ditambahkan')
#
#         file.close()
#
#     labelsIP.destroy()
#     inputTextIP.destroy()
#     buttonSaveIP.destroy()
#     buttonNext.destroy()
#
#     labelsSSH = Label(addIP, text="Masukkan Secara Berurut Device Type, Username, dan Password, Serta Password Secret Router \n Dengan Tiap Masukan Lalu Diberi Enter")
#     labelsSSH.grid(row=0, column=0, ipady="5")
#
#     inputTextSSH = Text(addIP)
#     inputTextSSH.grid(row=1, padx="15", pady="15")
#
#     buttonSaveSSH = Button(addIP, text="Save", command=savefileSSH, width=15)
#     buttonSaveSSH.grid(row=2, column=0, pady="10")
#
# labelsIP = Label(addIP, text="Masukkan IP SSH Masing Masing Router, Dengan Tiap Masukan Lalu Diberi Enter")
# labelsIP.grid(row=0, column=0, ipady="5")
#
# inputTextIP = Text(addIP)
# inputTextIP.grid(row=1, padx="15", pady="15")
#
# buttonSaveIP = Button(addIP, text="Save", command=savefileIP, width=15)
# buttonSaveIP.grid(row=2, column=0, pady="10")
#
# buttonNext = Button(addIP, text="Next", command=secondTab, width=15)
# buttonNext.grid(row=3, column=0, pady="10")
#
# addIP.mainloop()



# Code Baru

winShow = Tk()
winShow.geometry("600x500")

with open("SSH Username Connect.txt") as fileSSH:
    contentSSH = fileSSH.read()
with open("IP SSH Connect.txt", "r") as device_list:
    for row_position, ipaddress in enumerate(device_list):
        device_list = {
            'ip': ipaddress
        }
        conn = ConnectHandler(ip=ipaddress, device_type=contentSSH.split()[0],
                              username=contentSSH.split()[1],
                              password=contentSSH.split()[2], secret=contentSSH.split()[3])
        labelShow = Label(winShow, text=conn.send_command('show ip int br\n'))
        labelShow.grid(row=row_position, column=0)

messagebox.showinfo('Show Interface', 'Menu berhasil dijalankan')

winShow.mainloop()
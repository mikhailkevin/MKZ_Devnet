from netmiko import ConnectHandler
from tkinter import *
from tkinter import messagebox
import tkinter as tk
from PIL import ImageTk, Image

router = '''
        192.168.17.2
        192.168.17.3
        192.168.17.4
'''.strip().splitlines()

device_type = 'cisco_ios'
username = 'netautomation'
password = 'net123'
secret = 'net123'

def onClick(args):
    if args == 1:
        try:
            winShow = Toplevel()
            winShow.geometry("600x500")

            for row_position,  routers in enumerate(router):
                conn = ConnectHandler(ip=routers, device_type=device_type, username=username, password=password,
                                      secret=secret)
                labelShow= Label(winShow, text=conn.send_command('show ip int br'))
                labelShow.grid(row=row_position, column=0)

            messagebox.showinfo('Show Interface', 'Menu berhasil dijalankan')
            winShow.mainloop()

        except NameError:
            messagebox.showinfo('Show Interface','Menu gagal dijalankan!!')


    elif args == 2:
        try:
            conn = ConnectHandler(ip='192.168.17.2', device_type=device_type, username=username,
                                      password=password, secret=secret)
            conn.enable()
            conn.send_config_set(["interface fa0/0", "ip address 10.10.10.1 255.255.255.0", "no shutdown", "exit"])


            conn = ConnectHandler(ip='192.168.17.3', device_type=device_type, username=username,
                                  password=password, secret=secret)
            conn.enable()
            conn.send_config_set(["interface fa1/0", "ip address 10.10.10.2 255.255.255.0", "no shutdown", "exit"])
            conn.send_config_set(["interface fa2/0", "ip address 20.20.20.1 255.255.255.0", "no shutdown", "exit"])


            conn = ConnectHandler(ip='192.168.17.4', device_type=device_type, username=username,
                                  password=password, secret=secret)
            conn.enable()
            conn.send_config_set(["interface fa1/0", "ip address 20.20.20.2 255.255.255.0", "no shutdown", "exit"])

            messagebox.showinfo('Fill IP Interface', 'Menu berhasil dijalankan')

        except NameError:
            messagebox.showinfo('Fill IP Interface','Menu gagal dijalankan!!')


    elif args == 3:
        try:
            conn = ConnectHandler(ip='192.168.17.2', device_type=device_type, username=username,
                                  password=password, secret=secret)
            conn.enable()
            conn.send_config_set(["router rip", "version 2", "network 10.10.10.0", "network 20.20.20.0", "no shutdown"])
            conn.disconnect()

            conn = ConnectHandler(ip='192.168.17.3', device_type=device_type, username=username,
                                  password=password, secret=secret)
            conn.enable()
            conn.send_config_set(["router rip", "version 2", "network 10.10.10.0", "network 20.20.20.0", "no shutdown"])
            conn.disconnect()

            conn = ConnectHandler(ip='192.168.17.4', device_type=device_type, username=username,
                                  password=password, secret=secret)
            conn.enable()
            conn.send_config_set(["router rip", "version 2", "network 10.10.10.0", "network 20.20.20.0", "no shutdown"])
            conn.disconnect()

            messagebox.showinfo('Configure Routing Dynamic RIP', 'Menu berhasil dijalankan')

        except NameError:
            messagebox.showinfo('Configure Routing Dynamic RIP', 'Menu gagal dijalankan!!')

    elif args == 4:
        try:
            def populate(frame):
                for row_position, routers in enumerate(router):
                    conn = ConnectHandler(ip=routers, device_type=device_type, username=username, password=password,
                                          secret=secret)
                    tk.Label(frame, text=conn.send_command('show ip route')).grid(row=row_position, column=0)

            def onFrameConfigure(canvas):
                canvas.configure(scrollregion=canvas.bbox("all"))

            winShowRoute = tk.Tk()
            winShowRoute.geometry("500x500")
            canvas = tk.Canvas(winShowRoute, borderwidth=0)
            frame = tk.Frame(canvas)
            vsb = tk.Scrollbar(winShowRoute, orient="vertical", command=canvas.yview)
            canvas.configure(yscrollcommand=vsb.set)

            vsb.pack(side="right", fill="y")
            canvas.pack(side="left", fill="both", expand=True)
            canvas.create_window((4, 4), window=frame, anchor="nw")

            frame.bind("<Configure>", lambda event, canvas=canvas: onFrameConfigure(canvas))

            populate(frame)

            messagebox.showinfo('Configure Routing Dynamic RIP', 'Menu berhasil dijalankan')
            winShowRoute.mainloop()

        except NameError:
            messagebox.showinfo('Configure Routing Dynamic RIP', 'Menu gagal dijalankan!!')

window= Tk()
window.geometry("350x500")


labelEmpty1= Label(window, text="          ")
labelEmpty1.grid(row= 0, column= 0)

mainImage = ImageTk.PhotoImage(Image.open("Python-Symbol.png"))
labelImage= Label(image= mainImage)
labelImage.grid(row= 1, column= 1)

labels = Label(window, text="Program Network Automation")
labels.grid(row= 2, column= 1)

button= Button(window, text="Show Interface Router", command= lambda:onClick(1), width= 17)
button.grid(row= 4, column= 1)

button= Button(window, text="Make IP Address Interface", command= lambda:onClick(2), width= 20)
button.grid(row= 5, column= 1)

button= Button(window, text="Make RIP Configuration", command= lambda:onClick(3), width= 20)
button.grid(row= 6, column= 1)

button= Button(window, text="Show IP Route", command= lambda:onClick(4), width= 16)
button.grid(row= 7, column= 1)

window.mainloop()




from netmiko import ConnectHandler
from tkinter import *
from tkinter import messagebox
import tkinter as tk
from PIL import ImageTk, Image

index_ip, root = 0, None
def onClick(args):
    global index_ip, root
    if args == 1:
        def addInfoIPSSH():
            addIPSSH = Toplevel()

            def savefileIPSSH():
                file = open("IP SSH Connect.txt", "a")
                filetext = str(inputTextIP.get(1.0, END))
                file.write(filetext)

                messagebox.showinfo('Add IP SSH Connect', 'IP Berhasil Ditambahkan')

                file.close()

            def secondTabSSH():
                def savefileSSH():
                    file = open("SSH Username Connect.txt", "a")
                    filetext = str(inputTextSSH.get(1.0, END))
                    file.write(filetext)

                    messagebox.showinfo('Add SSH Username', 'User SSH Berhasil Ditambahkan')

                    file.close()

                labelsIP.destroy()
                inputTextIP.destroy()
                buttonSaveIP.destroy()
                buttonNext.destroy()

                labelsSSH = Label(addIPSSH, text="Masukkan Secara Berurut Device Type, Username, dan Password, Serta "
                                                 "Password Secret Router \n Dengan Tiap Masukan Lalu Diberi Enter")
                labelsSSH.grid(row=0, column=0, ipady="5")

                inputTextSSH = Text(addIPSSH)
                inputTextSSH.grid(row=1, padx="15", pady="15")

                buttonSaveSSH = Button(addIPSSH, text="Save", command=savefileSSH, width=15)
                buttonSaveSSH.grid(row=2, column=0, pady="10")

            labelsIP = Label(addIPSSH, text="Masukkan IP SSH Masing Masing Router, Dengan Tiap Masukan Lalu Diberi "
                                            "Enter")
            labelsIP.grid(row=0, column=0, ipady="5")

            inputTextIP = Text(addIPSSH)
            inputTextIP.grid(row=1, padx="15", pady="15")

            buttonSaveIP = Button(addIPSSH, text="Save", command=savefileIPSSH, width=15)
            buttonSaveIP.grid(row=2, column=0, pady="10")

            buttonNext = Button(addIPSSH, text="Next", command=secondTabSSH, width=15)
            buttonNext.grid(row=3, column=0, pady="10")

            addIPSSH.mainloop()

        def addInfoInt():
            def savefileInt():
                file = open("Int Router Connect.txt", "a")
                filetext = str(inputTextInt.get(1.0, END))
                file.write(filetext)

                messagebox.showinfo('Add Int Connect', 'Interface Router Berhasil Ditambahkan')

                file.close()

            interface = Toplevel()

            labelInfoInt = Label(interface, text="Masukkan Interface Masing Masing Router, Dengan Tiap Masukan Lalu "
                                                 "Diberi Enter")
            labelInfoInt.grid(row=0, column=0, ipady="5")

            inputTextInt = Text(interface)
            inputTextInt.grid(row=1, padx="15", pady="15")

            buttonSaveIP = Button(interface, text="Save", command=savefileInt, width=15)
            buttonSaveIP.grid(row=2, column=0, pady="10")

            interface.mainloop()

        def addInfoIP():
            def savefileIP():
                file = open("IP Router Connect.txt", "a")
                filetext = str(inputTextIP.get(1.0, END))
                file.write(filetext)

                messagebox.showinfo('Add IP Address Router Connect', 'IP Address Router Berhasil Ditambahkan')

                file.close()

            addIP = Toplevel()

            labelInfoIP = Label(addIP,
                                 text="Masukkan IP Interface Masing Masing Router, Dengan Tiap Masukan Lalu Diberi "
                                      "Enter")
            labelInfoIP.grid(row=0, column=0, ipady="5")

            inputTextIP = Text(addIP)
            inputTextIP.grid(row=1, padx="15", pady="15")

            buttonSaveIP = Button(addIP, text="Save", command=savefileIP, width=15)
            buttonSaveIP.grid(row=2, column=0, pady="10")

            addIP.mainloop()

        def addInfoIPNetwork():
            def savefileIPNetwork():
                file = open("IP Network Router Connect.txt", "a")
                filetext = str(inputTextIPNetwork.get(1.0, END))
                file.write(filetext)

                messagebox.showinfo('Add IP Network Router Connect', 'IP Address Router Berhasil Ditambahkan')

                file.close()

            addIPNetwork = Toplevel()

            labelInfoIPNetwork = Label(addIPNetwork,
                                 text="Masukkan IP Network Yang Terhubung, Dengan Tiap Masukan Lalu Diberi Enter")
            labelInfoIPNetwork.grid(row=0, column=0, ipady="5")

            inputTextIPNetwork = Text(addIPNetwork)
            inputTextIPNetwork.grid(row=1, padx="15", pady="15")

            buttonSaveIPNetwork = Button(addIPNetwork, text="Save", command=savefileIPNetwork, width=15)
            buttonSaveIPNetwork.grid(row=2, column=0, pady="10")

            addIPNetwork.mainloop()


        addInfo = Tk()

        btnAddIPSSH = Button(addInfo, text="Add Info SSH Connect", command=addInfoIPSSH, width=22)
        btnAddIPSSH.grid(row=0, column=0, pady="10", padx="10")

        btnAddIntIP = Button(addInfo, text="Add Info Interface Router", command=addInfoInt, width=22)
        btnAddIntIP.grid(row=1, column=0, pady="5", padx="10")

        btnAddIP = Button(addInfo, text="Add Info IP Address Router", command=addInfoIP, width=22)
        btnAddIP.grid(row=2, column=0, pady="5", padx="10")

        btnAddIP = Button(addInfo, text="Add Info IP Network Router", command=addInfoIPNetwork, width=22)
        btnAddIP.grid(row=3, column=0, pady="5", padx="10")

        addInfo.mainloop()

    elif args == 2:
        def removeInfoSSH():
            file = open("IP SSH Connect.txt", "w")
            file.close()

            MsgBox = messagebox.askquestion('Remove IP SSH Connect',
                                            'IP Berhasil Dihapus, Ingin Menghapus Juga Untuk User SSH?', icon='warning')
            if MsgBox == "yes":
                file = open("SSH Username Connect.txt", "w")
                file.close()
                messagebox.showinfo('Remove User SSH Connect', 'User Berhasil Dihapus')
            else:
                MsgBox

        def removeInfoInt():
            file = open("Int Router Connect.txt", "w")
            file.close()

            messagebox.showinfo('Rmove Int Router Connect', 'Int Router Berhasil Dihapus')

        def removeInfoIP():
            file = open("IP Router Connect.txt", "w")
            file.close()

            messagebox.showinfo('Remove IP Router Connect', 'IP Router Berhasil Dihapus')

        def removeIPNetwork():
            file = open("IP Network Router Connect.txt", "w")
            file.close()

            messagebox.showinfo('Remove IP Network Router Connect', 'IP Network Router Berhasil Dihapus')

        winRemove = Tk()

        btnRemoveIPSSH = Button(winRemove, text="Remove Info SSH Connect", command=removeInfoSSH, width=22)
        btnRemoveIPSSH.grid(row=0, column=0, pady="10", padx="10")

        btnRemoveIntIP = Button(winRemove, text="Remove Info Interface Router", command=removeInfoInt, width=22)
        btnRemoveIntIP.grid(row=1, column=0, pady="5", padx="10")

        btnRemoveIP = Button(winRemove, text="Remove Info IP Address Router", command=removeInfoIP, width=24)
        btnRemoveIP.grid(row=2, column=0, pady="5", padx="10")

        btnRemoveNetwork = Button(winRemove, text="Remove IP Network Router", command=removeIPNetwork, width=24)
        btnRemoveNetwork.grid(row=2, column=0, pady="5", padx="10")

        winRemove.mainloop()

    elif args == 3:
        try:
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

        except NameError:
            messagebox.showinfo('Show Interface', 'Menu gagal dijalankan!!')

    elif args == 4:
        contentSSH = open("SSH Username Connect.txt").read()
        try:
            ip_address_ssh = open("IP SSH Connect.txt", "r").read().split("\n")[index_ip]
            ip_address_router = open("IP Router Connect.txt", "r").read().split("\n")[index_ip]
            interface = open("Int Router Connect.txt", "r").read().split("\n")[index_ip]
        except:
            messagebox.showinfo('Make IP Interface Router', 'Semua IP Telah di konfigurasi')
            return None

        root = Tk()
        root.geometry("450x100")
        ip_label = Label(root, text=ip_address_ssh)
        ip_label.grid(row=1, column=0)
        interface_label = Label(root, text="Router Angka Berapa Yang Ingin Dikonfigurasi :")
        interface_count = Entry(root)
        interface_label.grid(row=2, column=0)
        interface_count.grid(row=2, column=1)

        def set_interface(count: str, ip_label):
            global index_ip, root
            if not count.isdigit():
                return None
            count = int(count)
            ip_address_ssh = open("IP SSH Connect.txt", "r").read().split("\n")[index_ip]
            ip_address = open("IP Router Connect.txt", "r").read().split("\n")
            interface = open("Int Router Connect.txt", "r").read().split("\n")
            print(ip_address_ssh)
            print(contentSSH.split("\n")[0])
            print(contentSSH.split("\n")[1])
            print(contentSSH.split("\n")[2])
            print(contentSSH.split("\n")[3])

            conn = ConnectHandler(
                ip=ip_address_ssh, device_type=contentSSH.split("\n")[0],
                username=contentSSH.split("\n")[1],
                password=contentSSH.split("\n")[2],
                secret=contentSSH.split("\n")[3]
            )
            conn.enable()
            print("Config Berhasil!")
            if count == 1:
                print([f"interface {interface[0]}", f"ip address {ip_address[0]}", "no shutdown", "exit"])
                print([f"interface {interface[1]}", f"ip address {ip_address[1]}", "no shutdown", "exit"])
                conn.send_config_set(
                    [f"interface {interface[0]}", f"ip address {ip_address[0]}", "no shutdown", "exit"])
                conn.send_config_set(
                    [f"interface {interface[1]}", f"ip address {ip_address[1]}", "no shutdown", "exit"])
            elif count == 2:
                print([f"interface {interface[2]}", f"ip address {ip_address[2]}", "no shutdown", "exit"])
                print([f"interface {interface[3]}", f"ip address {ip_address[3]}", "no shutdown", "exit"])
                conn.send_config_set(
                    [f"interface {interface[2]}", f"ip address {ip_address[2]}", "no shutdown", "exit"])
                conn.send_config_set(
                    [f"interface {interface[3]}", f"ip address {ip_address[3]}", "no shutdown", "exit"])
            elif count == 3:
                print([f"interface {interface[4]}", f"ip address {ip_address[4]}", "no shutdown", "exit"])
                print([f"interface {interface[5]}", f"ip address {ip_address[5]}", "no shutdown", "exit"])
                conn.send_config_set(
                    [f"interface {interface[4]}", f"ip address {ip_address[4]}", "no shutdown", "exit"])
                conn.send_config_set(
                    [f"interface {interface[5]}", f"ip address {ip_address[5]}", "no shutdown", "exit"])
                pass
            index_ip += 1
            try:
                ip_address_ssh = open("IP SSH Connect.txt", "r").read().split("\n")[index_ip]
                ip_address = open("IP Router Connect.txt", "r").read().split("\n")[index_ip]
                interface = open("Int Router Connect.txt", "r").read().split("\n")[index_ip]
            except:
                messagebox.showinfo('info', 'Semua IP Telah di konfigurasi')
                root.quit()
            ip_label.config(text=ip_address_ssh)

        submit = Button(
            root,
            text="Submit",
            width=16,
            command=lambda: set_interface(interface_count.get(), ip_label)
        )
        submit.grid(row=3, column=0, pady="5", padx="5")
        root.mainloop()

    elif args == 5:
        contentSSH = open("SSH Username Connect.txt").read()
        ip_network = open("IP Network Router Connect.txt", "r").read().split("\n")
        with open("IP SSH Connect.txt", "r") as device_list:
            for ip_address in device_list:
                device_list = {
                    'ip': ip_address
                }
                conn = ConnectHandler(
                    ip=ip_address, device_type=contentSSH.split("\n")[0],
                    username=contentSSH.split("\n")[1],
                    password=contentSSH.split("\n")[2],
                    secret=contentSSH.split("\n")[3]
                )
                conn.enable()
                print("Config Berhasil!")
                print(["router rip", "version 2", "network " + ip_network[0], "network " + ip_network[1],
                       "network " + ip_network[2], "exit"])
                conn.send_config_set([
                    "router rip",
                    "version 2",
                    "network " + ip_network[0],
                    "network " + ip_network[1],
                    "network " + ip_network[2],
                    "exit"
                ])

        messagebox.showinfo('info', 'Semua IP Network Pada Router Telah di konfigurasi')


    elif args == 6:
        try:
            def populate(frame):
                with open("SSH Username Connect.txt") as fileSSH:
                    contentSSH = fileSSH.read()
                with open("IP SSH Connect.txt", "r") as device_list:
                    for row_position, ipaddress in enumerate(device_list):
                        device_list = {
                            'ip': ipaddress
                        }
                        conn = ConnectHandler(ip=ipaddress, device_type=contentSSH.split()[0],
                                              username=contentSSH.split()[1], password= contentSSH.split()[2],
                                              secret=contentSSH.split()[3])
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
window.geometry("350x550")

labelEmpty1= Label(window, text="          ")
labelEmpty1.grid(row= 0, column= 0)

mainImage = ImageTk.PhotoImage(Image.open("Python-Symbol.png"))
labelImage= Label(image= mainImage)
labelImage.grid(row= 1, column= 1)

labels = Label(window, text="Program Network Automation")
labels.grid(row= 2, column= 1)

button= Button(window, text="Add Information Router", command= lambda:onClick(1), width= 22)
button.grid(row= 3, column= 1, pady="5")

button= Button(window, text="Remove Information Router", command= lambda:onClick(2), width= 22)
button.grid(row= 4, column= 1, pady="2")

button= Button(window, text="Show Interface Router", command= lambda:onClick(3), width= 17)
button.grid(row= 5, column= 1, pady="2")

button= Button(window, text="Make IP Address Interface", command= lambda:onClick(4), width= 20)
button.grid(row= 6, column= 1, pady="2")

button= Button(window, text="Make RIP Configuration", command= lambda:onClick(5), width= 20)
button.grid(row= 7, column= 1, pady="2")

button= Button(window, text="Show IP Route", command= lambda:onClick(6), width= 16)
button.grid(row= 8, column= 1, pady="2")

window.mainloop()
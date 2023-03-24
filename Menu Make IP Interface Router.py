#Code Lama

from netmiko import ConnectHandler
from tkinter import *
from tkinter import messagebox
import tkinter as tk
from PIL import ImageTk, Image

try:
    with open("IP SSH Connect.txt", "r") as fileIP:
        contentIP = fileIP.read()
    with open("SSH Username Connect.txt", "r") as fileSSH:
        contentSSH = fileSSH.read()
    conn = ConnectHandler(ip=contentIP.split()[0], device_type=contentSSH.split()[0],
                          username=contentSSH.split()[1],
                          password=contentSSH.split()[2], secret=contentSSH.split()[3])
    conn.enable()
    conn.send_config_set(["interface fa0/0", "ip address 10.10.10.1 255.255.255.252", "no shutdown", "exit"])

    conn = ConnectHandler(ip=contentIP.split()[1], device_type=contentSSH.split()[0],
                          username=contentSSH.split()[1],
                          password=contentSSH.split()[2], secret=contentSSH.split()[3])
    conn.enable()
    conn.send_config_set(["interface fa1/0", "ip address 10.10.10.2 255.255.255.252", "no shutdown", "exit"])
    conn.send_config_set(["interface fa2/0", "ip address 20.20.20.1 255.255.255.252", "no shutdown", "exit"])

    conn = ConnectHandler(ip=contentIP.split()[2], device_type=contentSSH.split()[0],
                          username=contentSSH.split()[1],
                          password=contentSSH.split()[2], secret=contentSSH.split()[3])
    conn.enable()
    conn.send_config_set(["interface fa1/0", "ip address 20.20.20.2 255.255.255.252", "no shutdown", "exit"])

    messagebox.showinfo('Fill IP Interface', 'Menu berhasil dijalankan')

except NameError:
    messagebox.showinfo('Make IP Address Router', 'Menu gagal dijalankan!!')


# Code Baru

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
        interface_label = Label(root, text="Ada Berapa Interface didalam Router :")
        interface_count = Entry(root)
        interface_label.grid(row=2, column=0)
        interface_count.grid(row=2, column=1)

        def set_interface(count:str, ip_label):
            global index_ip, root
            if not count.isdigit():
                return None
            count = int(count)
            ip_address_ssh = open("IP SSH Connect.txt", "r").read().split("\n")[index_ip]
            ip_address = open("IP Router Connect.txt", "r").read().split("\n")
            interface = open("Int Router Connect.txt", "r").read().split("\n")
            conn = ConnectHandler(
                ip=ip_address_ssh, device_type=contentSSH.split("\n")[0],
                username=contentSSH.split("\n")[1],
                password=contentSSH.split("\n")[2],
                secret=contentSSH.split("\n")[3]
            )
            conn.enable()

            if count == 1:
                print(([f"interface {interface[0]}",f"ip address {ip_address[0]}","no shutdown","exit"]))
                conn.send_config_set([f"interface {interface[0]}",f"ip address {ip_address[0]}","no shutdown","exit"])
            elif count == 2:
                conn.send_config_set([f"interface {interface[1]}", f"ip address {ip_address[1]}", "no shutdown", "exit"])
                conn.send_config_set([f"interface {interface[2]}", f"ip address {ip_address[2]}", "no shutdown", "exit"])
            elif count == 3:
                conn.send_config_set([f"interface {interface[3]}", f"ip address {ip_address[3]}", "no shutdown", "exit"])
                conn.send_config_set([f"interface {interface[4]}", f"ip address {ip_address[4]}", "no shutdown", "exit"])
                conn.send_config_set([f"interface {interface[5]}", f"ip address {ip_address[4]}", "no shutdown", "exit"])
            elif count == 4:
                conn.send_config_set([f"interface {interface[6]}", f"ip address {ip_address[6]}", "no shutdown", "exit"])
                conn.send_config_set([f"interface {interface[7]}", f"ip address {ip_address[7]}", "no shutdown", "exit"])
                conn.send_config_set([f"interface {interface[8]}", f"ip address {ip_address[8]}", "no shutdown", "exit"])
                conn.send_config_set([f"interface {interface[9]}", f"ip address {ip_address[9]}", "no shutdown", "exit"])
            elif count == 5:
                conn.send_config_set([f"interface {interface[10]}", f"ip address {ip_address[10]}", "no shutdown", "exit"])
                conn.send_config_set([f"interface {interface[11]}", f"ip address {ip_address[11]}", "no shutdown", "exit"])
                conn.send_config_set([f"interface {interface[12]}", f"ip address {ip_address[12]}", "no shutdown", "exit"])
                conn.send_config_set([f"interface {interface[13]}", f"ip address {ip_address[13]}", "no shutdown", "exit"])
            elif count == 6:
                conn.send_config_set([f"interface {interface[14]}", f"ip address {ip_address[14]}", "no shutdown", "exit"])
                conn.send_config_set([f"interface {interface[15]}", f"ip address {ip_address[15]}", "no shutdown", "exit"])
                conn.send_config_set([f"interface {interface[16]}", f"ip address {ip_address[16]}", "no shutdown", "exit"])
                conn.send_config_set([f"interface {interface[17]}", f"ip address {ip_address[17]}", "no shutdown", "exit"])
                conn.send_config_set([f"interface {interface[18]}", f"ip address {ip_address[18]}", "no shutdown", "exit"])
                conn.send_config_set([f"interface {interface[19]}", f"ip address {ip_address[19]}", "no shutdown", "exit"])
            elif count == 7:
                conn.send_config_set([f"interface {interface[20]}", f"ip address {ip_address[20]}", "no shutdown", "exit"])
                conn.send_config_set([f"interface {interface[21]}", f"ip address {ip_address[21]}", "no shutdown", "exit"])
                conn.send_config_set([f"interface {interface[22]}", f"ip address {ip_address[22]}", "no shutdown", "exit"])
                conn.send_config_set([f"interface {interface[23]}", f"ip address {ip_address[23]}", "no shutdown", "exit"])
                conn.send_config_set([f"interface {interface[24]}", f"ip address {ip_address[24]}", "no shutdown", "exit"])
                conn.send_config_set([f"interface {interface[25]}", f"ip address {ip_address[25]}", "no shutdown", "exit"])
                conn.send_config_set([f"interface {interface[26]}", f"ip address {ip_address[26]}", "no shutdown", "exit"])
            elif count == 8:
                conn.send_config_set([f"interface {interface[27]}", f"ip address {ip_address[27]}", "no shutdown", "exit"])
                conn.send_config_set([f"interface {interface[28]}", f"ip address {ip_address[28]}", "no shutdown", "exit"])
                conn.send_config_set([f"interface {interface[29]}", f"ip address {ip_address[29]}", "no shutdown", "exit"])
                conn.send_config_set([f"interface {interface[30]}", f"ip address {ip_address[30]}", "no shutdown", "exit"])
                conn.send_config_set([f"interface {interface[31]}", f"ip address {ip_address[31]}", "no shutdown", "exit"])
                conn.send_config_set([f"interface {interface[32]}", f"ip address {ip_address[32]}", "no shutdown", "exit"])
                conn.send_config_set([f"interface {interface[33]}", f"ip address {ip_address[33]}", "no shutdown", "exit"])
                conn.send_config_set([f"interface {interface[34]}", f"ip address {ip_address[34]}", "no shutdown", "exit"])
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



#Code Baru 2

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
    conn = ConnectHandler(
        ip=ip_address_ssh, device_type=contentSSH.split("\n")[0],
        username=contentSSH.split("\n")[1],
        password=contentSSH.split("\n")[2],
        secret=contentSSH.split("\n")[3]
    )
    conn.enable()
    print("Config Berhasil!")
    if count == 1:
        conn.send_config_set([f"interface {interface[0]}", f"ip address {ip_address[0]}", "no shutdown", "exit"])
        conn.send_config_set([f"interface {interface[1]}", f"ip address {ip_address[1]}", "no shutdown", "exit"])
    elif count == 2:
        conn.send_config_set([f"interface {interface[2]}", f"ip address {ip_address[2]}", "no shutdown", "exit"])
        conn.send_config_set([f"interface {interface[3]}", f"ip address {ip_address[3]}", "no shutdown", "exit"])
    elif count == 3:
        conn.send_config_set([f"interface {interface[4]}", f"ip address {ip_address[4]}", "no shutdown", "exit"])
        conn.send_config_set([f"interface {interface[5]}", f"ip address {ip_address[5]}", "no shutdown", "exit"])
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




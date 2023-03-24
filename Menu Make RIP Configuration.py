try:
    with open("IP SSH Connect.txt", "r") as fileIP:
        contentIP = fileIP.read()
    with open("SSH Username Connect.txt", "r") as fileSSH:
        contentSSH = fileSSH.read()
    conn = ConnectHandler(ip=contentIP.split()[0], device_type=contentSSH.split()[0],
                          username=contentSSH.split()[1],
                          password=contentSSH.split()[2], secret=contentSSH.split()[3])
    conn.enable()
    conn.send_config_set(["router rip", "version 2", "network 10.10.10.0", "network 20.20.20.0", "no shutdown"])
    conn.disconnect()

    conn = ConnectHandler(ip=contentIP.split()[1], device_type=contentSSH.split()[0],
                          username=contentSSH.split()[1],
                          password=contentSSH.split()[2], secret=contentSSH.split()[3])
    conn.enable()
    conn.send_config_set(["router rip", "version 2", "network 10.10.10.0", "network 20.20.20.0", "no shutdown"])
    conn.disconnect()

    conn = ConnectHandler(ip=contentIP.split()[2], device_type=contentSSH.split()[0],
                          username=contentSSH.split()[1],
                          password=contentSSH.split()[2], secret=contentSSH.split()[3])
    conn.enable()
    conn.send_config_set(["router rip", "version 2", "network 10.10.10.0", "network 20.20.20.0", "no shutdown"])
    conn.disconnect()

    messagebox.showinfo('Configure Routing Dynamic RIP', 'Menu berhasil dijalankan')

except NameError:
    messagebox.showinfo('Configure Routing Dynamic RIP', 'Menu gagal dijalankan!!')
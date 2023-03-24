from netmiko import ConnectHandler
import getpass
from past.builtins import raw_input
from types import SimpleNamespace

device = {
    'router0' : {
        'device_type': 'cisco_ios',
        'ip': '192.168.17.170',
        'username': 'netautomation',
        'password': 'net123',
        'secret': 'net123'
    },
    'router1' : {
        'device_type': 'cisco_ios',
        'ip': '192.168.17.171',
        'username': 'netautomation',
        'password': 'net123',
        'secret': 'net123'
    }
}

# for keys,values in device.items():
#     print(keys, ":", values)

for devices in device.items():
        conn = ConnectHandler(**device['router0','device_type','ip','username','password','secret'])
        print(conn.send_command('sh ip int br'))

# def main():
#         pilih = int(input("Pilih Konfigurasi : "))
#         if pilih == 1:
#                 device = {}
#                 inputId = int(input("How many Router In Your Topology? : "))
#                 for i in range(0, inputId):
#                         print("Identity in Router", i + 1)
#                         routerHost = input("Put Your Router Name Here : ")
#                         ipAddress = input("Put Your IP Address Here : ")
#                         username = "netautomation"
#                         password = "net123"
#                         enableSec = "net123"
#                         router = routerHost
#                         ipFill = ipAddress
#                         userFill = username
#                         passFill = password
#                         enableFill = enableSec
#                         if router == router or ipFill == ipFill or userFill == userFill or passFill == passFill or enableFill == enableFill:
#                                 print("<--Successful Adding Information Router ", i + 1, "-->")
#                                 router = router.strip()
#                                 ipFill = ipFill.strip()
#                                 userFill = userFill.strip()
#                                 passFill = passFill.strip()
#                                 enableFill = enableFill.strip()
#                                 device[router] = {ipFill, userFill, passFill, enableFill}
#
#
#
#                 # convert = SimpleNamespace(**device)
#                 inputRouter = input("Pilih Router yang Akan Dikonfigurasi :")
#                 if inputRouter == "router0":
#                         conn = ConnectHandler(**device['router0'])
#                         print(conn.enable())
#                         print(conn.send_command('sh ip int b'))
#                 # elif inputRouter == "router1":
#                 #         conn = ConnectHandler(**convert.router1)
#                 #         print(conn.send_command('sh ip int b'))
#                 # elif inputRouter == "router2":
#                 #         conn = ConnectHandler(**convert.router2)
#                 #         print(conn.send_command('sh ip int b'))
#                 else:
#                         print("Router Yang Anda Masukkan Tidak Ada!!!")
#
#         # elif pilih == 2:
#
#
#
#         repeat = input("Would you like move to Menu? ")
#         if repeat == "yes":
#                 main()
#         else:
#                 print("Thank you for your amazing spirit!!, Comeback later")
#                 exit()
# main()




# for i in  device.items():
#     conn = ConnectHandler(**device)

# key_list = list(device.keys())
# val_list = list(device.values())
#
# position = val_list.index('router-1')

#user exec modedada





#global config mode
# cmd = [
#         'interface loopback 1',
#         'ip address 100.100.100.1 255.255.255.0',
#         'no shutdown'
# ]
# print(conn.send_config_set(cmd))
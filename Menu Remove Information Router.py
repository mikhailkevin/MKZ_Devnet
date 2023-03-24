file = open("IP SSH Connect.txt", "w")
        file.close()

        MsgBox = messagebox.askquestion('Remove IP SSH Connect', 'IP Berhasil Dihapus, Ingin Menghapus Juga Untuk User SSH?', icon='warning')
        if MsgBox == "yes":
            file = open("SSH Username Connect.txt", "w")
            file.close()
            messagebox.showinfo('Remove User SSH Connect', 'User Berhasil Dihapus')
        else:
            MsgBox


removeInfo = Tk()


def removeIPSSH():


labelRemoveInfo = Label(removeInfo, text="Silahkan Pilih Menu Hapus")
labelRemoveInfo.grid(row=0, column=0)

btnRemoveIPSSH = Button(removeInfo, text="Remove Info SSH", width=22)
btnRemoveIPSSH.grid(row=0, column=0, pady="5", command=removeIPSSH, padx="5")

btnRemoveInfoSSH = Button(removeInfo, text="Remove Info Interface Router", width=22)
btnRemoveInfoSSH.grid(row=1, column=0, pady="5", padx="5")

btnRemoveInfoSSH = Button(removeInfo, text="Remove Info IP Address Router", width=22)
btnRemoveInfoSSH.grid(row=2, column=0, pady="5", padx="5", )

removeInfo.mainloop()
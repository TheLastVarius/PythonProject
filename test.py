#coding=UTF8
import Tkinter

root=Tkinter.Tk()
root.geometry("300x200")

def thing_listbox_bind(*args, **kwargs):
    print (thing_listbox.curselection())

thing_listbox = Tkinter.Listbox(root, selectmode= Tkinter.SINGLE)
thing_list_file = open ("thing_list", "r")
for element in thing_list_file:
    thing_listbox.insert(Tkinter.END, element)
thing_listbox.pack()
thing_list_file.close()

thing_listbox.bind("<ButtonRelease-1>", thing_listbox_bind)


root.mainloop()

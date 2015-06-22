#coding=UTF8
import Tkinter

root=Tkinter.Tk()
root.geometry("400x300")
root.title("Сборник статей")
def thing_listbox_bind(*args, **kwargs):
    print (thing_listbox.curselection())

thing_listbox = Tkinter.Listbox(root, selectmode= Tkinter.SINGLE)
thing_list_file = open ("thing_list", "r")
for element in thing_list_file:
    thing_listbox.insert(Tkinter.END, element)
thing_listbox.grid(row = 1, column = 1)
thing_list_file.close()


thing_article_list = Tkinter.Listbox(root, selectmode = Tkinter.SINGLE)
thing_article_list.grid(row = 1, column = 3)

thing_listbox.bind("<ButtonRelease-1>", thing_listbox_bind)


root.mainloop()

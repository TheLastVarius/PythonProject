#coding=UTF8
import Tkinter

root=Tkinter.Tk()
root.geometry("400x300")
root.title("Сборник статей")

login_button = Tkinter.Button(root, text= "Войти как администратор")
login_button.grid(row=2, column=5)

mydict = dict(Admin="admin", User = "user", Log= "log")

u = []
u.append(mydict.items())

log_file = open("log_file", "w")
for element in u:
    for kortej in element:
        print kortej   
        log_file.write(str(kortej))
log_file.close()

mylist = []
log_file=open("log_file", "r")
for line in log_file:
    mylist.append(line)

print mylist


root.mainloop()

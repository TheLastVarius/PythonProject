#coding=UTF8
import Tkinter

root=Tkinter.Tk()
root.geometry("400x300")
root.title("Сборник статей")

login_button = Tkinter.Button(root, text= "Войти как администратор")
login_button.grid(row=2, column=5)


root.mainloop()

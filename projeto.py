from tkinter import *

window = Tk()
window.title("Gestor de Roteiro de Viagens")

#CENTRAR JANELA
w = 500
h = 200
ws = window.winfo_screenwidth()
hs = window.winfo_screenheight()
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
window.geometry('%dx%d+%d+%d' % (w, h, x, y))

#LABEL LOGIN
lbl_login = Label(window, text = "Por favor efetue o seu login ou crie a sua conta", fg = "red", font =("Times New Roman", 14))
lbl_login.place (x=60, y =50)

#BOTÃO PARA LOGIN
btn_login = Button(window, text = "Login", fg = "green", font = ("Calibri", 12))
btn_login.place (x = 214, y = 100)

#BOTÃO PARA CRIAR CONTA
btn_criar = Button(window, text = "Criar conta", fg = "blue", font = ("Calibri", 12))
btn_criar.place (x = 200, y = 140)

#FUNÇÃO CRIAR CONTA







window.mainloop()
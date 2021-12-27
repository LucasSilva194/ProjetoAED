from tkinter import *

window = Tk()
window.title("Gestor de Roteiro de Viagens")

#CRIA UM FICHEIRO CHAMADO basedados.txt CASO O MESMO NÃO EXISTA
f = open("basedados.txt","a")
f.close()

#CENTRAR JANELA PRINCIPAL
w = 500
h = 200
ws = window.winfo_screenwidth()
hs = window.winfo_screenheight()
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
window.geometry('%dx%d+%d+%d' % (w, h, x, y))

#LABEL UTILIZADOR
lbl_utilizador=Label(window,text="Utilizador:",fg="black",font=("Times New Roman",14))
lbl_utilizador.place(x=150,y=20)

#ENTRY UTILIZADOR
txt_utilizador=Entry(window,width=20)
txt_utilizador.place(x=240,y=22)

#LABEL PALAVRA-PASSE
lbl_passe=Label(window,text="Palavra-Passe:",fg="black",font=("Times New Roman",14))
lbl_passe.place(x=150,y=50)

#ENTRY PALAVRA-PASSE
txt_passe=Entry(window,width=20,show="*")
txt_passe.place(x=265,y=53)

#BOTÃO PARA LOGIN
btn_login = Button(window, text = "Login", fg = "green", font = ("Calibri", 12),width=15,height=1)
btn_login.place (x = 190, y = 100)

#BOTÃO PARA CRIAR CONTA
btn_criar = Button(window, text = "Criar Conta", fg = "blue", font = ("Calibri", 12),width=15,height=1)
btn_criar.place (x = 190, y = 140)

#FUNÇÃO CRIAR CONTA
def Login():
    user = txt_utilizador.get()
    password = txt_passe.get()
    
    guardar = user + ";" + password
    f = open("basedados.txt","r")
    lista = f.readlines()

    txt_utilizador.set("")
    txt_passe.set("")

window.mainloop()
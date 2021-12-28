from tkinter import *
import tkinter as tk

window = Tk()
window.title("Gestor de Roteiro de Viagens")

#FUNÇÃO JANELA CRIARCONTA
def janela1(criar):
    criar.top=Toplevel()
    criar.top.geometry()
    criar.top.title("Criar Conta")
    criar.top.focus_force()
    criar.top.grab_set()
    #LABEL JANELA CRIAR CONTA-UTILIZADOR
    lbl_utilizador2=Label(janela1,text="Utilizador:",fg="black",font=("Times New Roman",14))
    lbl_utilizador2.place(x=150,y=20)

    #ENTRY JANELA CRIAR CONTA-UTILIZADOR
    txt_utilizador2=Entry(janela1,width=20)
    txt_utilizador2.place(x=240,y=22)
    
#LABEL JANELA CRIAR CONTA-EMAIL
    lbl_email=Label(janela1,text="Email:",fg="black",font=("Times New Roman",14))
    lbl_email.place(x=150,y=40)

    #ENTRY JANELA CRIAR CONTA-EMAIL
    txt_email=Entry(janela1,width=20)
    txt_email.place(x=180,y=20)

    #LABEL JANELA CRIAR CONTA-PALAVRA PASSE
    lbl_passe2=Label(janela1,text="Palavra-Passe:")
    lbl_passe2.place(x=150,y=60)

    #ENTRY JANELA CRIAR CONTA-PALAVRA-PASSE
    txt_passe2=Entry(janela1,width=20)
    txt_passe2.place(x=180,y=60)

#CENTRAR JANELA
w = 500
h = 200
ws = window.winfo_screenwidth()
hs = window.winfo_screenheight()
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
window.geometry('%dx%d+%d+%d' % (w, h, x, y))

#DEFENIR JANELA INICIAL
original_frame=window

#LABEL UTILIZADOR
lbl_utilizador=Label(window,text="Utilizador:",fg="black",font=("Times New Roman",14))
lbl_utilizador.place(x=150,y=20)

#ENTRY UTILIZADOR
txt_utilizador=Entry(window,width=20)
txt_utilizador.place(x=240,y=22)

#LABEL PALAVRA-PASSE
lbl_passe=Label(window,text="Palavra-Passe:",fg="black",font=("Times New Roman",14))
lbl_passe.place(x=120,y=50)

#ENTRY PALAVRA-PASSE
txt_passe=Entry(window,width=20,show="*")
txt_passe.place(x=240,y=53)

#BOTÃO PARA LOGIN
btn_login = Button(window, text = "Login", fg = "green", font = ("Calibri", 12),width=15,height=1)
btn_login.place (x = 190, y = 100)

#BOTÃO PARA CRIAR CONTA
btn_criar = Button(window, text = "Criar Conta", fg = "blue", font = ("Calibri", 12),width=15,height=1,command=janela1())
btn_criar.place (x = 190, y = 140)

window.mainloop()

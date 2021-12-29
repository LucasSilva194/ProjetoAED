from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Gestor de Roteiro de Viagens")

#CRIA UM FICHEIRO CHAMADO basedados.txt CASO O MESMO NÃO EXISTA
f = open("basedados.txt","a")
f.close()

#FUNÇÃO LOGIN
def Login():
    user = txt_utilizador.get()
    password = txt_passe.get()

    guardar = user + ";" + password
    f = open("basedados.txt","r")
    lista = f.readlines()

    if user == "" or password == "":
        messagebox.showerror("Erro","Por favor forneça os seus dados de Acesso")
    else:
        if str(guardar) in str(lista):
            messagebox.showinfo("Bem vindo",f"Olá {user}, o seu login foi efetuado com sucesso")
        else:
            messagebox.showerror("Tentativa de Login sem sucesso","Utilizador ou palavra-passe incorreta. Por favor tente novamente ou crie conta.")
            txt_passe.delete(0,"end")              

#FUNÇÃO CRIAR CONTA
def CriarConta():
    utilizador = txt_utilizador.get()
    password = txt_passe.get()
    email = txt_email.get()
    cpassword = txt_cpasse.get()

    guardar = utilizador + ";" + email + ";" + password 
    f = open("basedados.txt","r")
    if utilizador == "" or email == "" or password == "" or cpassword == "":
        messagebox.showerror("Erro","Por favor forneça todos os dados corretamente.")

    if utilizador != "" and password != "":
        lista = f.readlines()

        if str(guardar) in str(lista):
            messagebox.showerror("Erro","Já existe uma conta com esses dados, por favor efetue login")
            
        elif str(utilizador) in str(lista):
            messagebox.showerror("Erro","Esse utilizador já existe")
            
        else:
            if password == cpassword:
                f = open("basedados.txt","a")
                f.write(utilizador + ";" + email + ";" + password + ";" + "user""\n")
                messagebox.showinfo("Sucesso","A sua conta foi criada com sucesso!")
                
            else:
                messagebox.showerror("Erro","As duas passwords não coincidem")

#CENTRAR JANELA PRINCIPAL
w = 500
h = 200
ws = window.winfo_screenwidth()
hs = window.winfo_screenheight()
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
window.geometry('%dx%d+%d+%d' % (w, h, x, y))

#------------------EFETUAR LOGIN------------------#

#LABEL UTILIZADOR
lbl_utilizador=Label(window,text="Utilizador:",fg="black",font=("Times New Roman",14))
lbl_utilizador.place(x=120,y=20)

#ENTRY UTILIZADOR
txt_utilizador=Entry(window,width=30)
txt_utilizador.place(x=230,y=22)

#LABEL PALAVRA-PASSE
lbl_passe=Label(window,text="Palavra-Passe:",fg="black",font=("Times New Roman",14))
lbl_passe.place(x=90,y=50)

#ENTRY PALAVRA-PASSE
txt_passe=Entry(window,width=30,show="*")
txt_passe.place(x=230,y=53)

#BOTÃO PARA LOGIN
btn_login = Button(window, text = "Login", fg = "green", font = ("Calibri", 12),width=15,height=1, command = Login)
btn_login.place (x=190,y=100)

#------------------CRIAR UTILIZADOR------------------#

#LABEL E-MAIL
lbl_email=Label(window,text="Email:",fg="black",font=("Times New Roman",14))

#ENTRY E-MAIL
txt_email=Entry(window, width=30)

#LABEL CONFIRMAR PALAVRA-PASSE
lbl_cpasse=Label(window,text="Confirmar Palavra-Passe:",fg="black",font=("Times New Roman",14))

#ENTRY CONFIRMAR PALAVRA-PASSE
txt_cpasse=Entry(window, width=30,show="*")

def nJanela():
    w = 450
    h = 230
    ws = window.winfo_screenwidth()
    hs = window.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    window.geometry('%dx%d+%d+%d' % (w, h, x, y))

    lbl_utilizador.place(x=30,y=20)
    txt_utilizador.place(x=230,y=22)

    lbl_email.place(x=30,y=50)
    txt_email.place(x=230,y=53)

    lbl_passe.place(x=30,y=80)
    txt_passe.place(x=230,y=83)

    lbl_cpasse.place(x=30,y=110)
    txt_cpasse.place(x=230,y=113)

    btn_login.destroy()
    btn_criarconta.destroy()

    btn_criar = Button(window,text="Criar Conta", fg="blue", font = ("Calibri",12), width=15,height=1, command=CriarConta)
    btn_criar.place(x=160,y=160)

#BOTÃO CRIAR CONTA
btn_criarconta = Button(window, text = "Criar Conta", fg = "blue", font = ("Calibri", 12),width=15,height=1, command = nJanela)
btn_criarconta.place (x = 190, y = 140)


window.mainloop()
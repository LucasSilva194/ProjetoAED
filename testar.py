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
    utilizador = txt_utilizador_criar.get()
    password = txt_passe_criar.get()
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
w = 800
h = 300
ws = window.winfo_screenwidth()
hs = window.winfo_screenheight()
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
window.geometry('%dx%d+%d+%d' % (w, h, x, y))

#------------------EFETUAR LOGIN------------------#

#LABEL EFETUE LOGIN
lbl_efetue_login=Label(window, text = "Efetue o seu Login:", font=("Times New Roman",25))
lbl_efetue_login.place(x=480,y = 20)

#LABEL UTILIZADOR
lbl_utilizador=Label(window,text="Utilizador:",fg="black",font=("Times New Roman",14))
lbl_utilizador.place(x=460,y=110)

#ENTRY UTILIZADOR
txt_utilizador=Entry(window,width=20)
txt_utilizador.place(x=645,y=112)

#LABEL PALAVRA-PASSE
lbl_passe=Label(window,text="Palavra-Passe:",fg="black",font=("Times New Roman",14))
lbl_passe.place(x=460,y=140)

#ENTRY PALAVRA-PASSE
txt_passe=Entry(window,width=20,show="*")
txt_passe.place(x=645,y=143)

#BOTÃO PARA LOGIN
btn_login = Button(window, text = "Login", fg = "green", font = ("Calibri", 12),width=15,height=1, command = Login)
btn_login.place (x = 550, y = 220)

#------------------CRIAR UTILIZADOR------------------#

#LABEL EFETUE LOGIN
lbl_criar_login=Label(window, text = "Crie a sua conta:", font=("Times New Roman",25))
lbl_criar_login.place(x=100,y = 20)

#LABEL CRIAR UTILIZADOR
lbl_utilizador_criar=Label(window,text="Utilizador:",fg="black",font=("Times New Roman",14))
lbl_utilizador_criar.place(x=25,y=80)

#ENTRY CRIAR UTILIZADOR
txt_utilizador_criar=Entry(window, width=30)
txt_utilizador_criar.place(x=225,y=82)

#LABEL E-MAIL
lbl_email=Label(window,text="Email:",fg="black",font=("Times New Roman",14))
lbl_email.place(x=25,y=110)

#ENTRY E-MAIL
txt_email=Entry(window, width=30)
txt_email.place(x=225,y=113)

#LABEL CRIAR PALAVRA-PASSE
lbl_passe_criar=Label(window,text="Palavra-Passe:",fg="black",font=("Times New Roman",14))
lbl_passe_criar.place(x=25,y=140)

#ENTRY CRIAR PALAVRA-PASSE
txt_passe_criar=Entry(window, width=30,show="*")
txt_passe_criar.place(x=225,y=143)

#LABEL CONFIRMAR PALAVRA-PASSE
lbl_cpasse=Label(window,text="Confirmar Palavra-Passe:",fg="black",font=("Times New Roman",14))
lbl_cpasse.place(x=25,y=170)

#ENTRY CONFIRMAR PALAVRA-PASSE
txt_cpasse=Entry(window, width=30,show="*")
txt_cpasse.place(x=225,y=173)

#BOTÃO CRIAR CONTA
btn_criarconta = Button(window, text = "Criar Conta", fg = "blue", font = ("Calibri", 12),width=15,height=1, command = CriarConta)
btn_criarconta.place (x = 155, y = 220)

window.mainloop()
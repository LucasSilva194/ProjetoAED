from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
window = Tk()
window.title("Gestor de Roteiro de Viagens")

#CRIA UM FICHEIRO CHAMADO basedados.txt CASO O MESMO NÃO EXISTA
f = open("basedados.txt","a")
f.close()

#-----------------------FUNÇÃO DA JANELA PRINCIPAL-----------------------#
def mainWindow():

    #CENTRAR JANELA
    w = 500
    h = 200
    ws = window.winfo_screenwidth()
    hs = window.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    window.geometry('%dx%d+%d+%d' % (w, h, x, y))

    #INSERE A LABEL E ENTRY DO UTILIZADOR
    lbl_utilizador.place(x=120,y=20)
    txt_utilizador.place(x=230,y=22)

    #INSERE A LABEL E ENTRY DA PALAVRA PASSE
    lbl_passe.place(x=90,y=50)
    txt_passe.place(x=230,y=53)

    #INSERE OS BOTÕES DE LOGIN E DE CRIAR CONTA
    btn_login.place (x=190,y=100)
    btn_criarconta.place (x = 190, y = 140)

    #ESQUECE O POSICIONAMENTO DAS LABELS EMAIL, CPASSE E DO BOTÃO CRIAR CONTA (SEM A FUNÇÃO)
    lbl_email.place_forget()
    txt_email.place_forget()
    lbl_cpasse.place_forget() 
    txt_cpasse.place_forget()
    btn_criar.place_forget()

#-----------------------FUNÇÃO JANELA DE CRIAR CONTA-----------------------#
def nJanela():

    #ALTERAR AS DIMENSÕES DA JANELA PARA INSERIR NOVOS CAMPOS
    w = 450
    h = 230
    ws = window.winfo_screenwidth()
    hs = window.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    window.geometry('%dx%d+%d+%d' % (w, h, x, y))

    #PLACE DA ENTRY UTILIZADOR
    lbl_utilizador.place(x=30,y=20)
    txt_utilizador.place(x=230,y=22)

    #PLACE DA ENTRY EMAIL
    lbl_email.place(x=30,y=50)
    txt_email.place(x=230,y=53)

    #PLACE DA ENTRE PASSWORD
    lbl_passe.place(x=30,y=80)
    txt_passe.place(x=230,y=83)

    #PLACE DA ENTRY PARA CONFIRMAR PASSOWRD
    lbl_cpasse.place(x=30,y=110)
    txt_cpasse.place(x=230,y=113)

    #PLACE DO BOTÃO CRIAR 
    btn_criar.place(x=160,y=160)

    #APAGAR OS BOTÕES DE LOGIN E DE CRIAR CONTA
    btn_login.place_forget()
    btn_criarconta.place_forget()

#-----------------------FUNÇÃO JANELA-----------------------#
def JanelaApp():
    w = 1000
    h = 550
    ws = window.winfo_screenwidth()
    hs = window.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    window.geometry('%dx%d+%d+%d' % (w, h, x, y))

    #Limpar janela
    btn_login.place_forget()
    btn_criarconta.place_forget()
    lbl_utilizador.place_forget()
    txt_utilizador.place_forget()
    lbl_passe.place_forget()
    txt_passe.place_forget()
    user = txt_utilizador.get()

    lbl_user = Label(window, text= f"Utilizador: {user}",fg="black")
    lbl_user.place(x=10,y=10)

    btn_guias.place(x=30,y=100)
    btn_roadtrip.place(x=260,y=100)
    btn_trilhos.place(x=490,y=100)
    btn_praia.place(x=720,y=100)
#-----------------------FUNÇÃO LOGIN-----------------------#
def Login():

    #BUSCA O USUÁRIO E A PASSWORD INSERIDOS
    user = txt_utilizador.get()
    password = txt_passe.get()

    #GUARDA OS DADOS DE LOGIN NUMA STRING
    guardar = user + ";" + password

    #ABRE O FICHEIRO basedados.txt E ADICIONA OS DADOS PARA UMA STRING
    f = open("basedados.txt","r")
    lista = f.readlines()

    #CASO OS CAMPOS "UTILIZADOR" OU "PALAVRA-PASSE" ESTEJAM VAZIOS, RETORNA UM ERRO
    if user == "" or password == "":
        messagebox.showerror("Erro","Por favor forneça os seus dados de Acesso")
    
    #CASO OS DADOS DE ACESSO ESTEJAM CORRETOS, EFETUA LOGIN
    else:
        if str(guardar) in str(lista):
           messagebox.showinfo("Bem vindo",f"Olá {user}, o seu login foi efetuado com sucesso")
           JanelaApp()
        
        #SE OS DADOS ESTIVEREM ERRADOS, RETORNA UM ERRO
        else:
            messagebox.showerror("Tentativa de Login sem sucesso","Utilizador ou palavra-passe incorreta. Por favor tente novamente ou crie conta.")
            txt_passe.delete(0,"end")              


#-----------------------FUNÇÃO CRIAR CONTA-----------------------#
def CriarConta():

    #BUSCA OS DADOS DE ACESSO (UTILIZADOR, PASSWORD E EMAIL)
    utilizador = txt_utilizador.get()
    password = txt_passe.get()
    email = txt_email.get()
    cpassword = txt_cpasse.get()

    #GUARDA OS DADOS DE ACESSO INSERIDOS PARA UMA STRING
    guardar = utilizador + ";" + password + ";" + email

    #ABRE O FICHEIRO basedados.txt PARA LEITURA
    f = open("basedados.txt","r")

    #CASO ALGUM DOS CAMPOS ESTEJA VAZIO, RETORNA UM ERRO
    if utilizador == "" or email == "" or password == "" or cpassword == "":
        messagebox.showerror("Erro","Por favor forneça todos os dados corretamente.")

    #SE OS CAMPOS UTILIZADOR E PALAVRA-PASSE ESTIVEREM PREENCHIDOS, ADICIONA OS DADOS DO FICHEIRO basedados.txt PARA UMA STRING
    if utilizador != "" and password != "":
        lista = f.readlines()

        #VERIFICA SE OS DADOS JÁ SE ENCONTRAM NO FICHEIRO
        if str(guardar) in str(lista):
            messagebox.showerror("Erro","Já existe uma conta com esses dados, por favor efetue login")

        #VERIFICA SE O NOME DE UTILIZADOR JÁ ESTÁ EM USO 
        elif str(utilizador) in str(lista):
            messagebox.showerror("Erro","Esse utilizador já existe")

        #SE A PALAVRA-PASSE FOR CONFIRMADA CORRETAMENTE CRIA A CONTA  
        else:
            if password == cpassword:
                f = open("basedados.txt","a")
                f.write(utilizador + ";" + password + ";" + email + ";" + "user""\n")
                messagebox.showinfo("Sucesso","A sua conta foi criada com sucesso!")

                mainWindow()
            else:
                messagebox.showerror("Erro","As duas passwords não coincidem")


#-----------------------CRIAÇÃO DE LABELS E ENTRIES-----------------------#

#LABEL UTILIZADOR
lbl_utilizador=Label(window,text="Utilizador:",fg="black",font=("Times New Roman",14))

#ENTRY UTILIZADOR
txt_utilizador=Entry(window,width=30)

#LABEL E-MAIL
lbl_email=Label(window,text="Email:",fg="black",font=("Times New Roman",14))

#ENTRY E-MAIL
txt_email=Entry(window, width=30)

#LABEL PALAVRA-PASSE
lbl_passe=Label(window,text="Palavra-Passe:",fg="black",font=("Times New Roman",14))

#ENTRY PALAVRA-PASSE
txt_passe=Entry(window,width=30,show="*")

#LABEL CONFIRMAR PALAVRA-PASSE
lbl_cpasse=Label(window,text="Confirmar Palavra-Passe:",fg="black",font=("Times New Roman",14))

#ENTRY CONFIRMAR PALAVRA-PASSE
txt_cpasse=Entry(window, width=30,show="*")


#-----------------------CRIAÇÃO DE BOTÕES-----------------------#

#BOTÃO PARA LOGIN
btn_login = Button(window, text = "Login", fg = "green", font = ("Calibri", 12),width=15,height=1, command = Login)

#BOTÃO CRIAR CONTA
btn_criarconta = Button(window, text = "Criar Conta", fg = "blue", font = ("Calibri", 12),width=15,height=1, command = nJanela)

#BOTÃO DE CRIAR CONTA QUE EXECUTA A FUNÇÃO
btn_criar = Button(window,text="Criar Conta", fg="blue", font = ("Calibri",12), width=15,height=1, command=CriarConta)

#BOTÃO GUIAS E ROTEIROS
foto_guias = ImageTk.PhotoImage(Image.open("guias.png"))
btn_guias = Button(window, text = "", fg="black", width = 220, height = 395,image = foto_guias)

#BOTÃO ROADTRIPS
foto_roadtrips=ImageTk.PhotoImage(Image.open("roadtrips.png"))
btn_roadtrip=Button(window, text = "", width = 220, height = 395,image = foto_roadtrips)

#BOTÃO TRILHOS E OUTDOORS
foto_trilhos=ImageTk.PhotoImage(Image.open("trilhos.png"))
btn_trilhos=Button(window, text = "",width = 220, height = 395,image = foto_trilhos)

#BOTÃO PRAIA
foto_praia=ImageTk.PhotoImage(Image.open("praias.png"))
btn_praia=Button(window,text="",width = 220, height = 395,image = foto_praia)

mainWindow()
window.mainloop()
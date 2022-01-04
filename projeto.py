from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

window = Tk()
window.title("Gestor de Roteiro de Viagens")

#CRIA UM FICHEIRO CHAMADO basedados.txt CASO O MESMO NÃO EXISTA
f = open("basedados.txt","a")
f.close()

#-----------------------------FUNÇÃO DA INICIAL---------------------------#
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

    #ESQUECE O POSICIONAMENTO DAS LABELS NÃO NECESSÁRIAS
    lbl_email.place_forget()
    txt_email.place_forget()
    lbl_cpasse.place_forget() 
    txt_cpasse.place_forget()
    btn_criar.place_forget()
    btn_retornar.place_forget()

#-----------------------FUNÇÃO JANELA DE CRIAR CONTA----------------------#
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
    btn_criar.place(x=240,y=160)
    btn_retornar.place(x=70, y=160)

    #APAGAR OS BOTÕES DE LOGIN E DE CRIAR CONTA
    btn_login.place_forget()
    btn_criarconta.place_forget()

#------------------------------FUNÇÃO JANELA------------------------------#
def JanelaApp():

    #REDIMENSIONAR A JANELA
    w = 980
    h = 550
    ws = window.winfo_screenwidth()
    hs = window.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    window.geometry('%dx%d+%d+%d' % (w, h, x, y))
    window.configure(bg ="white")

    #ESQUECE OS BOTÕES NÃO NECESSÁRIOS
    btn_login.place_forget()
    btn_criarconta.place_forget()
    btn_retornar_menu.place_forget()

    #ESQUECE OS BOTÕES DAS PRAIAS
    btn_kaanapali.place_forget()
    btn_anse.place_forget()
    btn_navagio.place_forget()
    btn_zlatni.place_forget()

    #ESQUECE AS LABELS NÃO NECESSÁRIAS
    lbl_passe.place_forget()
    lbl_utilizador.place_forget()

    #ESQUECE AS ENTRIES NÃO NECESSÁRIAS
    txt_utilizador.place_forget()
    txt_passe.place_forget()

    #INSERE O NOME DE UTILIZADOR QUE ESTÁ AUTENTICADO
    user = txt_utilizador.get()
    lbl_user = Label(window, text= f"Utilizador: {user}",fg="black",font = ("Calibri", 10),width=20,height=1,bg = "white")
    lbl_user.place(x=10,y=20)

    #INSERE O TITULO DA PÁGINA
    lbl_menu.place(x=230, y=20)

    #BOTÃO PARA FECHAR TUDO
    btn_sair.place(x=856, y=10)

    #INSERE OS BOTÕES DE GUIAS, MONTANHAS, CIDADES E PRAIAS
    btn_guias.place(x=30,y=100)
    btn_montanhas.place(x=260,y=100)
    btn_cidades.place(x=490,y=100)
    btn_praia.place(x=720,y=100)

#-------------------------FUNÇÃO GUIAS E ROTEIROS-------------------------#
def guias_roteiros():

    #REDIMENSIONAR A JANELA
    w = 500
    h = 500
    ws = window.winfo_screenwidth()
    hs = window.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    window.geometry('%dx%d+%d+%d' % (w, h, x, y))
    
    #ESQUECE OS BOTÕES NÃO NECESSÁRIOS
    btn_guias.place_forget()
    btn_montanhas.place_forget()
    btn_cidades.place_forget()
    btn_praia.place_forget()
    btn_retornar.place_forget()
    btn_sair.place_forget()

    #ESQUECE A LABEL DO MENU
    lbl_menu.place_forget()

    #INSERE O BOTÃO PARA RETORNAR AO MENU PRINCIPAL
    btn_retornar_menu.place(x=380,y=10)

#----------------------------FUNÇÃO ROADTRIPS-----------------------------#
def montanhas():

    #REDIMENSIONAR A JANELA
    w = 500
    h = 500
    ws = window.winfo_screenwidth()
    hs = window.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    window.geometry('%dx%d+%d+%d' % (w, h, x, y))
    
    #ESQUECE OS BOTÕES NÃO NECESSÁRIOS
    btn_guias.place_forget()
    btn_montanhas.place_forget()
    btn_cidades.place_forget()
    btn_praia.place_forget()
    btn_sair.place_forget()

    #ESQUECE A LABEL DO MENU PRINCIPAL
    lbl_menu.place_forget()

    #INSERE O BOTÃO PARA RETORNAR AO MENU
    btn_retornar_menu.place(x=380,y=10)

#-----------------------------FUNÇÃO CIDADES------------------------------#
def cidades():

    #REDIMENSIONA A JANELA
    w = 500
    h = 500
    ws = window.winfo_screenwidth()
    hs = window.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    window.geometry('%dx%d+%d+%d' % (w, h, x, y))
    
    #ESQUECE OS BOTÕES NÃO NECESSÁRIOS
    btn_guias.place_forget()
    btn_montanhas.place_forget()
    btn_cidades.place_forget()
    btn_praia.place_forget()
    btn_sair.place_forget()

    #ESQUECE A LABEL DO MENU PRINCIPAL
    lbl_menu.place_forget()

    #INSERE O BOTÃO PARA RETORNAR AO MENU PRINCIPAL
    btn_retornar_menu.place(x=380,y=10)

#-----------------------------FUNÇÃO PRAIAS-------------------------------#
def praias():

    #REDIMENSIONAR A JANELA
    w = 885
    h = 500
    ws = window.winfo_screenwidth()
    hs = window.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    window.geometry('%dx%d+%d+%d' % (w, h, x, y))
    window.configure(bg ="lightblue")

    #ESQUECE OS BOTÕES NÃO NECESSÁRIOS
    btn_guias.place_forget()
    btn_montanhas.place_forget()
    btn_cidades.place_forget()
    btn_praia.place_forget()
    btn_sair.place_forget()

    #ESQUECE A LABEL DO MENU PRINCIPAL
    lbl_menu.place_forget()

    #INSERE O BOTÃO PARA RETORNAR AO MENU PRINCIPAL
    btn_retornar_menu.place(x=740,y=10)

    #BOTÃO DA PRAIA ANSE
    btn_anse.place(x=55,y=60)

    #BOTÃO PRAIA NAVAGIO
    btn_navagio.place(x=55, y=280)

    #BOTÃO PRAIA ZLATNI
    btn_zlatni.place(x=450,y=60)

    #BOTÃO PRAIA KAANAPALI
    btn_kaanapali.place(x=450, y=280)

#-----------------------------FUNÇÃO LOGIN--------------------------------#
def Login():

    #BUSCA O USUÁRIO E A PASSWORD INSERIDOS
    user = txt_utilizador.get()
    password = txt_passe.get()

    #GUARDA OS DADOS DE LOGIN NUMA STRING
    guardar = user + ";" + password + ";" + "user"
    guardaradmin = user + ";" + password + ";" + "admin"

    #ABRE O FICHEIRO basedados.txt E ADICIONA OS DADOS PARA UMA STRING
    f = open("basedados.txt","r")
    lista = f.readlines()

    #CASO OS CAMPOS "UTILIZADOR" OU "PALAVRA-PASSE" ESTEJAM VAZIOS, RETORNA UM ERRO
    if user == "" or password == "":
        messagebox.showerror("Erro","Por favor forneça os seus dados de acesso.")
    
    #CASO OS DADOS DE ACESSO ESTEJAM CORRETOS, EFETUA LOGIN
    else:
        if str(guardaradmin) in str(lista):
           messagebox.showinfo("Bem vindo ADMIN",f"Olá {user}, o seu login foi efetuado com sucesso!")
           JanelaApp()

        elif str(guardar) in str(lista):
            messagebox.showinfo("Bem vindo",f"Olá {user}, o seu login foi efetuado com sucesso!")
            JanelaApp()
        
        #SE OS DADOS ESTIVEREM ERRADOS, RETORNA UM ERRO
        else:
            messagebox.showerror("Tentativa de Login sem sucesso","Utilizador ou palavra-passe incorreta. Por favor tente novamente ou crie conta.")
            txt_passe.delete(0,"end")              

#--------------------------FUNÇÃO CRIAR CONTA-----------------------------#
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
            messagebox.showerror("Erro","Já existe uma conta com esses dados, por favor efetue login.")

        #VERIFICA SE O NOME DE UTILIZADOR JÁ ESTÁ EM USO 
        elif str(utilizador) in str(lista):
            messagebox.showerror("Erro","Esse utilizador já existe.")

        #SE A PALAVRA-PASSE FOR CONFIRMADA CORRETAMENTE CRIA A CONTA  
        else:
            if password == cpassword:
                f = open("basedados.txt","a")
                f.write(utilizador + ";" + password + ";" + "user" + ";" + email + "\n")
                messagebox.showinfo("Sucesso","A sua conta foi criada com sucesso!")

                mainWindow()
            else:
                messagebox.showerror("Erro","As duas passwords não coincidem.")

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

#LABEL MENU PRINCIPAL
lbl_menu = Label(window, text="MENU PRINCIPAL",fg = "black", bg="white", font=("Calibri 25 bold"), width = 30, height = 1)


#-----------------------------CRIAÇÃO DE BOTÕES--------------------------#

#BOTÃO PARA LOGIN
btn_login = Button(window, text = "Login", fg = "white", bg="green", font = ("Calibri 12 bold"),width=15,height=1, command = Login)

#BOTÃO CRIAR CONTA
btn_criarconta = Button(window, text = "Criar Conta", fg = "white",bg="blue", font = ("Calibri 12 bold"),width=15,height=1, command = nJanela)

#BOTÃO DE CRIAR CONTA QUE EXECUTA A FUNÇÃO
btn_criar = Button(window,text="Criar Conta", fg="white",bg="green", font = ("Calibri 12 bold"), width=15,height=1, command=CriarConta)

#BOTÃO RETORNAR
btn_retornar = Button(window,text="<-- Retornar", fg="white",bg="red", font = ("Calibri 12 bold"), width=15,height=1, command=mainWindow)

#BOTÃO GUIAS E ROTEIROS
foto_guias = ImageTk.PhotoImage(Image.open("guias.png"))
btn_guias = Button(window, text = "", fg="black", width = 220, height = 395,image = foto_guias, command = guias_roteiros)

#BOTÃO ROADTRIPS
foto_roadtrips=ImageTk.PhotoImage(Image.open("roadtrips.png"))
btn_roadtrip=Button(window, text = "", width = 220, height = 395,image = foto_roadtrips)

#BOTÃO TRILHOS E OUTDOORS
foto_trilhos=ImageTk.PhotoImage(Image.open("trilhos.png"))
btn_trilhos=Button(window, text = "",width = 220, height = 395,image = foto_trilhos)

#BOTÃO SAIR
btn_sair = Button(window, text = "SAIR", fg = "red", font = ("Calibri", 12),width=10,height=1, command = window.quit)

#### BOTÕES PRAIAS ####

#PRINCIPAL
foto_praia=ImageTk.PhotoImage(Image.open("praias.png"))
btn_praia=Button(window,text="",width = 220, height = 395,image = foto_praia, command = praias)

#NAVAGIO
foto_navagio = ImageTk.PhotoImage(Image.open("navagio.png"))
btn_navagio = Button(window,text="",width = 375, height = 200,image = foto_navagio)

#ANSE
foto_anse = ImageTk.PhotoImage(Image.open("anse.png"))
btn_anse = Button(window,text="",width = 375, height = 200,image = foto_anse)

#ZLATNI
foto_zlatni = ImageTk.PhotoImage(Image.open("zlatni.png"))
btn_zlatni = Button(window,text="",width = 375, height = 200,image = foto_zlatni)

#KAANAPALI
foto_kaanapali = ImageTk.PhotoImage(Image.open("Kaanapali.png"))
btn_kaanapali = Button(window,text="",width = 375, height = 200,image = foto_kaanapali)

#### BOTÕES CIDADES ####
foto_cidades=ImageTk.PhotoImage(Image.open("cidades.png"))
btn_cidades=Button(window,text="",width = 220, height = 395,image = foto_cidades,command = cidades)


#BOTÃO MONTANHAS
foto_montanhas=ImageTk.PhotoImage(Image.open("montanhas.png"))
btn_montanhas=Button(window,text="",width = 220, height = 395,image = foto_montanhas, command = montanhas)

#BOTÃO RETORNAR MENU
btn_retornar_menu = Button(window, text="Menu", fg="black",font = ("Calibri 12 bold"), width=10,height=1, command=JanelaApp)


mainWindow()
window.mainloop()
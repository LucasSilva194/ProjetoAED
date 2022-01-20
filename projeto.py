from cgitb import text
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

window = Tk()
window.title("Gestor de Roteiro de Viagens")

#CRIAÇÃO DE FICHEIROS 
f = open("basedados.txt","a")
f.close()

f = open("comentarios.txt","a")
f.close()

f = open("classificacoes.txt","a")
f.close()

def dev():
    messagebox.showinfo("ACESSO RESTRITO","Esta página ainda se encontra em desenvolvimento. Pedimos desculpa pelo incómodo causado.")

#region LOGIN E CRIAÇÃO DE CONTA

#-------------------------FUNÇÃO DA JANELA INICIAL-------------------------#
def JanelaLogin():

    #CENTRAR JANELA
    w = 500
    h = 200
    ws = window.winfo_screenwidth()
    hs = window.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    window.geometry('%dx%d+%d+%d' % (w, h, x, y))
    window.configure(bg ="#F0F0F0")

    #INSERE A LABEL E ENTRY DO UTILIZADOR
    lbl_utilizador.place(x=120,y=20)
    txt_utilizador.place(x=230,y=22)

    #INSERE A LABEL E ENTRY DA PALAVRA PASSE
    lbl_passe.place(x=90,y=50)
    txt_passe.place(x=230,y=53)

    #INSERE OS BOTÕES DE LOGIN E DE CRIAR CONTA
    btn_login.place (x=190,y=100)
    btn_criarconta.place (x = 190, y = 140)

    #REMOVE ENTRIES E LABELS NÃO NECESSÁRIAS
    lbl_email.place_forget()
    txt_email.place_forget()
    lbl_cpasse.place_forget() 
    txt_cpasse.place_forget()
    btn_criar.place_forget()
    btn_retornar.place_forget()

    #REMOVE NÃO NECESSÁRIOS LOGOUT
    btn_guias.place_forget()
    btn_montanhas.place_forget()
    btn_cidades.place_forget()
    btn_praia.place_forget()
    btn_sair.place_forget()
    lbl_menu.place_forget()

#-----------------------FUNÇÃO JANELA DE CRIAR CONTA----------------------#
def JanelaCriar():

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

#-----------------------------FUNÇÃO LOGIN--------------------------------#
def Login():

    #BUSCA O USUÁRIO E A PASSWORD INSERIDOS
    user = txt_utilizador.get()
    password = txt_passe.get()

    #GUARDA OS DADOS DE LOGIN NUMA STRING
    guardar = user + ";" + password + ";" + "user"
    guardaradmin = user + ";" + password + ";" + "admin"

    #ABRE O FICHEIRO basedados.txt E PARA LEITURA
    f = open("basedados.txt","r")
    lista = f.readlines()

    #CASO OS CAMPOS "UTILIZADOR" OU "PALAVRA-PASSE" ESTEJAM VAZIOS, RETORNA UM ERRO
    if user == "" or password == "":
        messagebox.showerror("Erro","Por favor forneça os seus dados de acesso.")
    
    #CASO OS DADOS DE ACESSO ESTEJAM CORRETOS, EFETUA LOGIN
    else:
        if str(guardaradmin) in str(lista):
           messagebox.showinfo("Bem vindo ADMINISTRADOR",f"Olá {user}! Está autenticado como ADMIN")
           txt_passe.delete(0,"end")
           JanelaAppAdmin()

        elif str(guardar) in str(lista):
            messagebox.showinfo("Bem vindo",f"Olá {user}, o seu login foi efetuado com sucesso!")
            txt_passe.delete(0,"end")
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
                JanelaLogin()
            else:
                messagebox.showerror("Erro","As duas passwords não coincidem.")

def JanelaCriarAdmin():
    JanCriarAdmin = Toplevel(window)
    JanCriarAdmin.title("Adicionar Utilizadores Utilizador")

    w = 450
    h = 230
    ws = JanCriarAdmin.winfo_screenwidth()
    hs = JanCriarAdmin.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    JanCriarAdmin.geometry('%dx%d+%d+%d' % (w, h, x, y))

    #UTILIZADOR
    lbl_utilizador=Label(JanCriarAdmin,text="Utilizador:",fg="black",font=("Times New Roman",14))
    txt_utilizador=Entry(JanCriarAdmin,width=30)
    lbl_utilizador.place(x=30,y=20)
    txt_utilizador.place(x=230,y=22)

    #EMAIL
    lbl_email=Label(JanCriarAdmin,text="Email:",fg="black",font=("Times New Roman",14))
    txt_email=Entry(JanCriarAdmin, width=30)
    lbl_email.place(x=30,y=50)
    txt_email.place(x=230,y=53)

    #PASSWORD
    lbl_passe=Label(JanCriarAdmin,text="Palavra-Passe:",fg="black",font=("Times New Roman",14))
    txt_passe=Entry(JanCriarAdmin,width=30,show="*")
    lbl_passe.place(x=30,y=80)
    txt_passe.place(x=230,y=83)

    #CONFIRMAR PASSOWRD
    lbl_cpasse=Label(JanCriarAdmin,text="Confirmar Palavra-Passe:",fg="black",font=("Times New Roman",14))
    txt_cpasse=Entry(JanCriarAdmin, width=30,show="*")
    lbl_cpasse.place(x=30,y=110)
    txt_cpasse.place(x=230,y=113)

    #CHECKBUTTON USER OU ADMIN
    cb1 = IntVar()
    cb1.set(1)
    cb2 = IntVar()

    cb1_utilizador = Checkbutton(JanCriarAdmin, text="Utilizador", variable = cb1)
    cb2_utilizador = Checkbutton(JanCriarAdmin,text="Administrador",variable=cb2)
        
    cb1_utilizador.place(x=70, y=150)
    cb2_utilizador.place(x=70, y=180)

    def CriarContaAdmin():
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
            JanCriarAdmin.attributes("-topmost",True)

        #SE OS CAMPOS UTILIZADOR E PALAVRA-PASSE ESTIVEREM PREENCHIDOS, ADICIONA OS DADOS DO FICHEIRO basedados.txt PARA UMA STRING
        if utilizador != "" and password != "":
            lista = f.readlines()

            #VERIFICA SE OS DADOS JÁ SE ENCONTRAM NO FICHEIRO
            if str(guardar) in str(lista):
                messagebox.showerror("Erro","Já existe uma conta com esses dados, por favor efetue login.")
                JanCriarAdmin.attributes("-topmost",True)

            #VERIFICA SE O NOME DE UTILIZADOR JÁ ESTÁ EM USO 
            elif str(utilizador) in str(lista):
                messagebox.showerror("Erro","Esse utilizador já existe.")
                JanCriarAdmin.attributes("-topmost",True)

            #SE A PALAVRA-PASSE FOR CONFIRMADA CORRETAMENTE CRIA A CONTA  
            else:
                if password == cpassword:
                    if cb1.get() == 1 and cb2.get() == 0:
                        f = open("basedados.txt","a")
                        f.write(utilizador + ";" + password + ";" + "user" + ";" + email + "\n")
                        messagebox.showinfo("Sucesso","A sua conta de UTILIZADOR foi criada com sucesso!")
                        JanelaAppAdmin()
                        JanCriarAdmin.quit()
                    elif cb2.get() == 1 and cb1.get() == 0:
                        f = open("basedados.txt","a")
                        f.write(utilizador + ";" + password + ";" + "admin" + ";" + email + "\n")
                        messagebox.showinfo("Sucesso","A sua conta de ADMINISTRADOR foi criada com sucesso!")
                        JanelaAppAdmin()
                        JanCriarAdmin.quit()
                    elif cb1.get() == 1 and cb2.get() == 1:
                        messagebox.showerror("Erro","Por favor selecione apenas uma das opções: UTILIZADOR ou ADMINISTRADOR.")
                        
                else:
                    messagebox.showerror("Erro","As duas passwords não coincidem.")
                    JanCriarAdmin.attributes("-topmost",True)

    #BOTÃO CRIAR
    btn_criar = Button(JanCriarAdmin,text="Criar Conta", fg="white",bg="lightgreen", font = ("Calibri 12 bold"), width=15,height=1, command=CriarContaAdmin)
    btn_criar.place(x=240,y=160)


#BOTÃO PARA LOGIN E CRIAR CONTA
btn_login = Button(window, text = "Login", fg = "white", bg="limegreen", font = ("Calibri 12 bold"),width=15,height=1, command = Login)
btn_criarconta = Button(window, text = "Criar Conta", fg = "white",bg="royalblue1", font = ("Calibri 12 bold"),width=15,height=1, command = JanelaCriar)
btn_criar = Button(window,text="Criar Conta", fg="white",bg="lightgreen", font = ("Calibri 12 bold"), width=15,height=1, command=CriarConta)

#UTILIZADOR
lbl_utilizador=Label(window,text="Utilizador:",fg="black",font=("Times New Roman",14))
txt_utilizador=Entry(window,width=30)

#E-MAIL
lbl_email=Label(window,text="Email:",fg="black",font=("Times New Roman",14))
txt_email=Entry(window, width=30)

#PALAVRA-PASSE
lbl_passe=Label(window,text="Palavra-Passe:",fg="black",font=("Times New Roman",14))
txt_passe=Entry(window,width=30,show="*")

#CONFIRMAR PALAVRA-PASSE
lbl_cpasse=Label(window,text="Confirmar Palavra-Passe:",fg="black",font=("Times New Roman",14))
txt_cpasse=Entry(window, width=30,show="*")

#BOTÃO RETORNAR
btn_retornar = Button(window,text="<-- Retornar", fg="white",bg="red", font = ("Calibri 12 bold"), width=15,height=1, command=JanelaLogin)

#endregion

#region JANELA DA APP
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

    #REMOVE OS BOTÕES NÃO NECESSÁRIOS DE INICIO DE SESSÃO
    btn_login.place_forget()
    btn_criarconta.place_forget()
    btn_retornar_menu.place_forget()

    #REMOVE OS BOTÕES DAS PRAIAS
    btn_kaanapali.place_forget()
    btn_anse.place_forget()
    btn_navagio.place_forget()
    btn_zlatni.place_forget()

    #REMOVE BOTÕES DAS MONTANHAS
    btn_kilimanjaro.place_forget()
    btn_kirkjufell.place_forget()
    btn_matterhorn.place_forget()
    btn_estrela.place_forget()

    #REMOVE AS LABELS E ENTRIES NÃO NECESSÁRIAS
    lbl_passe.place_forget()
    lbl_utilizador.place_forget()
    lbl_praias.place_forget()
    txt_utilizador.place_forget()
    txt_passe.place_forget()

    #INSERE O NOME DE UTILIZADOR QUE ESTÁ AUTENTICADO
    user = txt_utilizador.get()
    lbl_user = Label(window, text= f"Utilizador: {user}",fg="black",font = ("Calibri", 10),width=20,height=1,bg = "white")
    lbl_user.place(x=10,y=20)

    #INSERE O TITULO DA PÁGINA
    lbl_menu.place(x=490, y=60,anchor=CENTER)

    #BOTÃO PARA FECHAR TUDO
    btn_sair.place(x=856, y=10)

    #INSERE OS BOTÕES DE GUIAS, MONTANHAS, CIDADES E PRAIAS
    btn_guias.place(x=30,y=100)
    btn_montanhas.place(x=260,y=100)
    btn_cidades.place(x=490,y=100)
    btn_praia.place(x=720,y=100)

#LABEL MENU PRINCIPAL
lbl_menu = Label(window, text="MENU PRINCIPAL",fg = "black", bg="white", font=("Calibri 25 bold"), width = 30, height = 1)

#BOTÃO SAIR
btn_sair = Button(window, text = "SAIR", fg = "red", font = ("Calibri", 12),width=10,height=1, command = window.quit)

#BOTÃO RETORNAR MENU
btn_retornar_menu = Button(window, text="Menu", fg="black",font = ("Calibri 12 bold"), width=10,height=1, command=JanelaApp)

#endregion

#region JANELA DA APP ADMIN
def JanelaAppAdmin():

    #REMOVE OS BOTÕES NÃO NECESSÁRIOS DE INICIO DE SESSÃO
    btn_login.place_forget()
    btn_criarconta.place_forget()
    btn_retornar_menu.place_forget()

    #REMOVE OS BOTÕES DAS PRAIAS
    btn_kaanapali.place_forget()
    btn_anse.place_forget()
    btn_navagio.place_forget()
    btn_zlatni.place_forget()

    #REMOVE BOTÕES DAS MONTANHAS
    btn_kilimanjaro.place_forget()
    btn_kirkjufell.place_forget()
    btn_matterhorn.place_forget()
    btn_estrela.place_forget()

    #REMOVE AS LABELS E ENTRIES NÃO NECESSÁRIAS
    lbl_passe.place_forget()
    lbl_utilizador.place_forget()
    lbl_praias.place_forget()
    txt_utilizador.place_forget()
    txt_passe.place_forget()

    #INSERE O NOME DE UTILIZADOR QUE ESTÁ AUTENTICADO
    user = txt_utilizador.get()
    lbl_user = Label(window, text= f"Utilizador: {user}",fg="black",font = ("Calibri", 10),width=20,height=1,bg = "white")
    lbl_user.place(x=10,y=20)

    #INSERE O TITULO DA PÁGINA
    lbl_menu.place(x=490, y=60,anchor=CENTER)

    #BOTÃO PARA FECHAR TUDO
    btn_sair.place(x=856, y=10)

    #INSERE OS BOTÕES DE GUIAS, MONTANHAS, CIDADES E PRAIAS
    btn_guias.place(x=30,y=100)
    btn_montanhas.place(x=260,y=100)
    btn_cidades.place(x=490,y=100)
    btn_praia.place(x=720,y=100)

    #BARRA MENU ADMIN
    barra_admin = Menu(window)

    utilizadores_Menu = Menu(barra_admin)
    utilizadores_Menu.add_command(label="Adicionar Utilizadores", command=JanelaCriarAdmin)
    utilizadores_Menu.add_command(label="Remover Utilizadores", command=dev)
    barra_admin.add_cascade(label="Utilizadores", menu=utilizadores_Menu)

    categorias_menu = Menu(barra_admin)
    categorias_menu.add_command(label = "Alterar Categorias",command=dev)
    barra_admin.add_cascade(label = "Categorias", menu=categorias_menu)

    ordenar_menu = Menu(barra_admin)
    ordenar_menu.add_command(label="Mais Popular", command = dev)
    ordenar_menu.add_command(label="Mais Comentada", command = dev)
    barra_admin.add_cascade(label="Ordenar", menu=ordenar_menu)

    #REDIMENSIONAR A JANELA
    w = 980
    h = 550
    ws = window.winfo_screenwidth()
    hs = window.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    window.geometry('%dx%d+%d+%d' % (w, h, x, y))
    window.configure(bg ="white", menu=barra_admin)

#LABEL MENU PRINCIPAL
lbl_menu = Label(window, text="MENU PRINCIPAL",fg = "black", bg="white", font=("Calibri 25 bold"), width = 30, height = 1)

#BOTÃO SAIR
btn_sair = Button(window, text = "SAIR", fg = "red", font = ("Calibri", 12),width=10,height=1, command = window.quit)

#BOTÃO RETORNAR MENU
btn_retornar_menu = Button(window, text="Menu", fg="black",font = ("Calibri 12 bold"), width=10,height=1, command=JanelaApp)

#endregion

#region GUIAS E ROTEIROS

def guias_roteiros():

    #REDIMENSIONAR A JANELA
    w = 500
    h = 500
    ws = window.winfo_screenwidth()
    hs = window.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    window.geometry('%dx%d+%d+%d' % (w, h, x, y))
    
    #REMOVE OS BOTÕES NÃO NECESSÁRIOS
    btn_guias.place_forget()
    btn_montanhas.place_forget()
    btn_cidades.place_forget()
    btn_praia.place_forget()
    btn_retornar.place_forget()
    btn_sair.place_forget()

    #REMOVE A LABEL DO MENU
    lbl_menu.place_forget()

    #REMOVE O BOTÃO PARA RETORNAR AO MENU PRINCIPAL
    btn_retornar_menu.place(x=380,y=10)

#BOTÃO GUIAS E ROTEIROS
foto_guias = ImageTk.PhotoImage(Image.open("guias.png"))
btn_guias = Button(window, text = "", fg="black", width = 220, height = 395,image = foto_guias, command = dev)

#endregion

#region MONTANHAS
def montanhas():

    #REDIMENSIONAR A JANELA
    w = 885
    h = 560
    ws = window.winfo_screenwidth()
    hs = window.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    window.geometry('%dx%d+%d+%d' % (w, h, x, y))

    window.configure(bg ="#aba8e2")
    
    #REMOVE OS BOTÕES NÃO NECESSÁRIOS
    btn_guias.place_forget()
    btn_montanhas.place_forget()
    btn_cidades.place_forget()
    btn_praia.place_forget()
    btn_sair.place_forget()

    #REMOVE A LABEL DO MENU PRINCIPAL
    lbl_menu.place_forget()

    #INSERE O BOTÃO PARA RETORNAR AO MENU
    btn_retornar_montanhas.place_forget()
    btn_retornar_menu.place(x=740,y=17)

    #INSERE O NOME DE UTILIZADOR QUE ESTÁ AUTENTICADO
    user = txt_utilizador.get()
    lbl_user = Label(window, text= f"Utilizador: {user}",fg="black",font = ("Calibri bold", 10),width=20,height=1,bg = "#aba8e2")
    lbl_user.place(x=10,y=20)
    
    #BOTÃO KILIMANJARO
    btn_kilimanjaro.place(x=55,y=90)
    
    #REMOVE A IMAGEM E A DESCRIÇÃO DA KILIMANJARO
    desc_kilimanjaro.place_forget()
    lbl_kilimanjaro.place_forget()

    #BOTÃO KIRKJUFELL
    btn_kirkjufell.place(x=55, y=310)

    #REMOVE A IMAGEM E A DESCRIÇÃO DA KIRKJUFELL
    desc_kirkjufell.place_forget()
    lbl_kirkjufell.place_forget()

    #BOTÃO MATTERHORN
    btn_matterhorn.place(x=450,y=90)

    #BOTÃO SERRA DA ESTRELA
    btn_estrela.place(x=450, y=310)

def kilimanjaro():

    #REDIMENSIONAR A JANELA
    w = 885
    h = 560
    ws = window.winfo_screenwidth()
    hs = window.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    window.geometry('%dx%d+%d+%d' % (w, h, x, y))


    #REMOVE OS BOTÕES DAS MONTANHAS
    btn_kilimanjaro.place_forget()
    btn_matterhorn.place_forget()
    btn_kirkjufell.place_forget()
    btn_estrela.place_forget()

    #TROCA O BOTÃO MENU POR BOTÃO RETORNAR
    btn_retornar_menu.place_forget()
    btn_retornar_montanhas.place(x=740,y=17)

    #INSERE A IMAGEM
    lbl_kilimanjaro.place(x=445, y=200, anchor = CENTER)

    #DESCRIÇÃO DA MONTANHA
    desc_kilimanjaro.place(x=445,y=400, anchor=CENTER)

def kirkjufell():

    #REDIMENSIONAR A JANELA
    w = 885
    h = 560
    ws = window.winfo_screenwidth()
    hs = window.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    window.geometry('%dx%d+%d+%d' % (w, h, x, y))

    #REMOVE OS BOTÕES DAS MONTANHAS
    btn_kilimanjaro.place_forget()
    btn_matterhorn.place_forget()
    btn_kirkjufell.place_forget()
    btn_estrela.place_forget()

    #TROCA O BOTÃO MENU POR BOTÃO RETORNAR
    btn_retornar_menu.place_forget()
    btn_retornar_montanhas.place(x=740,y=17)

    #INSERE A IMAGEM
    lbl_kirkjufell.place(x=445, y=200, anchor = CENTER)

    #DESCRIÇÃO DA MONTANHA
    desc_kirkjufell.place(x=445,y=400, anchor=CENTER)

#BOTÃO MONTANHAS
foto_montanhas=ImageTk.PhotoImage(Image.open("montanhas.png"))
btn_montanhas=Button(window,text="",width = 220, height = 395,image = foto_montanhas, command = montanhas)

#BOTÃO RETORNAR MONTANHAS
btn_retornar_montanhas = Button(window, text="Retornar", fg="black",font = ("Calibri 12 bold"), width=10,height=1, command=montanhas)

#KILIMANJARO
foto_kilimanjaro = ImageTk.PhotoImage(Image.open("Kilimanjaro.png"))
btn_kilimanjaro=Button(window,text="",width = 375, height = 200,image = foto_kilimanjaro,command=kilimanjaro)
lbl_kilimanjaro = Label(window,text="",width = 375, height = 200,image = foto_kilimanjaro)
desc_kilimanjaro = Label(window,text="O Parque Nacional do Kilimanjaro já é famoso pelo enorme nome que carrega da famosa montanha da luz,\ntambém conhecida como Kilimanharo.O parque nacional é um dos parques nacionais que se encontram em\num dos países da África Oriental, a Tanzânia. O parque possui a montanha mais alta com neve na África,\nchamada de parque nacional Kilimanjaro. O parque nacional Kilimanjaro está localizado na parte norte da\nTanzânia, logo acima das colinas suaves e do planalto do parque nacional Amboeseli.", font=("Calibri 14"),bg="#aba8e2", width = 85, height = 5)

#KIRKJUFELL
foto_kirkjufell = ImageTk.PhotoImage(Image.open("Kirkjufell.png"))
btn_kirkjufell=Button(window,text="",width = 375, height = 200,image = foto_kirkjufell,command=kirkjufell)
lbl_kirkjufell = Label(window,text="",width = 375, height = 200,image = foto_kirkjufell)
desc_kirkjufell = Label(window,text="Kirkjufell, ou 'Montanha da Igreja', é um pico de formato distinto encontrado na costa norte da Península\nde Snæfellsnes, na Islândia, a apenas uma curta distância da cidade de Grundarfjörður. É frequentemente\nchamada de 'a montanha mais fotografada da Islândia',devido à sua formação dramática\ne localização costeira perfeita.", font=("Calibri 14"),bg="#aba8e2", width = 85, height = 5)

#MATTERHORN
foto_matterhorn = ImageTk.PhotoImage(Image.open("Matterhorn.png"))
btn_matterhorn=Button(window,text="",width = 375, height = 200,image = foto_matterhorn,command=dev)

#SERRA DA ESTRELA
foto_estrela = ImageTk.PhotoImage(Image.open("estrela.png"))
btn_estrela=Button(window,text="",width = 375, height = 200,image = foto_estrela,command=dev)

#endregion

#region CIDADES
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

#BOTÃO CIDADES
foto_cidades=ImageTk.PhotoImage(Image.open("cidades.png"))
btn_cidades=Button(window,text="",width = 220, height = 395,image = foto_cidades,command = dev)

#endregion

#region PRAIAS

def praias():

    #REDIMENSIONAR A JANELA
    w = 885
    h = 560
    ws = window.winfo_screenwidth()
    hs = window.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    window.geometry('%dx%d+%d+%d' % (w, h, x, y))

    window.configure(bg ="#025083")

    #REMOVE OS BOTÕES NÃO NECESSÁRIOS
    btn_guias.place_forget()
    btn_montanhas.place_forget()
    btn_cidades.place_forget()
    btn_praia.place_forget()
    btn_sair.place_forget()

    #REMOVE A LABEL DO MENU PRINCIPAL
    lbl_menu.place_forget()

    #INSERE O BOTÃO PARA RETORNAR AO MENU 
    btn_retornar_praia.place_forget()
    btn_retornar_menu.place(x=740,y=17)

    #REMOVE OS BOTÕES DE COMENTÁRIO
    btn_comentar_anse.place_forget()
    btn_comentar_zlatni.place_forget()
    btn_comentar_navagio.place_forget()
    btn_comentar_kaanapali.place_forget()

    txt_comentario.place_forget()

    btn_submeter_anse.place_forget()
    btn_submeter_zlatni.place_forget()
    btn_submeter_navagio.place_forget()
    btn_submeter_kaanapali.place_forget()

    btn_ver_anse.place_forget()

    #REMOVE OS BOTÕES DE GOSTO
    btn_gosto_anse.place_forget()
    btn_gosto_zlatni.place_forget()
    btn_gosto_navagio.place_forget()
    btn_gosto_kaanapali.place_forget()

    #INSERE O NOME DE UTILIZADOR QUE ESTÁ AUTENTICADO
    user = txt_utilizador.get()
    lbl_user = Label(window, text= f"Utilizador: {user}",fg="white",font = ("Calibri bold", 10),width=20,height=1,bg = "#025083")
    lbl_user.place(x=10,y=20)

    #TITULO DA JANELA
    lbl_praias.place(x=442.5,y=60, anchor=CENTER)
    
    #BOTÃO DA PRAIA ANSE
    btn_anse.place(x=55,y=90)

    #REMOVE A IMAGEM E A DESCRIÇÃO DA ANSE
    lbl_anse.place_forget()
    desc_anse.place_forget()

    #BOTÃO PRAIA NAVAGIO
    btn_navagio.place(x=55, y=310)

    #REMOVE A IMAGEM E A DESCRIÇÃO DA NAVAGIO
    lbl_navagio.place_forget()
    desc_navagio.place_forget()

    #BOTÃO PRAIA ZLATNI
    btn_zlatni.place(x=450,y=90)

    #REMOVE A IMAGEM E A DESCRIÇÃO DA ZLATNI
    lbl_zlatni.place_forget()
    desc_zlatni.place_forget()

    #BOTÃO PRAIA KAANAPALI
    btn_kaanapali.place(x=450, y=310)

    #REMOVE A IMAGEM E A DESCRIÇÃO DA KAANAPALI
    lbl_kaanapali.place_forget()
    desc_kaanapali.place_forget()

def navagio():

    #REDIMENSIONAR A JANELA
    w = 885
    h = 560
    ws = window.winfo_screenwidth()
    hs = window.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    window.geometry('%dx%d+%d+%d' % (w, h, x, y))

    #REMOVE OS BOTÕES DAS PRAIAS
    btn_navagio.place_forget()
    btn_anse.place_forget()
    btn_zlatni.place_forget()
    btn_kaanapali.place_forget()

    #TROCA O BOTÃO MENU POR BOTÃO RETORNAR
    btn_retornar_menu.place_forget()
    btn_retornar_praia.place(x=740,y=17)

    #INSERE A IMAGEM
    lbl_navagio.place(x=445, y=200, anchor = CENTER)

    #DESCRIÇÃO DA PRAIA
    desc_navagio.place(x=445,y=400, anchor=CENTER)

    #COMENTÁRIO
    btn_comentar_navagio.place(x=502,y=520,anchor=CENTER)

    #GOSTO
    btn_gosto_navagio.place(x=372,y=520,anchor=CENTER)

def anse():
    #REDIMENSIONAR A JANELA
    w = 885
    h = 560
    ws = window.winfo_screenwidth()
    hs = window.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    window.geometry('%dx%d+%d+%d' % (w, h, x, y))

    #REMOVE OS BOTÕES DAS PRAIAS
    btn_navagio.place_forget()
    btn_anse.place_forget()
    btn_zlatni.place_forget()
    btn_kaanapali.place_forget()

    #TROCA O BOTÃO MENU POR BOTÃO RETORNAR
    btn_retornar_menu.place_forget()
    btn_retornar_praia.place(x=740,y=17)

    #INSERE A IMAGEM
    lbl_anse.place(x=445, y=200, anchor = CENTER)

    #DESCRIÇÃO DA PRAIA
    desc_anse.place(x=445,y=400, anchor=CENTER)

    #COMENTÁRIO
    btn_comentar_anse.place(x=414,y=520,anchor=CENTER)
    btn_ver_anse.place(x=572, y=520, anchor = CENTER)

    #GOSTO
    btn_gosto_anse.place(x=292,y=520,anchor=CENTER)

def zlatni():
    #REDIMENSIONAR A JANELA
    w = 885
    h = 560
    ws = window.winfo_screenwidth()
    hs = window.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    window.geometry('%dx%d+%d+%d' % (w, h, x, y))

    #REMOVE OS BOTÕES DAS PRAIAS
    btn_navagio.place_forget()
    btn_anse.place_forget()
    btn_zlatni.place_forget()
    btn_kaanapali.place_forget()

    #TROCA O BOTÃO MENU POR BOTÃO RETORNAR
    btn_retornar_menu.place_forget()
    btn_retornar_praia.place(x=740,y=17)

    #INSERE A IMAGEM
    lbl_zlatni.place(x=445, y=200, anchor = CENTER)

    #DESCRIÇÃO DA PRAIA
    desc_zlatni.place(x=445,y=400, anchor=CENTER)

    #COMENTÁRIO
    btn_comentar_zlatni.place(x=502,y=520,anchor=CENTER)

    #GOSTO
    btn_gosto_zlatni.place(x=372,y=520,anchor=CENTER)

def kaanapali():
    #REDIMENSIONAR A JANELA
    w = 885
    h = 560
    ws = window.winfo_screenwidth()
    hs = window.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    window.geometry('%dx%d+%d+%d' % (w, h, x, y))

    #REMOVE OS BOTÕES DAS PRAIAS
    btn_navagio.place_forget()
    btn_anse.place_forget()
    btn_zlatni.place_forget()
    btn_kaanapali.place_forget()

    #TROCA O BOTÃO MENU POR BOTÃO RETORNAR
    btn_retornar_menu.place_forget()
    btn_retornar_praia.place(x=740,y=17)

    #INSERE A IMAGEM
    lbl_kaanapali.place(x=445, y=200, anchor = CENTER)

    #DESCRIÇÃO DA PRAIA
    desc_kaanapali.place(x=445,y=400, anchor=CENTER)

    #COMENTÁRIO
    btn_comentar_kaanapali.place(x=502,y=520,anchor=CENTER)

    #GOSTO
    btn_gosto_kaanapali.place(x=372,y=520,anchor=CENTER)

#BOTÃO PRINCIPAL
foto_praia=ImageTk.PhotoImage(Image.open("praias.png"))
btn_praia=Button(window,text="",width = 220, height = 395,image = foto_praia, command = praias)

#BOTÃO RETORNAR PRAIAS
btn_retornar_praia = Button(window, text="Retornar", fg="black",font = ("Calibri 12 bold"), width=10,height=1, command=praias)

#NAVAGIO
foto_navagio = ImageTk.PhotoImage(Image.open("navagio.png"))
btn_navagio = Button(window,text="",width = 375, height = 200,image = foto_navagio,command=navagio)
lbl_navagio = Label(window,text="",width = 375, height = 200,image = foto_navagio)
desc_navagio = Label(window,text="Navagio está localizado no noroeste de Zakynthos (Ilha grega). As colinas de alturas variáveis que\nprotegem a baía e a praia dos ventos fortes contribuem para a sua singularidade. A praia é coberta por\nareia macia e limpa de cor creme e uma água bastante clara.", font=("Calibri 14"),bg="#025083", fg="white", width = 80, height = 4)

#ANSE
foto_anse = ImageTk.PhotoImage(Image.open("anse.png"))
btn_anse = Button(window,text="",width = 375, height = 200,image = foto_anse,command=anse)
lbl_anse = Label(window,text="",width = 375, height= 200, image=foto_anse)
desc_anse = Label(window,text="Localizada no extremo oeste de La Digue, Anse Source d'Argent é um autêntico paraíso na terra, uma\nbela praia de areia branca e calmas águas turquesas rodeada por coqueiros e curiosos blocos de granito\nmoldados com o passar do tempo.",font=("Calibri 14"), bg="#025083", fg="white", width = 80, height = 4)

#ZLATNI
foto_zlatni = ImageTk.PhotoImage(Image.open("zlatni.png"))
btn_zlatni = Button(window,text="",width = 375, height = 200,image = foto_zlatni,command=zlatni)
lbl_zlatni = Label(window,text="",width = 375, height= 200, image=foto_zlatni)
desc_zlatni = Label(window,text="Zlatni Rat é uma praia na cidade de Bol, que fica na Ilha de Brač. Um fenômeno natural da região\nformou uma ponta de areia, que parece um chifre, cercado de um mar turquesa maravilhoso.\nPor conta desse visual, a praia ganhou esse nome: Zlatni Rat, que significa\nChifre Dourado, na língua local. ",font=("Calibri 14"), bg="#025083", fg="white", width = 80, height = 4)

#KAANAPALI
foto_kaanapali = ImageTk.PhotoImage(Image.open("Kaanapali.png"))
btn_kaanapali = Button(window,text="",width = 375, height = 200,image = foto_kaanapali,command=kaanapali)
lbl_kaanapali = Label(window,text="",width = 375, height= 200, image=foto_kaanapali)
desc_kaanapali = Label(window,text="Kaanapali Beach em Maui se estende por 3 milhas entre o Hyatt Regency Maui para o sul e Sheraton\nMaui para o norte. Muito tempo atrás, costumava ser um playground para os membros da realeza de\nMaui e hoje esta praia incrível é um dos pontos mais visitados da ilha.",font=("Calibri 14"), bg="#025083", fg="white", width = 80, height = 4)

#TITULO: PRAIAS
lbl_praias = Label(window, text= "PRAIAS",fg = "white", bg="#025083", font=("Calibri 25 bold"), width = 30, height = 1)

#endregion

#region ROADTRIPS

#BOTÃO ROADTRIPS
foto_roadtrips=ImageTk.PhotoImage(Image.open("roadtrips.png"))
btn_roadtrip=Button(window, text = "", width = 220, height = 395,image = foto_roadtrips, command=dev)

#endregion

#region TRILHOS E OUTDOORS

#BOTÃO TRILHOS E OUTDOORS
foto_trilhos=ImageTk.PhotoImage(Image.open("trilhos.png"))
btn_trilhos=Button(window, text = "",width = 220, height = 395,image = foto_trilhos,command=dev)

#endregion

#region GESTÃO DE COMENTÁRIOS

#COMENTAR ANSE
def comentar_anse():
    txt_comentario.place(x=402,y=490, anchor=CENTER)
    btn_comentar_anse.place_forget()
    btn_gosto_anse.place_forget()
    btn_submeter_anse.place(x=795,y=490,anchor=CENTER)

def submeter_comentario_anse():

    comentario = txt_comentario.get("1.0",END)
    user = txt_utilizador.get()

    f = open("comentarios.txt","a")
    f.write("Anse: " + user + ":" + comentario)
    messagebox.showinfo("Sucesso","O seu comentário foi adicionado com sucesso!")
    txt_comentario.delete("1.0",END)

    txt_comentario.place_forget()
    btn_submeter_anse.place_forget()
    btn_comentar_anse.place(x=442,y=520,anchor=CENTER)

def ver_cmt_anse():
    f = open("comentarios.txt","r")
    linhas = f.readlines()
    anse = []
    for i in linhas:
        if str("Anse") in i:
            anse.append(i)
    if anse == []:
        messagebox.showerror("ERRO", "Não existem comentários.")
    else:
        JanComentarios = Toplevel(window)
        JanComentarios.title("Comentários Anse")

        w = 500
        h = 300
        ws = JanComentarios.winfo_screenwidth()
        hs = JanComentarios.winfo_screenheight()
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        JanComentarios.geometry('%dx%d+%d+%d' % (w, h, x, y))

        lbl_cmt_anse= Label(JanComentarios,width=60, height=3,text=anse)
        lbl_cmt_anse.place(x=250,y=150,anchor=CENTER)
        
btn_comentar_anse=Button(window, text="Adicionar comentário",fg="black", font = ("Calibri bold", 12),width=20,height=1, command = comentar_anse)
txt_comentario = Text(window,width=80,height=5)
btn_submeter_anse = Button(window, text="Submeter",fg="black", font = ("Calibri bold", 12),width=10,height=1, command = submeter_comentario_anse)
btn_ver_anse=Button(window, text="Ver comentários",fg="black", font = ("Calibri bold", 12),width=15,height=1, command = ver_cmt_anse)

#COMENTAR ZLATNI
def comentar_zlatni():
    txt_comentario.place(x=402,y=490, anchor=CENTER)
    btn_comentar_zlatni.place_forget()
    btn_gosto_zlatni.place_forget()
    btn_submeter_zlatni.place(x=795,y=490,anchor=CENTER)

def submeter_comentario_zlatni():

    comentario = txt_comentario.get("1.0",END)
    user = txt_utilizador.get()

    f = open("comentarios.txt","a")
    f.write("Zlatni: " + user + ":" + comentario)
    messagebox.showinfo("Sucesso","O seu comentário foi adicionado com sucesso!")

    txt_comentario.place_forget()
    btn_submeter_zlatni.place_forget()
    btn_comentar_zlatni.place(x=442,y=520,anchor=CENTER)

btn_comentar_zlatni=Button(window, text="Adicionar comentário",fg="black", font = ("Calibri bold", 12),width=20,height=1, command = comentar_zlatni)
txt_comentario = Text(window,width=80,height=5)
btn_submeter_zlatni = Button(window, text="Submeter",fg="black", font = ("Calibri bold", 12),width=10,height=1, command = submeter_comentario_zlatni)

#COMENTAR NAVAGIO
def comentar_navagio():
    txt_comentario.place(x=402,y=490, anchor=CENTER)
    btn_comentar_navagio.place_forget()
    btn_gosto_navagio.place_forget()
    btn_submeter_navagio.place(x=795,y=490,anchor=CENTER)

def submeter_comentario_navagio():

    comentario = txt_comentario.get("1.0",END)
    user = txt_utilizador.get()

    f = open("comentarios.txt","a")
    f.write("Navagio: " + user + ":" + comentario)
    messagebox.showinfo("Sucesso","O seu comentário foi adicionado com sucesso!")

    txt_comentario.place_forget()
    btn_submeter_navagio.place_forget()
    btn_comentar_navagio.place(x=442,y=520,anchor=CENTER)

btn_comentar_navagio=Button(window, text="Adicionar comentário",fg="black", font = ("Calibri bold", 12),width=20,height=1, command = comentar_navagio)
txt_comentario = Text(window,width=80,height=5)
btn_submeter_navagio = Button(window, text="Submeter",fg="black", font = ("Calibri bold", 12),width=10,height=1, command = submeter_comentario_navagio)

#COMENTAR KAANAPALI
def comentar_kaanapali():
    txt_comentario.place(x=402,y=490, anchor=CENTER)
    btn_comentar_kaanapali.place_forget()
    btn_gosto_kaanapali.place_forget()
    btn_submeter_kaanapali.place(x=795,y=490,anchor=CENTER)

def submeter_comentario_kaanapali():

    comentario = txt_comentario.get("1.0",END)
    user = txt_utilizador.get()

    f = open("comentarios.txt","a")
    f.write("Kaanapali: " + user + ":" + comentario)
    messagebox.showinfo("Sucesso","O seu comentário foi adicionado com sucesso!")

    txt_comentario.place_forget()
    btn_submeter_kaanapali.place_forget()
    btn_comentar_kaanapali.place(x=442,y=520,anchor=CENTER)

btn_comentar_kaanapali=Button(window, text="Adicionar comentário",fg="black", font = ("Calibri bold", 12),width=20,height=1, command = comentar_kaanapali)
txt_comentario = Text(window,width=80,height=5)
btn_submeter_kaanapali = Button(window, text="Submeter",fg="black", font = ("Calibri bold", 12),width=10,height=1, command = submeter_comentario_kaanapali)

#endregion

#region CLASSIFICAÇÕES

def gosto_anse():
    f = open("classificacoes.txt","a")
    f.write("Anse" + "\n")
    
    f= open("classificacoes.txt","r")
    encontrar = f.read()
    num = encontrar.count("Anse")

    messagebox.showinfo("Sucesso!",f"A sua classificação foi adicionada com sucesso! Esta praia já tem {num} gosto(s).")

def gosto_zlatni():
    f = open("classificacoes.txt","a")
    f.write("Zlatni" + "\n")
    
    f= open("classificacoes.txt","r")
    encontrar = f.read()
    num = encontrar.count("Zlatni")

    messagebox.showinfo("Sucesso!",f"A sua classificação foi adicionada com sucesso! Esta praia já tem {num} gosto(s).")

def gosto_navagio():
    f = open("classificacoes.txt","a")
    f.write("Navagio" + "\n")
    
    f= open("classificacoes.txt","r")
    encontrar = f.read()
    num = encontrar.count("Navagio")

    messagebox.showinfo("Sucesso!",f"A sua classificação foi adicionada com sucesso! Esta praia já tem {num} gosto(s).")

def gosto_kaanapali():
    f = open("classificacoes.txt","a")
    f.write("Kaanapali" + "\n")
    
    f= open("classificacoes.txt","r")
    encontrar = f.read()
    num = encontrar.count("Kaanapali")

    messagebox.showinfo("Sucesso!",f"A sua classificação foi adicionada com sucesso! Esta praia já tem {num} gosto(s).")

#BOTÕES
btn_gosto_anse=Button(window, text="Gosto",fg="green", font = ("Calibri bold", 12),width=6,height=1, command = gosto_anse)
btn_gosto_zlatni=Button(window, text="Gosto",fg="green", font = ("Calibri bold", 12),width=5,height=1, command = gosto_zlatni)
btn_gosto_navagio=Button(window, text="Gosto",fg="green", font = ("Calibri bold", 12),width=5,height=1, command = gosto_navagio)
btn_gosto_kaanapali=Button(window, text="Gosto",fg="green", font = ("Calibri bold", 12),width=5,height=1, command = gosto_kaanapali)

#endregion

JanelaLogin()
window.mainloop()
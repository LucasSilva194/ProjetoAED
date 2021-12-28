def Login():
    user = txt_utilizador.get()
    password = txt_passe.get()
    
    guardar = user + ";" + password
    f = open("basedados.txt","r")
    lista = f.readlines()

    if str(guardar) in str(lista):
        messagebox.showinfo("Bem vindo",f"Olá {user}, o seu login foi efetuado com sucesso")
    else:
        messagebox.showerror("Erro","Utilizador não encontrado. Por favor crie conta.")

    txt_utilizador.set("")
    txt_passe.set("")

def CriarConta():
    user = txt_utilizador,get()
    password = txt_passe.get()
    cpassword = txt_cpasse.get()

    guardar = user + ";" + password
    f = open("basedados.txt","r")
    f.close()
    if user != "" and password != "":
        lista = f.readlines()
        if str(guardar) in str(lista):
            messagebox.showerror("Erro","Já existe uma conta com esses dados, por favor efetue login")
            txt_utilizador.set("")
            txt_passe.set("")
        elif str(user) in str(lista):
            messagebox.showerror("Erro","Esse utilizador já existe")
            txt_utilizador.set("")
            txt_passe.set("")
        else:
            if password == cpassword:
                f = open("basedados.txt","a")
                f.write(f"{user};{password}\n")
                messagebox.showinfo("A sua conta foi criada com sucesso!")
                txt_utilizador.set("")
                txt_passe.set("")
                txt_cpasse.set("")
            else:
                messagebox.showerror("Erro","As duas passwords não coincidem")
                txt_utilizador.set("")
                txt_passe.set("")
                txt_cpasse.set("")
def Login():
    user = txt_utilizador.get()
    password = txt_passe.get()
    
    guardar = user + ";" + password
    f = open("basedados.txt","r")
    lista = f.readlines()

    if str(guardar) in str(lista):
        

    txt_utilizador.set("")
    txt_passe.set("")
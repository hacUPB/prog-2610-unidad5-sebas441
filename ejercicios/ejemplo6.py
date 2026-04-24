# Se puede utilizar donde tu creas que se pueda generar un error es decir con el try intenta y busca si existe pero si no entonces hace el except y te manda el mensaje 
try:
    with open("archivo_que_no_existe.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("Error: Estás intentando abrir un archivo que no existe.")
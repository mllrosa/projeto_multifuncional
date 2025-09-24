import os
def verificar_arquivos(): 
    arquivos = os.listdir()
    for item in arquivos:
        print(item)

verificar_arquivos()
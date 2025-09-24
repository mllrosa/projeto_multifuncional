import os, flet as ft

# A ideia será vocês criarem uma interface que faça os comandos exigidos de um sistema simples com as bibliotecas mencionadas acima.


# 2 - Criar arquivos dentro da pasta e fora.
# 4 - Renomear arquivo
# 5 - Verificar e excluir arquivo

import os
import flet as ft

def main(page: ft.Page):
    page.title = "Interface com OS"
    page.theme_mode = "dark"

    # Função para verificar arquivos FOI
    def verificar_arquivos(a): 
        arquivos = os.listdir()
        for item in arquivos:
            print(item)
        page.update()

    # Função para criar pastas FOI
    def criar_pasta(e):
        texto = texto_recebido.value
        try:
            os.mkdir(texto)
            informativo.value = f"Pasta criada: '{texto}'"
        except FileExistsError:
            informativo.value = f"A pasta '{texto}' já existe."
        page.update()
    
    # Função para criar arquivos FOI
    def criar_arquivo(e):
        texto = texto_recebido.value
        try:
            open(texto, "w").close()
            informativo.value = f"Arquivo criado: '{texto}'"
        except Exception as erro:
            informativo.value = f"Erro: {erro}"
        page.update()

    # Campos e botões FOI
    texto_recebido = ft.TextField(label="Escreva o nome do arquivo/pasta...")
    botao_pasta = ft.ElevatedButton("CRIAR PASTA", bgcolor="PURPLE", color="WHITE", width=200, on_click=criar_pasta)
    botao_arquivo = ft.ElevatedButton("CRIAR ARQUIVO", bgcolor="CYAN", color="BLACK", width=200, on_click=criar_arquivo)
    informativo = ft.Text("", size=20, color="white")
    botao_verificar_arquivos = ft.ElevatedButton("VERIFICAR ARQUIVOS", bgcolor="CYAN", color="BLACK", width=200, on_click=verificar_arquivos)

    # excluir arquivo
    def excluir_arquivo():
        


    

    # Layout
    page.add(
        ft.Row([texto_recebido], alignment="center"),
        ft.Row([botao_pasta, botao_arquivo, botao_verificar_arquivos], alignment="center"),
        ft.Row([informativo], alignment="center")
     
    )

ft.app(target=main)
import os, flet as ft

# A ideia será vocês criarem uma interface que faça os comandos exigidos de um sistema simples com as bibliotecas mencionadas acima.
# 2 - Criar arquivos dentro da pasta e fora.


import os
import flet as ft

def main(page: ft.Page):
    page.title = "Interface com OS"
    page.theme_mode = "dark"

# FUNCOES ======================================================

    # 5 - Verificar e excluir arquivo
    def verificar_excluir(a):
        texto = texto_principal.value
        try:
            if os.path.exists(texto):
                os.remove(texto)
                print("Arquivo apagado")
            else:
                print("Arquivo não encontrado")
                informativo.value = (f"Pasta {texto} deletada com sucesso")
        except FileExistsError:
            informativo.value = f"A pasta '{texto}' não existe."
            

    # Função para verificar arquivos
    def verificar_arquivos(a):
        arquivos = os.listdir()
        informativo.value = arquivos
        page.update()


    # 1 - Criar uma pasta
    # 2 - Criar arquivos dentro da pasta e fora.
    def criar_pasta(e):
        texto = texto_principal.value
        try:
            os.mkdir(texto)
            informativo.value = f"Pasta criada: '{texto}'"
        except FileExistsError:
            informativo.value = f"A pasta '{texto}' já existe."
        page.update()
    
    # Função para criar arquivos FOI
    def criar_arquivo(e):
        texto = texto_principal.value
        try:
            open(texto, "w").close()
            informativo.value = f"Arquivo criado: '{texto}'"
        except Exception as erro:
            informativo.value = f"Erro: {erro}"
        page.update()

    def renomear_arquivos(a):
        try:
            nome_arquivo = ft.TextField(label="Escreva o nome do arquivo...")
            page.update()
            nome_novo_arquivo = ft.TextField(label="Escreva o novo nome do arquivo...")
            os.rename(nome_arquivo, nome_novo_arquivo)
        except Exception as erro:
            informativo.value = "Digite os nomes corretamente!"
        page.update()


    # Campos e botões FOI
    texto_principal = ft.TextField(label="Escreva o nome do arquivo/pasta...")
    botao_pasta = ft.ElevatedButton("CRIAR PASTA", bgcolor="PURPLE", color="WHITE", width=200, on_click=criar_pasta)
    botao_arquivo = ft.ElevatedButton("CRIAR ARQUIVO", bgcolor="CYAN", color="BLACK", width=200, on_click=criar_arquivo)
    botao_excluir_arquivo = ft.ElevatedButton("EXCLUIR ARQUIVOS", bgcolor="CYAN", color="BLACK", width=200, on_click= verificar_excluir)
    botao_renomear = ft.ElevatedButton("RENOMEAR ARQUIVOS", bgcolor="CYAN", color="BLACK", width=200, on_click= renomear_arquivos)
    botao_listar_arquivos = ft.ElevatedButton("LISTAR ARQUIVOS", bgcolor="CYAN", color="BLACK", width=200, on_click= verificar_arquivos)
    informativo = ft.Text("", size=20, color="white")

    
    

    # Layout
    page.add(
        ft.Row([texto_principal], alignment="center"),
        ft.Row([botao_pasta, botao_arquivo, botao_excluir_arquivo, botao_renomear, botao_listar_arquivos], alignment="center"),
        ft.Row([informativo], alignment="center")
    )

ft.app(target=main)
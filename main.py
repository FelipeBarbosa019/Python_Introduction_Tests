import os

def criar_arquivo(nome_arquivo, conteudo=''):
    with open(nome_arquivo, 'w') as f:
        f.write(conteudo)

def ler_arquivo(nome_arquivo):
    with open(nome_arquivo, 'r') as f:
        return f.read()

def excluir_arquivo(nome_arquivo):
    os.remove(nome_arquivo)

def criar_pasta(nome_pasta):
    os.mkdir(nome_pasta)

def excluir_pasta(nome_pasta):
    os.rmdir(nome_pasta)
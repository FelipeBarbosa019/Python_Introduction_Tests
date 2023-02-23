import pytest
import os
from main import criar_arquivo, ler_arquivo, excluir_arquivo, criar_pasta, excluir_pasta


# Função que cria um arquivo de teste com o conteúdo especificado
@pytest.fixture
def arquivo_teste():
    nome_arquivo = 'arquivo_teste.txt'
    criar_arquivo(nome_arquivo, 'Conteúdo do arquivo de teste')

    # O yield indica o ponto de início e fim da execução da fixture
    yield nome_arquivo

    # Remove o arquivo criado pela fixture
    excluir_arquivo(nome_arquivo)

# Função que cria um diretório com o nome especificado
@pytest.fixture
def pasta_teste():
    nome_pasta = 'pasta_teste'
    criar_pasta(nome_pasta)
    yield nome_pasta
    excluir_pasta(nome_pasta)


# Testa se o arquivo foi criado corretamente
def test_criar_arquivo(arquivo_teste):
    assert os.path.exists(arquivo_teste)

# Testa se o conteúdo do arquivo está correto
def test_ler_arquivo(arquivo_teste):
    assert ler_arquivo(arquivo_teste) == 'Conteúdo do arquivo de teste'

# Testa se a pasta foi criada corretamente
def test_criar_pasta(pasta_teste):
    assert os.path.exists(pasta_teste)

# Testa se o arquivo foi excluído corretamente
def test_excluir_arquivo():
    arquivo_teste = 'arquivo_teste_excluir.txt'
    criar_arquivo(arquivo_teste, 'Conteúdo do arquivo de teste')
    excluir_arquivo(arquivo_teste)
    assert not os.path.exists(arquivo_teste)

# Testa se a pasta foi excluída corretamente
def test_excluir_pasta():
    pasta_teste = 'pasta_teste_excluir'
    criar_pasta(pasta_teste)
    excluir_pasta(pasta_teste)
    assert not os.path.exists(pasta_teste)


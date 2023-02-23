##Projeto de Testes com Pytest para Manipulação de Arquivos
Este projeto foi criado, durante o curso de python do programa Alpha edtech. Tem a motivação de demonstrar e praticar o uso do Pytest para criar testes automatizados para a manipulação de arquivos em disco.

O projeto contém duas fixtures, uma para criar um diretório e outra para criar um arquivo com conteúdo de teste. Cada fixture cria um arquivo ou diretório antes da execução de um teste e remove o arquivo/diretório após a execução do teste.

Há dois testes definidos, um para testar se o diretório é criado corretamente e outro para testar se o arquivo é criado corretamente e se o conteúdo do arquivo está correto. A exclusão do arquivo e diretório também é testada.

O projeto está organizado da seguinte maneira:

Requisitos:
O projeto requer o Python e o Pytest instalados. Para isso execute:

```
pip install pytest
```

Uso:
Para executar os testes, navegue para o diretório do projeto e execute o seguinte comando no terminal:

```
python -m pytest test_main.py
```

Isso executará todos os testes definidos no projeto.

# Sobre o projeto
 Interface web que aceita upload do arquivo CNAB, normaliza os dados e armazena-os em um banco de dados relacional, armazenando também o arquivo CNAB com o dia e a hora para um melhor controle das transações.
 
 # Funcionalidades e rotas 
  No caminho http://127.0.0.1:8000/file/ é onde pode ser feito o upload dos arquivos CNAB, tenha certeza de que o arquivo está no padrão correto para que não ocorra nenhum erro, os dados contidos no arquivo serão interpretados e armazenados no banco de dados.
  
  No caminho http://127.0.0.1:8000/stores/<str:store_name> o usuário consegue pegar todas as operações de uma determinada loja passando na url o nome da loja, trazendo as operações com seu nome específicado, o nome da loja, e o saldo da loja.
  
 # Tecnologias
 
 - Django Framework
 - SQLite 
 - Python 3
 
 # Como instalar e rodar a aplicação 
 

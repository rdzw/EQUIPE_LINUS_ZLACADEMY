-- Banco de Dados MySQL
-- Apagar o banco de dados
drop database banco;
-- Criar o banco de dados
create database banco;
-- Atribuir os privilégios de acesso aos objetos do banco
-- para o usuário root
GRANT ALL PRIVILEGES ON banco.* TO 'root' @'localhost';
-- Acesar o banco de dados: banco
USE banco;

CREATE TABLE eleitor(
cpf varchar(11) NOT NULL,
nome varchar(100) NOT NULL,
data_nascimento varchar(10) NOT NULL,
nome_mae varchar(100) NOT NULL,
cep varchar(8) NOT NULL,
nro_endereco varchar(10) NOT NULL,
nro_titulo varchar(14) NOT NULL,
situacao varchar(20) NOT NULL,
secao varchar(4) NOT NULL,
zona varchar(4) NOT NULL,
local_votacao varchar(200) NOT NULL,
endereco_votacao varchar(200) NOT NULL,
bairro varchar(100) NOT NULL,
municipio_uf varchar(100) NOT NULL,
pais varchar(50) NOT NULL,
PRIMARY KEY (cpf)
);
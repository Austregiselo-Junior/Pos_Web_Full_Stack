# Comando DDL - Cria uma tabela
CREATE TABLE clientes 
(
	id_clientes INT PRIMARY KEY AUTO_INCREMENT, 
    nome VARCHAR(255) NOT NULL, 
	email VARCHAR(255), 
	cpf VARCHAR(11) NOT NULL, 
	data_Nascimento DATE
);

# Comandos DML
# Visualiza dados de uma tabela
SELECT * FROM clientes;

# Inseirndo dados em todos os campos de uma tabela
INSERT INTO clientes VALUES (
	5,
	'Daniel Brandão',
	'daniel@brandao.com',
	'11122233344',
	'1988-12-20'
);

# Inserindo dados de algumas campos de uma tabela
INSERT INTO clientes (nome, email, cpf) VALUES (
	'Joana Silva', 
	'joana@email.com',
	'11122233355'
);

# Atualizando o registro de uma tabela
UPDATE clientes SET id_clientes = 2 WHERE id_clientes = 6;

# Excluindo um registro identificando o campo ID
DELETE FROM clientes WHERE id_clientes = 6;

# Excluindo um registro identificando o campo nome que contenha Daniel + alguma coisa
DELETE FROM clientes WHERE nome LIKE "Daniel%";

insert into clientes (id_clientes, nome, cpf, date_Nascimento) values (3, "Miqueias", "09678153475", "1950-7-08");
insert into clientes (nome, cpf)values ("Jhon", "00678103475");

update clientes set cpf = "00078153480" where id_clientes = 3;
drop table clientes;
delete from clientes where nome = "Jhon";


CREATE TABLE produto 
(
	id_produto INT PRIMARY KEY AUTO_INCREMENT, 
    nome VARCHAR(255) NOT NULL, 
	descricao VARCHAR(355), 
	preco decimal NOT NULL, 
	categoria VARCHAR(255)
);

insert into produto (nome, descricao, preco, categoria) values 
("dyssei G6", "Monitor Samsung QWHD...", 3500.0, "Monitor"),
("dyssei G5", "Monitor Samsung QWHD curvado...", 25000, "Monitor"),
("Galaxy Book 2 Pro", "Notebook 16GB, tela AMOLED", 8900.9, "Notebook"),
("Galaxy Book 3 Ultra", "Notebook 32GB, tela AMOLED", 18900.90, "Notebook"),
("Samsung s24", "celuar 32GB com IA da samsung", 4000.90, "Celular");

insert into produto (nome, preco, categoria)values ("Jhon", "00678103475", "1290-12-08");

update produto set nome = "Galaxy book 3" where id_clientes = 3;
drop table produto;
delete from produto where id_clientes = 3;

SELECT * FROM banco_web.produto;

# Criando uma tabela com chaves estrangeiras
CREATE TABLE IF NOT EXISTS pedidos (
  id_pedidos INT NOT NULL AUTO_INCREMENT,
  id_cliente INT NOT NULL,
  id_produto INT NOT NULL,
  data_pedido DATE NOT NULL,
  valor_total DECIMAL(9,2) NOT NULL,
  PRIMARY KEY (id_pedidos),
  CONSTRAINT fk_tabela_produto
    FOREIGN KEY (id_produto)
    REFERENCES produto (id_produto),
  CONSTRAINT fk_tabela_cliente
    FOREIGN KEY (id_cliente)
    REFERENCES clientes (id_clientes)
)
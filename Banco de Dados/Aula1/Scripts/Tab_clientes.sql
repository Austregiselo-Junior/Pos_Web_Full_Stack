# Comandos DDL - Linguagem de definição de dados, Create, Alter, Drop
# Comandoss DML - Data Manipulation languege, é o CRUD - Create, Read, Update, Delete.
create table clientes
(
	id_clientes int primary key auto_increment, 
    nome varchar(255) not null,
    descrecao text,
    preco decimal not null unique,
    categoria varchar(255)
);

select *  from clientes;

insert into clientes (id_clientes, nome, cpf, date_Nascimento) values (3, "Miqueias", "09678153475", "1950-7-08");
insert into clientes (nome, cpf, date_Nascimento)values ("Jhon", "00678103475", "1290-12-08");

update clientes set cpf = "00078153480" where id_clientes = 3;
drop table clientes;
delete from clientes where nome = "Jhon";


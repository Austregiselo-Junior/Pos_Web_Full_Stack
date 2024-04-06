create table produtos
(
	id_produtos int primary key auto_increment, 
    nome varchar(255) not null,
    descrecao text,
    preco decimal not null unique,
    categoria varchar(255)
);

select *  from produtos;

insert into produtos (nome, descrecao, preco, categoria) values 
("dyssei G6", "Monitor Samsung QWHD...", 3500, "Monitor"),
("dyssei G5", "Monitor Samsung QWHD curvado...", 2500, "Monitor"),
("Galaxy Book 2 Pro", "Notebook 16GB, tela AMOLED", 8900.90, "Notebook"),
("Galaxy Book 3 Ultra", "Notebook 32GB, tela AMOLED", 18900.90, "Notebook"),
("Samsung s24", "celuar 32GB com IA da samsung", 4900.90, "Celular");

insert into produtos (nome, preco, categoria)values ("Jhon", "00678103475", "1290-12-08");

update produtos set nome = "Galaxy book 3" where id_clientes = 3;
drop table produtos;
delete from produtos where id_clientes = 3;


create table pedidos
(
	id_pedidos int not null auto_increment,
    id_cliente int not null,
    id_produto int not null,
    data_pedido date not null,
    valor_total decimal(9,2) not null,
    primary key (id_pedidos),
    constraint fk_tabela_produto foreign key (id_produto) references produtos(id_produtos),
    constraint fk_tabela_cliente foreign key (id_cliente) references clientes(id_clientes)
);

select *  from pedidos;
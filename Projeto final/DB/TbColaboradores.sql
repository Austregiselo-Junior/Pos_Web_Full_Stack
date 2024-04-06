Create table TbColaboradores(
Id int Primary key auto_increment, 
Nome varchar(100) not null, 
Cpf varchar(100) not null,
Email varchar(100) not null,
Telefone varchar(20) not null,
NomedasClinicasqueTrabalha varchar(300) not null,
Id_Clinica int not null,
constraint fk_TbClinicas foreign key auto_increment (Id_Clinica) references tbclinicas(Id));

insert into TbColaboradores (Nome, Cpf, Email, Telefone, NomedasClinicasqueTrabalha, Id_Clinica) values
("Miqueias Lincon", "09678153475", "Lincon@gmail.com", "83998905014", "Clinica de Terapia Ocupacional", "1");

select *  from TbColaboradores;

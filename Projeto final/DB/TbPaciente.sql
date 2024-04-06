Create table TbPaciente(
Id int Primary key auto_increment, 
Nome varchar(100) not null, 
Cpf varchar(100) not null,
Email varchar(100) not null,
Telefone varchar(20) not null,
NomedoColaborador varchar(300) not null,
NomedaClinica varchar(300) not null,
Id_Colaborador int not null,
Id_Clinica int not null,
constraint fk_TbColaborador foreign key auto_increment (Id_Colaborador) references tbcolaboradores(Id),
constraint fk_TbClinica foreign key auto_increment (Id_Clinica) references tbclinicas(Id));

insert into TbPaciente (Nome, Cpf, Email, Telefone, NomedoColaborador, NomedaClinica, Id_Colaborador, Id_Clinica) values
("Caio Lima", "09678123475", "Caio@gmail.com", "83998901234", "Miqueias Lincon", "Clinica de Terapia Ocupacional", "1", "1");

select *  from TbPaciente;
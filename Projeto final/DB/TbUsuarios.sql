Create Database projetofinaldb;

Create Table TbClinicas
(Id int Primary key auto_increment, 
Nome varchar(100) not null, 
Loguin varchar(100) not null, 
Senha varchar(100) not null);

Insert TbClinicas
(Nome, Loguin, Senha)
Values
('Clinica de Terapia Ocupacional', 'Ocupacional@gmail.com', 'Ocupacional@123');

select * from TbClinicas;
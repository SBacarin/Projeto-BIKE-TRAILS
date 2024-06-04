CREATE DATABASE BIKE_TRAILS;
USE BIKE_TRAILS;
create table TRILHAS(
    codigo int not null primary key,
    apelido varchar(100) not null,
    descricao varchar(400),
    km_total varchar(60),
    tempo_mov varchar(60),
    elevacao  varchar(60),
    grau_dif varchar(60),
    dt_ultima_realiz date); 

select * from trilhas;


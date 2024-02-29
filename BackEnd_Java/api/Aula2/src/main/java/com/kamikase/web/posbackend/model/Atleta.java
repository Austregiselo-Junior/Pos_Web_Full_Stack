package com.kamikase.web.posbackend.model;

import jakarta.persistence.*;
import jakarta.validation.constraints.Email;
import jakarta.validation.constraints.NotEmpty;
import lombok.Getter;
import lombok.Setter;
import org.hibernate.validator.constraints.br.CPF;
import validator.EmailValidation;

import java.io.Serializable;

@Getter
@Setter
@Entity
public class Atleta implements Serializable {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Integer id;
    @Column(length = 150)
    @NotEmpty(message = "The name can not emplity")
    private String nome;
    private Integer anoNascimento;
    private String esporte;
    @Email
    @EmailValidation
    private String email;
    @CPF
    private String cpf;

}

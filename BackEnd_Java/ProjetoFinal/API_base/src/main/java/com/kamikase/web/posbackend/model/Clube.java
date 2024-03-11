package com.kamikase.web.posbackend.model;


import com.kamikase.web.posbackend.validator.EmailValidation;
import jakarta.persistence.*;
import jakarta.validation.constraints.Email;
import jakarta.validation.constraints.NotEmpty;
import lombok.Getter;
import lombok.Setter;
import org.hibernate.validator.constraints.br.CPF;

import java.io.Serializable;
import java.util.Date;

@Getter
@Setter
@Entity
public class Clube implements Serializable {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Integer id;
    @Column(length = 150)
    @NotEmpty(message = "O nome não pode ser nulo nem em branco")
    private String nome;
    private String estado;
    @Email
    @EmailValidation
    private String email;
    private String cnpj;
    @CPF
    private Date dataCriacao;
}

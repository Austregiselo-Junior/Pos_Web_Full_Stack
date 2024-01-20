package br.edu.unipe.pos.api.model;

import jakarta.persistence.*;
import jakarta.validation.constraints.NotEmpty;
import lombok.Getter;
import lombok.Setter;
import java.io.Serializable;

@Getter
@Setter
@Entity
public class Atleta implements Serializable {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Integer iD;

    @Column(length = 150)
    @NotEmpty()
    private String nome;

    private Integer anoNascimento;

    private String esporte;


}

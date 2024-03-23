package com.kamikase.web.posbackend.model;

import jakarta.persistence.*;
import lombok.Data;

@Data
@Entity
public class Esporte {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private long id;

    @Column(unique = true)
    private String nome;
}

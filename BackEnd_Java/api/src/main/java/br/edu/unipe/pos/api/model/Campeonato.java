package br.edu.unipe.pos.api.model;

import jakarta.persistence.Column;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.validation.constraints.NotEmpty;
import org.springframework.boot.autoconfigure.web.WebProperties;

import java.io.Serializable;

public class Campeonato implements Serializable {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Integer iD;

    @Column(length = 150)
    @NotEmpty
    private String time;
}

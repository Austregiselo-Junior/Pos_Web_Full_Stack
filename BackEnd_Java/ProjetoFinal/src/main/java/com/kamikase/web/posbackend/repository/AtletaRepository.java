package com.kamikase.web.posbackend.repository;

import com.kamikase.web.posbackend.model.Atleta;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface AtletaRepository
        extends JpaRepository<Atleta, Integer> {

    public List<Atleta> findByNomeOrderByNomeAsc(String nome);
}

package com.kamikase.web.posbackend.repository;

import com.kamikase.web.posbackend.model.Clube;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface ClubeRepository extends JpaRepository<Clube, Integer> {
    public List<Clube> findByNomeOrderByNomeAsc(String nome);

    @Query(value = "select a from Clube a where a.nome=:nome order by a.nome asc")
    public List<Clube> buscarNomeTime(@Param("nome") String nome);

}

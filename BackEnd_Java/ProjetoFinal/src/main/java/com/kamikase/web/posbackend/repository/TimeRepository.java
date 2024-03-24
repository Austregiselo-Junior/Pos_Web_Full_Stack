package com.kamikase.web.posbackend.repository;

import com.kamikase.web.posbackend.model.Clube;
import com.kamikase.web.posbackend.model.Time;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface TimeRepository extends JpaRepository<Time, Long > {

    @Query(value = "SELECT nome FROM Time ORDER BY nome ASC")
    public List<Time> buscarTodososNomesdeFomaAscendente();
}

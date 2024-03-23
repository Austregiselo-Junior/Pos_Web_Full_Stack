package com.kamikase.web.posbackend.repository;

import com.kamikase.web.posbackend.model.Esporte;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface EsporteRepository extends JpaRepository<Esporte, Long > {
}

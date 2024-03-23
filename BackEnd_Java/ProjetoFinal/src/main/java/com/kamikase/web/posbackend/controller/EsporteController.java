package com.kamikase.web.posbackend.controller;

import com.kamikase.web.posbackend.model.Esporte;
import com.kamikase.web.posbackend.service.EsporteService;
import lombok.AllArgsConstructor;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@AllArgsConstructor
@RestController
@RequestMapping("/esporte")
public class EsporteController {

    private EsporteService service;

    @PostMapping("/importar")
    public void importarEsportes(){
        service.importarEsportes();
    }

    @GetMapping
    public ResponseEntity<List<Esporte>> listarEsportes(){
        return ResponseEntity.ok(service.listarEsportes());
    }


}

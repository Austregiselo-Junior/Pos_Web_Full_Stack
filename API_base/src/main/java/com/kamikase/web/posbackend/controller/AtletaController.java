package com.kamikase.web.posbackend.controller;

import com.kamikase.web.posbackend.client.ViaCepClient;
import com.kamikase.web.posbackend.model.Atleta;
import com.kamikase.web.posbackend.model.dto.CepResponseDTO;
import com.kamikase.web.posbackend.service.AtletaService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;


@RestController
@RequestMapping("/atleta")
public class AtletaController {
    @Autowired
    private AtletaService service;

    @Autowired
    private ViaCepClient viaCepClient;

    @PostMapping
    public ResponseEntity<Atleta> cadastrar(@RequestBody Atleta atleta){
        atleta = service.cadastrar(atleta);
        return ResponseEntity.ok(atleta);
    }

    @PutMapping
    public ResponseEntity<Atleta> alterar(@RequestBody Atleta atleta){
        atleta = service.alterar(atleta);
        return ResponseEntity.ok(atleta);
    }

    @DeleteMapping("{id}")
    public ResponseEntity<Void> deletar(@PathVariable Integer id){
        service.deletar(id);
        return ResponseEntity.ok().build();
    }

    @GetMapping("{id}")
    public ResponseEntity<Atleta> consultarPorId(@PathVariable Integer id){
        return ResponseEntity.ok(service.consultarPorId(id));
    }

    @GetMapping
    public ResponseEntity<List<Atleta>> listarTodos(){
        return ResponseEntity.ok(service.listar());
    }

    @GetMapping("/nome/{nome}")
    public ResponseEntity<List<Atleta>> listarPorNome(@PathVariable String nome){
        return ResponseEntity.ok(service.listarPorNome(nome));
    }


    @GetMapping("/cep/{cep}")
    public ResponseEntity<CepResponseDTO> consultarCepAtleta(@PathVariable String cep){

        var cepResponse = viaCepClient.consultaCep(cep);

        return ResponseEntity.ok(cepResponse);
    }



}

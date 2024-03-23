package com.kamikase.web.posbackend.controller;

import com.kamikase.web.posbackend.client.ViaCepClient;
import com.kamikase.web.posbackend.model.Clube;
import com.kamikase.web.posbackend.model.dto.CepResponseDTO;
import com.kamikase.web.posbackend.service.ClubeService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/clube")
public class ClubeController {
    @Autowired
    private ClubeService clubeService;
    @Autowired
    private ViaCepClient viaCepClient;
    @PostMapping
    public ResponseEntity<Clube> cadastrar(@RequestBody Clube clube) {
        var newtime = clubeService.cadastrar(clube);
        return ResponseEntity.ok(newtime);
    }

    @PutMapping
    public ResponseEntity<Clube> alterar(@RequestBody Clube clube) {
        var updatedClube = clubeService.alterar(clube);
        return ResponseEntity.ok(updatedClube);
    }

    @GetMapping
    public ResponseEntity<List<Clube>> listarTodos() {
        return ResponseEntity.ok(clubeService.listar());
    }

    @GetMapping("{id}")
    public ResponseEntity<Clube> consultarPorId(@PathVariable Integer id) {
        return ResponseEntity.ok(clubeService.consultarPorId(id));
    }

    @GetMapping("/nome/{nome}")
    public ResponseEntity<List<Clube>> listarPorNome(@PathVariable String nome) {
        return ResponseEntity.ok(clubeService.listarPorNome(nome));
    }

    @DeleteMapping("/id/{id}")
    public ResponseEntity<Clube> delete(@PathVariable Integer id) {
        clubeService.deletar(id);
        return ResponseEntity.ok().build();
    }

    @GetMapping("/cep/{cep}")
    public ResponseEntity<CepResponseDTO> consultarCepAtleta(@PathVariable String cep){

        var cepResponse = viaCepClient.consultaCep(cep);

        return ResponseEntity.ok(cepResponse);
    }

}

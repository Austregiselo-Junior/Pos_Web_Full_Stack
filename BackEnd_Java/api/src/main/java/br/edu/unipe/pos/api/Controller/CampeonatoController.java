package br.edu.unipe.pos.api.Controller;

import br.edu.unipe.pos.api.Service.CampeonatoService;
import br.edu.unipe.pos.api.model.Campeonato;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Service;
import org.springframework.web.bind.annotation.*;

import java.util.Collections;
import java.util.List;

@RestController
@RequestMapping("/campeonato")
public class CampeonatoController {

    @Autowired
    private CampeonatoService service;

    @PostMapping
    public ResponseEntity<Campeonato> cadastrar(@RequestBody Campeonato campeonato){
        campeonato = service.cadastrar(campeonato);
        return ResponseEntity.ok(campeonato);
    }

    @PutMapping
    public ResponseEntity<Campeonato> alterar(@RequestBody Campeonato campeonato){
        campeonato = service.cadastrar(campeonato);
        return ResponseEntity.ok(campeonato);
    }

    @DeleteMapping
    public ResponseEntity<Void> deletar(@PathVariable Integer id){
        service.deletar(id);
        return ResponseEntity.ok().build();
    }

    @GetMapping
    public ResponseEntity<Void> listar(){
        service.listar();
        return ResponseEntity.ok().build();
    }

    @GetMapping("/nome/{nome}")
    public ResponseEntity<List<Campeonato>> listarPorNome(@PathVariable String nome){
        service.listarPorNome(nome);
       return ResponseEntity.ok().build();
    }

    @GetMapping("/id")
    public ResponseEntity<List<Campeonato>> consultarPorId(@PathVariable Integer id){
        return ResponseEntity.ok(Collections.singletonList(service.copnsultarPorId(id)));
    }
}

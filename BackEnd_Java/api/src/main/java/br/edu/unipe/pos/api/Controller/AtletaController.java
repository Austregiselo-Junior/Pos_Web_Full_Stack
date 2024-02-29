package br.edu.unipe.pos.api.Controller;

import br.edu.unipe.pos.api.Service.AtletaService;
import br.edu.unipe.pos.api.model.Atleta;
import br.edu.unipe.pos.api.model.Campeonato;
import br.edu.unipe.pos.api.model.Campeonato;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/atleta")
public class AtletaController {

    @Autowired
    private AtletaService service;

    @PostMapping
    public ResponseEntity<Atleta> cadastrar(@RequestBody Atleta atleta){
        atleta = service.cadastrar(atleta);
        return  ResponseEntity.ok(atleta);
    }

    @PutMapping
    public ResponseEntity<Atleta> alterar(@RequestBody Atleta atleta){
        atleta = service.cadastrar(atleta);
        return  ResponseEntity.ok(atleta);
    }

    @DeleteMapping
    public ResponseEntity<Void> deletar (@PathVariable Integer id){
        service.deletar(id);
        return ResponseEntity.ok().build();
    }

    @GetMapping
    public ResponseEntity<Void> listar (){
        service.listar();
        return ResponseEntity.ok().build();
    }

    @GetMapping("/nome/{nome}")
    public ResponseEntity<List<Atleta>> listarPorNome (@PathVariable String nome){
        service.listarPorNome(nome);
        return ResponseEntity.ok().build();
    }

    @GetMapping("{id}")
    public ResponseEntity<Atleta> consultarPorId(@PathVariable Integer id){
        return ResponseEntity.ok(service.consultarPorId(id));
    }
}

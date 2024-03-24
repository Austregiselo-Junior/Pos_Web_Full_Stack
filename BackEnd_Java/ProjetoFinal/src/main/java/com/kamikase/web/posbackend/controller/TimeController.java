package com.kamikase.web.posbackend.controller;

import com.kamikase.web.posbackend.model.Time;
import com.kamikase.web.posbackend.service.TimeService;
import lombok.AllArgsConstructor;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@AllArgsConstructor
@RestController
@RequestMapping("/time")
public class TimeController {

    private TimeService service;

    @PostMapping("/importar")
    public void importarTimes(){
        service.importarTimes();
    }

    @GetMapping
    public ResponseEntity<List<Time>> listarEsportes(){
        return ResponseEntity.ok(service.listarTimes());
    }

    @GetMapping("/ASC")
    public ResponseEntity<List<Time>> listarEsportesASC(){
        return ResponseEntity.ok(service.listarTimesPorOrdemAscendente());
    }


}

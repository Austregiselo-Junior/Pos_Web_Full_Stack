package com.kamikase.web.posbackend.service;

import com.kamikase.web.posbackend.model.Clube;
import com.kamikase.web.posbackend.repository.ClubeRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Objects;

@Service
public class ClubeService {
    @Autowired
    private ClubeRepository clubeRepository;

    public Clube cadastrar(Clube clube) {
        return clubeRepository.save(clube);
    }

    public List<Clube> listar() {
        return clubeRepository.findAll();
    }

    public List<Clube> listarPorNome(String nome) {
        return clubeRepository.findByNomeOrderByNomeAsc(nome);
    }

    public Clube consultarPorId(Integer id) {
        return clubeRepository.findById(id).orElseThrow(RuntimeException::new);
    }

    public Clube alterar(Clube clube) {
        if (Objects.isNull(clube.getId())) {
            throw new RuntimeException();
        }
        return clubeRepository.save(clube);
    }

    public void deletar(Integer id) {
        clubeRepository.deleteById(id);
    }
}

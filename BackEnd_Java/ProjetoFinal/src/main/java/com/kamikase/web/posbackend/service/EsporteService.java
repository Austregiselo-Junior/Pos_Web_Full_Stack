package com.kamikase.web.posbackend.service;

import com.kamikase.web.posbackend.client.EsporteClient;
import com.kamikase.web.posbackend.model.Esporte;
import com.kamikase.web.posbackend.model.dto.EsporteDTO;
import com.kamikase.web.posbackend.repository.EsporteRepository;
import lombok.AllArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.dao.DataIntegrityViolationException;
import org.springframework.stereotype.Service;

import java.util.List;

@AllArgsConstructor
@Slf4j
@Service
public class EsporteService {

    private EsporteRepository repository;
    private EsporteClient client;

    public List<Esporte> listarEsportes(){
        return repository.findAll();
    }

    public void importarEsportes(){
        log.info("Integração de esportes iniciada");
        List<EsporteDTO> listaEsporteIntegracao = client.listarEsporteIntegracao();
        for(EsporteDTO esporteDTO : listaEsporteIntegracao){
            var esporte = new Esporte();
            var nomeEsporte = esporteDTO.getCodigo() + " - " + esporteDTO.getNome();
            try {
                esporte.setNome(nomeEsporte);
                repository.save(esporte);
                log.info("Esporte {} integrado com sucesso", nomeEsporte);
            }catch (DataIntegrityViolationException e){
                log.info("Erro ao integrar esporte {}", nomeEsporte);
                log.error("ERRO VALOR DUPLICADO: {} ", e);
            } catch (Exception e){
                log.error("ERRO INESPERADO: {} ", e);
            }
        }
        log.info("Integração de esportes encerrada com sucesso");
    }

}

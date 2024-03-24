package com.kamikase.web.posbackend.service;

import com.kamikase.web.posbackend.client.TimeClient;
import com.kamikase.web.posbackend.model.Clube;
import com.kamikase.web.posbackend.model.Time;
import com.kamikase.web.posbackend.model.dto.TimeDTO;
import com.kamikase.web.posbackend.repository.TimeRepository;
import lombok.AllArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.dao.DataIntegrityViolationException;
import org.springframework.stereotype.Service;

import java.util.List;

@AllArgsConstructor
@Slf4j
@Service
public class TimeService {

    private TimeRepository repository;
    private TimeClient client;

    public List<Time> listarTimes(){
        return repository.findAll();
    }

    public List<Time> listarTimesPorOrdemAscendente(){
        return repository.buscarTodososNomesdeFomaAscendente();
    }

    public void importarTimes(){
        log.info("Integração de times iniciada");

        List<TimeDTO> listaTimeIntegracao = client.listarTimeIntegracao();
        ObterNomedoTime(listaTimeIntegracao);

        log.info("Integração de times encerrada com sucesso");
    }

    private void ObterNomedoTime(List<TimeDTO> listaTimeIntegracao) {
        for(TimeDTO timeDTO : listaTimeIntegracao){

            var time = new Time();
            var nomeTime = timeDTO.getCodigo() + " - " + timeDTO.getNome();

            try {

                time.setNome(nomeTime);
                repository.save(time);

                log.info("Time {} integrado com sucesso", nomeTime);
            }catch (DataIntegrityViolationException e){
                log.info("Erro ao integrar time {}", nomeTime);
                log.error("ERRO VALOR DUPLICADO: {} ", nomeTime);
            } catch (Exception e){
                log.error("ERRO INESPERADO: {} ", e.getMessage());
            }
        }
    }
}

package com.kamikase.web.posbackend.Client;

import com.kamikase.web.posbackend.model.Atleta;
import com.kamikase.web.posbackend.model.DTO.CepResponseDTO;
import org.springframework.cloud.openfeign.FeignClient;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;

import java.util.List;


@FeignClient(value = "atleta-gambi", url = "http://localhost:9090")
public interface AtletaClient {

    @GetMapping("/atleta/cep/{cep}")
    CepResponseDTO consultaCep(@PathVariable("cep") String cep);

    @GetMapping("/atleta")
    List<Atleta> listarAtleta();
}

package com.kamikase.web.posbackend.Client;

import com.kamikase.web.posbackend.model.DTO.CepResponseDTO;
import org.springframework.cloud.openfeign.FeignClient;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;


@FeignClient(value = "viacep", url = "https://viacep.com.br/ws/")
public interface ViaCepClient {

    @GetMapping("{cep}/json")
    CepResponseDTO consultaCep(@PathVariable("cep") String cep);

}

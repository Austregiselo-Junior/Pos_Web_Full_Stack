package com.kamikase.web.posbackend.client;



import com.kamikase.web.posbackend.model.dto.CepResponseDTO;
import org.springframework.cloud.openfeign.FeignClient;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;


@FeignClient(value = "viacep", url = "https://viacep.com.br/ws/")
public interface ViaCepClient {

    @GetMapping("{cep}/json")
    CepResponseDTO consultaCep(@PathVariable("cep") String cep);

}

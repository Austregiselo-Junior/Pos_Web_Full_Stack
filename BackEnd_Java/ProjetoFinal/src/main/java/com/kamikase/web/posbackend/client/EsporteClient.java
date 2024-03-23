package com.kamikase.web.posbackend.client;


import com.kamikase.web.posbackend.model.dto.EsporteDTO;
import org.springframework.cloud.openfeign.FeignClient;
import org.springframework.web.bind.annotation.GetMapping;

import java.util.List;

@FeignClient(value = "esporte-integration", url = "http://localhost:9090/esporte")
public interface EsporteClient {

    @GetMapping
    public List<EsporteDTO> listarEsporteIntegracao();

    @GetMapping("/disponiveis")
    public List<EsporteDTO> listarCodigosDisponiveis();


}

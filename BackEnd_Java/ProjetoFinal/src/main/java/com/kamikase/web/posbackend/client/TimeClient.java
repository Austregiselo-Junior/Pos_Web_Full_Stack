package com.kamikase.web.posbackend.client;


import com.kamikase.web.posbackend.model.dto.TimeDTO;
import org.springframework.cloud.openfeign.FeignClient;
import org.springframework.web.bind.annotation.GetMapping;

import java.util.List;

@FeignClient(value = "time-integration", url = "http://localhost:9090/time")
public interface TimeClient {

    @GetMapping
    public List<TimeDTO> listarTimeIntegracao();

    @GetMapping("/disponiveis")
    public List<TimeDTO> listarCodigosDisponiveis();


}

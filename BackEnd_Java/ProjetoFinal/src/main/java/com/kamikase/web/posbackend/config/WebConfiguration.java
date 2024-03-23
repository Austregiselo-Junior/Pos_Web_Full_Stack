package com.kamikase.web.posbackend.config;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.web.servlet.config.annotation.CorsRegistry;
import org.springframework.web.servlet.config.annotation.WebMvcConfigurer;

@Configuration
public class WebConfiguration {

    @Bean
    public WebMvcConfigurer webMvcConfigurer() {
        return new WebMvcConfigurer() {
            @Override
            public void addCorsMappings(CorsRegistry registry) {
                registry
                        .addMapping("/**")
                        .allowedOrigins("*","http://localhost:4200")
                        .allowedHeaders("*", "Authorization", "Content-Type", "Accept")
                        //.allowedHeaders("*") para geral
                        .allowedMethods("GET", "POST", "PUT", "DELETE");
            }

        };
    }
}
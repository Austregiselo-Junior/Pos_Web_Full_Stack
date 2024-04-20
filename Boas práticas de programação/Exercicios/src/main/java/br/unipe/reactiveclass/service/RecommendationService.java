package br.unipe.reactiveclass.service;

import br.unipe.reactiveclass.model.Book;
import reactor.core.publisher.Flux;
import reactor.core.scheduler.Schedulers;

import java.time.Duration;

public class RecommendationService {
    private final Schedulers schedulers;

    public RecommendationService(Schedulers schedulers) {
        this.schedulers = schedulers;
    }

    public Flux<Book> getRecommendations(Long bookId) {
        return Flux.range(1, 100) // Simula 100 recomendações
                .map(this::createRecommendation)
                .delayElements(Duration.ofMillis(1)) // Simula um produtor rápido
                .subscribeOn(schedulers.boundedElastic());
    }

    private Book createRecommendation(int id) {
        // Simula a criação de uma recomendação.
        return new Book((long) id, "Book Title " + id, "Author " + id);
    }
}

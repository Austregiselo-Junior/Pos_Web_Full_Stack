package br.unipe.reactiveclass.controller;

// Controlador REST (Exemplo: BookController.java)
import br.unipe.reactiveclass.dto.BookInfoWithRecommendationsDTO;
import br.unipe.reactiveclass.model.Book;
import br.unipe.reactiveclass.repository.BookRepository;
import br.unipe.reactiveclass.service.RecommendationService;
import lombok.AllArgsConstructor;
import org.springframework.web.bind.annotation.*;
import reactor.core.publisher.BufferOverflowStrategy;
import reactor.core.publisher.Flux;
import reactor.core.publisher.Mono;

import java.util.Collections;

@RestController
@RequestMapping("/books")
@AllArgsConstructor
public class BookController {

    private final RecommendationService recommendationService;
    private final BookRepository bookRepository;


    // Endpoint para buscar todos os livros
    @GetMapping
    public Flux<Book> getAllBooks() {
        return bookRepository.findAll();
    }

    // Endpoint para buscar um livro por ID
    @GetMapping("/{id}")
    public Mono<Book> getBookById(@PathVariable Long id) {
        return bookRepository.findById(id);
    }

    // Endpoint para adicionar um novo livro
    @PostMapping
    public Mono<Book> addBook(@RequestBody Book book) {
        return bookRepository.save(book);
    }

    // Endpoint para atualizar um livro existente
    @PutMapping("/{id}")
    public Mono<Book> updateBook(@PathVariable Long id, @RequestBody Book book) {
        return bookRepository.findById(id)
                .flatMap(existingBook -> {
                    existingBook.setTitle(book.getTitle());
                    existingBook.setAuthor(book.getAuthor());
                    return bookRepository.save(existingBook);
                })
                .switchIfEmpty(Mono.error(new RuntimeException("Livro não encontrado com o ID: " + id)));
    }

    // Endpoint para excluir um livro por ID
    @DeleteMapping("/{id}")
    public Mono<Void> deleteBook(@PathVariable Long id) {
        return bookRepository.deleteById(id);
    }


    @GetMapping("/books/{id}/recommendations")
    public Mono<BookInfoWithRecommendationsDTO> getBookWithRecommendations(@PathVariable Long id) {
        return bookRepository.findById(id)
                .flatMap(book -> recommendationService.getRecommendations(book.getId())
                        .onBackpressureBuffer(10) // Bufferiza até 10 itens
                        .collectList()
                        .map(recommendations -> new BookInfoWithRecommendationsDTO(book, recommendations)));
    }

    @GetMapping("/books/{id}/recommendations/error-handling")
    public Mono<BookInfoWithRecommendationsDTO> getBookWithRecommendationsExpcetion(@PathVariable Long id) {
        return bookRepository.findById(id)
                .flatMap(book -> recommendationService.getRecommendations(book.getId())
                        .onBackpressureBuffer(10,
                                BufferOverflowStrategy.DROP_OLDEST) // Define a estratégia de overflow
                        .collectList()
                        .map(recommendations -> new BookInfoWithRecommendationsDTO(book, recommendations)))
                .onErrorResume(e -> Mono.just(new BookInfoWithRecommendationsDTO(new Book(id, "Unknown", "Unknown"), Collections.emptyList()))); // Tratamento simplificado de erro
    }
}

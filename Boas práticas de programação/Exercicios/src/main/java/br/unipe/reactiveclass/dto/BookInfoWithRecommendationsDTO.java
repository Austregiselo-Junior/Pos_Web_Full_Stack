package br.unipe.reactiveclass.dto;


import br.unipe.reactiveclass.model.Book;
import lombok.AllArgsConstructor;
import lombok.Data;

import java.util.List;

@Data
@AllArgsConstructor
public class BookInfoWithRecommendationsDTO {
    private final Book book;
    private final List<Book> recommendations;
}

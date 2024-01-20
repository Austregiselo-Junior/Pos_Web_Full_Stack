package br.edu.unipe.pos.api.Repository;

import br.edu.unipe.pos.api.model.Atleta;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;

import java.util.List;

public interface AtletaRepository extends JpaRepository<Atleta, Integer>{

    public List<Atleta> findByNomeOrderByNomeAsc(String nome); // Query com minemonico, pega de acordo com a key passada acima.

    @Query(value = "select a from Atleta a where a.nome=:nome order by a.nome asc") //Query feita por JPQL
    public List<Atleta> buscvarNomeAtleta(String nome); // Pesquisar por nome
}

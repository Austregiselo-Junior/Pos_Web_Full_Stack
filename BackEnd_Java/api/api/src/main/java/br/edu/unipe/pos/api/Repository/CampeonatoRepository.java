package br.edu.unipe.pos.api.Repository;

import br.edu.unipe.pos.api.model.Campeonato;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import java.util.List;

public interface CampeonatoRepository extends JpaRepository<Campeonato, Integer> {

    public List<Campeonato> findByNomeOrderByNomeAsc(String time); // Query com minemonico, pega de acordo com a key passada acima.

    @Query(value = "select a from Campeonato a where a.time=:time order by a.time asc") //Query feita por JPQL
    public List<Campeonato> buscvarNomeCampeonato(String time); // Pesquisar por nome
}

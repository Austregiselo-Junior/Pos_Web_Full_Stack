package br.edu.unipe.pos.api.Repository;

import br.edu.unipe.pos.api.model.Atleta;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;

import java.net.InterfaceAddress;
import java.net.InterfaceAddress;
import java.util.List;

public interface AtletaRepository extends JpaRepository<Atleta, Integer>{

    public List<Atleta> findByNomeOrderByNomeAsc(String nome); // Query com minemonico, pega de acordo com a key passada acima.

    @Query(value = "select a from Atleta a where a.nome=:nome order by a.nome asc") //Query feita por JPQL
    public List<Atleta> buscvarNomeAtleta(String nome); // Pesquisar por nome
}

/*JPQL: JPQL é a sigla para Java Persistence Query Language. É uma linguagem de consulta poderosa que permite definir
consultas de banco de dados com base no modelo de entidade. A estrutura e a sintaxe do JPQL são muito semelhantes ao SQL.
No entanto, há uma diferença importante que você deve ter em mente: o JPQL usa o modelo de objeto de entidade
em vez de tabelas de banco de dados para definir uma consulta. Isso torna muito confortável para nós, desenvolvedores Java,
mas você deve ter em mente que o banco de dados ainda usa SQL. O Hibernate, ou qualquer outra implementação JPA,
tem que transformar a consulta JPQL em SQL.
*/


/*JPQL: JPQL é a sigla para Java Persistence Query Language. É uma linguagem de consulta poderosa que permite definir
consultas de banco de dados com base no modelo de entidade. A estrutura e a sintaxe do JPQL são muito semelhantes ao SQL.
No entanto, há uma diferença importante que você deve ter em mente: o JPQL usa o modelo de objeto de entidade
em vez de tabelas de banco de dados para definir uma consulta. Isso torna muito confortável para nós, desenvolvedores Java,
mas você deve ter em mente que o banco de dados ainda usa SQL. O Hibernate, ou qualquer outra implementação JPA,
tem que transformar a consulta JPQL em SQL.
*/


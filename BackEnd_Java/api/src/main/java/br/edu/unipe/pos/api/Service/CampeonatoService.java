package br.edu.unipe.pos.api.Service;

import br.edu.unipe.pos.api.Repository.CampeonatoRepository;
import br.edu.unipe.pos.api.model.Atleta;
import br.edu.unipe.pos.api.model.Campeonato;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Objects;

@Service
public class CampeonatoService {

    @Autowired
private CampeonatoRepository repository;

    public Campeonato cadastrar(Campeonato campeonato){return repository.save(campeonato);}
    public List<Campeonato> listar(){return repository.findAll();}
    public  List<Campeonato>listarPorNome(String time){return repository.findByNomeOrderByNomeAsc(time);}
    public void deletar(Integer id){repository.deleteById(id);}
    public Campeonato copnsultarPorId(Integer id){return repository.findById(id).get();}

    public Campeonato alterar(Campeonato campeonato)
    {
        if (Objects.isNull(campeonato.getID()))
        {
            throw new RuntimeException();
        }
        return repository.save(campeonato);
    }


}

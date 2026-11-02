using System.Collections.ObjectModel;
using System.ComponentModel.DataAnnotations;

namespace ASoftwareVersaoFisioterapiaAPI.Model
{
    public class Usuario
    {
        public int UsuarioId { get; set; }

        [Required]
        [StringLength(50, ErrorMessage = "Login grande, tente um menor")]
        public string Login { get; set; }

        [Required]
        [StringLength(12, ErrorMessage = "Senha grande, tente uma menor")]
        public string Senha { get; set; }

        [Required]
        public DateTime DataDoCadastro { get; set; }

        [Required]
        public DateTime? UltimaAtualizacao { get; set; }

        public ICollection<Cliente>? Clientes { get; set; }

        public Usuario()
        {
            Clientes = new Collection<Cliente>();
        }
    }
}
using Microsoft.EntityFrameworkCore.Migrations;

#nullable disable

namespace ASoftwareVersaoFisioterapiaAPI.Migrations
{
    /// <inheritdoc />
    public partial class PopulaClientes : Migration
    {
        /// <inheritdoc />
        protected override void Up(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.Sql("Insert into Clientes(Nome, Telefone, DataDaConsulta, DataDoCadastro, UltimaAtualizacao, UsuarioId, CategoriaId)" +
"values('Austregíselo Junior', '83998900000', now(), now(), now(), '1', '1')");

            migrationBuilder.Sql("Insert into Clientes(Nome, Telefone, DataDaConsulta, DataDoCadastro, UltimaAtualizacao, UsuarioId, CategoriaId)" +
     "values('Thiago', '83998900000', DATE_ADD(now(), INTERVAL 2 HOUR), now(), now(), '1', '2')");
        }

        /// <inheritdoc />
        protected override void Down(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.Sql("Delete from Clientes");
        }
    }
}
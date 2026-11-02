using Microsoft.EntityFrameworkCore.Migrations;

#nullable disable

namespace ASoftwareVersaoFisioterapiaAPI.Migrations
{
    /// <inheritdoc />
    public partial class PopulaCategoria : Migration
    {
        /// <inheritdoc />
        protected override void Up(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.Sql("Insert into Categorias(Nome, ValorDaSessao, QuantidadeDeSessao, ValorTotal, Desconto, ValorPago, Vencimento, SituacaoFinanceira, UltimaAtualizacao)" +
   "values('Mensal', '150.00' ,'4', '600.00', '0.2', '480.00', '12', 'Pago', now())");

            migrationBuilder.Sql("Insert into Categorias(Nome, ValorDaSessao, QuantidadeDeSessao, ValorTotal, Desconto, ValorPago, Vencimento, SituacaoFinanceira, UltimaAtualizacao)" +
   "values('Sessao', '200.00' ,'6', '1200.00', '0', '1200.00', '15', 'Pago', now())");
        }

        /// <inheritdoc />
        protected override void Down(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.Sql("Delete from Categorias");
        }
    }
}
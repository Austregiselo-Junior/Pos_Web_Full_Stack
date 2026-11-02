using Microsoft.EntityFrameworkCore.Migrations;

#nullable disable

namespace ASoftwareVersaoFisioterapiaAPI.Migrations
{
    /// <inheritdoc />
    public partial class RemoveRequiredFromValorPago : Migration
    {
        /// <inheritdoc />
        protected override void Up(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.AlterColumn<float>(
                name: "ValorPago",
                table: "Clientes",
                type: "float",
                nullable: true,
                oldClrType: typeof(float),
                oldType: "float");
        }

        /// <inheritdoc />
        protected override void Down(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.AlterColumn<float>(
                name: "ValorPago",
                table: "Clientes",
                type: "float",
                nullable: false,
                defaultValue: 0f,
                oldClrType: typeof(float),
                oldType: "float",
                oldNullable: true);
        }
    }
}

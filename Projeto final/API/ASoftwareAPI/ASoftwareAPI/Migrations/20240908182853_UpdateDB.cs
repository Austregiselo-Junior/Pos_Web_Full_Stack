using System;
using Microsoft.EntityFrameworkCore.Metadata;
using Microsoft.EntityFrameworkCore.Migrations;

#nullable disable

namespace ASoftwareVersaoFisioterapiaAPI.Migrations
{
    /// <inheritdoc />
    public partial class UpdateDB : Migration
    {
        /// <inheritdoc />
        protected override void Up(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DropForeignKey(
                name: "FK_Clientes_Categorias_CategoriaId",
                table: "Clientes");

            migrationBuilder.DropTable(
                name: "Categorias");

            migrationBuilder.DropIndex(
                name: "IX_Clientes_CategoriaId",
                table: "Clientes");

            migrationBuilder.DropColumn(
                name: "CategoriaId",
                table: "Clientes");

            migrationBuilder.AddColumn<string>(
                name: "Categoria",
                table: "Clientes",
                type: "varchar(50)",
                maxLength: 50,
                nullable: false,
                defaultValue: "")
                .Annotation("MySql:CharSet", "utf8mb4");

            migrationBuilder.AddColumn<float>(
                name: "Desconto",
                table: "Clientes",
                type: "float",
                nullable: false,
                defaultValue: 0f);

            migrationBuilder.AddColumn<int>(
                name: "QuantidadeDeSessao",
                table: "Clientes",
                type: "int",
                nullable: false,
                defaultValue: 0);

            migrationBuilder.AddColumn<string>(
                name: "SituacaoFinanceira",
                table: "Clientes",
                type: "varchar(80)",
                maxLength: 80,
                nullable: false,
                defaultValue: "")
                .Annotation("MySql:CharSet", "utf8mb4");

            migrationBuilder.AddColumn<float>(
                name: "ValorDaSessao",
                table: "Clientes",
                type: "float",
                nullable: false,
                defaultValue: 0f);

            migrationBuilder.AddColumn<float>(
                name: "ValorPago",
                table: "Clientes",
                type: "float",
                nullable: false,
                defaultValue: 0f);

            migrationBuilder.AddColumn<float>(
                name: "ValorTotal",
                table: "Clientes",
                type: "float",
                nullable: false,
                defaultValue: 0f);

            migrationBuilder.AddColumn<string>(
                name: "Vencimento",
                table: "Clientes",
                type: "longtext",
                nullable: false)
                .Annotation("MySql:CharSet", "utf8mb4");
        }

        /// <inheritdoc />
        protected override void Down(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DropColumn(
                name: "Categoria",
                table: "Clientes");

            migrationBuilder.DropColumn(
                name: "Desconto",
                table: "Clientes");

            migrationBuilder.DropColumn(
                name: "QuantidadeDeSessao",
                table: "Clientes");

            migrationBuilder.DropColumn(
                name: "SituacaoFinanceira",
                table: "Clientes");

            migrationBuilder.DropColumn(
                name: "ValorDaSessao",
                table: "Clientes");

            migrationBuilder.DropColumn(
                name: "ValorPago",
                table: "Clientes");

            migrationBuilder.DropColumn(
                name: "ValorTotal",
                table: "Clientes");

            migrationBuilder.DropColumn(
                name: "Vencimento",
                table: "Clientes");

            migrationBuilder.AddColumn<int>(
                name: "CategoriaId",
                table: "Clientes",
                type: "int",
                nullable: true);

            migrationBuilder.CreateTable(
                name: "Categorias",
                columns: table => new
                {
                    CategoriaId = table.Column<int>(type: "int", nullable: false)
                        .Annotation("MySql:ValueGenerationStrategy", MySqlValueGenerationStrategy.IdentityColumn),
                    Desconto = table.Column<float>(type: "float", nullable: false),
                    Nome = table.Column<string>(type: "varchar(50)", maxLength: 50, nullable: false)
                        .Annotation("MySql:CharSet", "utf8mb4"),
                    QuantidadeDeSessao = table.Column<int>(type: "int", nullable: false),
                    SituacaoFinanceira = table.Column<string>(type: "varchar(80)", maxLength: 80, nullable: false)
                        .Annotation("MySql:CharSet", "utf8mb4"),
                    UltimaAtualizacao = table.Column<DateTime>(type: "datetime(6)", nullable: false),
                    ValorDaSessao = table.Column<float>(type: "float", nullable: false),
                    ValorPago = table.Column<float>(type: "float", nullable: false),
                    ValorTotal = table.Column<float>(type: "float", nullable: false),
                    Vencimento = table.Column<string>(type: "longtext", nullable: false)
                        .Annotation("MySql:CharSet", "utf8mb4")
                },
                constraints: table =>
                {
                    table.PrimaryKey("PK_Categorias", x => x.CategoriaId);
                })
                .Annotation("MySql:CharSet", "utf8mb4");

            migrationBuilder.CreateIndex(
                name: "IX_Clientes_CategoriaId",
                table: "Clientes",
                column: "CategoriaId");

            migrationBuilder.AddForeignKey(
                name: "FK_Clientes_Categorias_CategoriaId",
                table: "Clientes",
                column: "CategoriaId",
                principalTable: "Categorias",
                principalColumn: "CategoriaId");
        }
    }
}

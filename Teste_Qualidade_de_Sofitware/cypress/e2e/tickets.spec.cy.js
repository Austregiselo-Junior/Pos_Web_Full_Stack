/// <reference types= "cypress"/>
import ticketsPage from "../Pages/Tickets/TicketsPage";
describe("Teste de Tickets", () => {

    beforeEach (() => cy.visit("https://ticket-box.s3.eu-central-1.amazonaws.com/index.html"))

    it("TC01 - Imput First and Last Name", () => {
        const firstName = "Astro";
        const lastName = "Jr";
        const fullName = `${firstName} ${lastName}`;

        cy.get("#first-name").type(firstName); // Pegando por id
        cy.get("#last-name").type(lastName);
        cy.get(".agreement p").should('contain', `I, ${fullName}, wish to buy`); // Pesquisa pelo qiue a frase tem

    })

        it("TC02 - Compra de ingresso", () => {
        const firstName = "Astro";
        const lastName = "Jr";
        const fullName = `${firstName} ${lastName}`;
        const email = "teste@gmail.com";
        const textfull = "Lorem alguma coisa...";

        cy.get("#first-name").type(firstName); // Pegando por id
        cy.get("#last-name").type(lastName);
        cy.get("#email").type(email);
        cy.get("#ticket-quantity").select("2");
        cy.get("#vip").check();
        cy.get("#publication").check();
        cy.get("#requests").type(textfull, {delay: 0}); // teste com o dalay de 0 sec para iniciar o teste

        cy.get(".agreement p").should('contain', `I, ${fullName}, wish to buy`); // Pesquisa pelo qiue a frase tem

        cy.get("#agree").check();
        cy.get("#signature").type(fullName, {delay: 0});
        cy.get("button[type='submit']").click(); // Busca pelo tipo, no caso unm botão submit

        cy.get(".success").should("be.visible");
        cy.get(".success").should("have.text", "Ticket(s) successfully ordered.");
    })

        it.only("TC03 - Compra de ingresso otimizado", () => {
       
        cy.fillMandatoryFields();
        ticketsPage.Success.should("be.visible");
        ticketsPage.Success.should("have.text", "Ticket(s) successfully ordered.");
    })
})
/// <reference types="cypress"/>

describe("Teste da API Viacep", () => {
      it("Requisição Get com CEP válido", () => {
        cy.request("viacep.com.br/ws/01001000/json").should(function(response){
        const {status, statusText} = response;
        expect(status).to.be.equal(200)
        expect(statusText).to.be.equal("OK");
      })
    })

     it("Requisição Get com CEP inválido", () => {
        cy.request({
            url:"viacep.com.br/ws/010010003/json",
            failOnStatusCode: false
        }).should(function(response){
        const {status, statusText} = response;
        expect(status).to.be.equal(400)
        expect(statusText).to.be.equal("Bad Request");
      })
    })

       it("Requisição Get com CEP inválido com ultimo igual a T", () => {
        cy.request({
            url:"viacep.com.br/ws/0100100T/json",
            failOnStatusCode: false
        }).should(function(response){
        const {status, statusText} = response;
        expect(status).to.be.equal(400)
        expect(statusText).to.be.equal("Bad Request");
      })
    })
})
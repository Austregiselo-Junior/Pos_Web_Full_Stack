/// <reference types="cypress"/>

describe("Teste do back", () => {
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

    it("Req POST", () => {
        cy.request({
            method: 'POST', url: 'https://httpbin.org/post',
            body:
            {
                name: 'Astro', age: '30'
            }
        }).should(function (response){
            const {status, statusText} = response;
            expect(status).to.be.equal(200)
            expect(statusText).to.be.equal("OK");
        })
    })

        it("Req POST 2", () => {
        cy.request({
            method: 'POST', url: 'https://httpbin.org/post',
            body:
            {
                name: 'Astro', age: '30'
            }
        }).its('body').should('not.be.empty') // Esse .its, a pessoa consegue recuperar o resoluado da requisição, nesse caso o bady.
        })
})


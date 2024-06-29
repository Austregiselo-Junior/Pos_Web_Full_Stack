/// <reference types="cypress"/>

describe("Teste do back", () => {
      it("Requisição Get", () => {
        cy.request("https://httpbin.org/get").should(function(response){
        const {status, statusText} = response;
        expect(status).to.be.equal(200)
        expect(statusText).to.be.equal("OK");
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


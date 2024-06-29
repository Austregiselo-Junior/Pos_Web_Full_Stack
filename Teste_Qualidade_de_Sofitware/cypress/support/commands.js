// ***********************************************
// This example commands.js shows you how to
// create various custom commands and overwrite
// existing commands.
//
// For more comprehensive examples of custom
// commands please read more here:
// https://on.cypress.io/custom-commands
// ***********************************************
//
//
// -- This is a parent command --
// Cypress.Commands.add('login', (email, password) => { ... })
//
//
// -- This is a child command --
// Cypress.Commands.add('drag', { prevSubject: 'element'}, (subject, options) => { ... })
//
//
// -- This is a dual command --
// Cypress.Commands.add('dismiss', { prevSubject: 'optional'}, (subject, options) => { ... })
//
//
// -- This will overwrite an existing command --
// Cypress.Commands.overwrite('visit', (originalFn, url, options) => { ... })

import ticketsPage from "../Pages/Tickets/TicketsPage"

Cypress.Commands.add("fillMandatoryFields", data =>{
    cy.fixture("user.json").then((user) => {
        ticketsPage.FirstName.type(user.firstName);
        ticketsPage.LastName.type(user.lastName);
        ticketsPage.Email.type(user.email);
    })

    ticketsPage.Agree.check();
    ticketsPage.SubmitButton.click();
})
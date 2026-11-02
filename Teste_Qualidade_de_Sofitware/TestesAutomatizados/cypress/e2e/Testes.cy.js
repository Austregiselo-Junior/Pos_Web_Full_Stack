describe("Funcionalidade: Registro de Usuário.", () => {

    it("Cenário 2", () => {
        const emailAdress = "csfsedfsd";

        cy.visit("http://www.automationpractice.pl/index.php?controller=authentication&back=my-account#account-creation");
        cy.get("#email_create").type(emailAdress);
        cy.get("#SubmitCreate").click();
       
        cy.get("#create_account_error").should('contain', `Invalid email address.`); 
    })

    it("Cenário 3", () => {
   
       const emailAdress = "austregiselo@gmail.com";
       const password = "12345";

        cy.visit("http://www.automationpractice.pl/index.php?controller=authentication&back=my-account#account-creation");
        cy.get("#email_create").type(emailAdress);
        cy.get("#SubmitCreate").click();

        cy.get("#customer_firstname").type('{backspace}');
        cy.get("#customer_lastname").type('{backspace}');
      
        cy.get("#passwd").type(password);
        cy.get("#submitAccount").click();
       
        cy.get(".alert-danger").should('contain', `There are 2 errors`); 
    })
})

describe("Funcionalidade: Pesquisa e Visualização de Produtos.", () => {
    it("Cenário 1", () => {
        const title = "Faded Short Sleeve T-shirts";

        cy.visit("http://www.automationpractice.pl/index.php");
        cy.get("#search_query_top").type(title);
        cy.get("#searchbox").click();
    })

       it("Cenário 2", () => {
        const title = "wedweded";

        cy.visit("http://www.automationpractice.pl/index.php");
        cy.get("#search_query_top").type(title);
        cy.get("#searchbox").click();
    })
})

describe("Adição de Itens ao Carrinho de Compras.", () => {
 

    it("Cenário 2", () => {
        
        cy.visit("http://www.automationpractice.pl/index.php?controller=order");
      
        cy.get('.alert-warning').should('contain', `Your shopping cart is empty.`)
    })

    it("Cenário 1", () => {
        
        cy.visit("http://www.automationpractice.pl/index.php?id_product=2&controller=product#/1-size-s/8-color-white");
        cy.get("#add_to_cart").click();

        cy.get('#layer_cart').should('contain', `Product successfully added to your shopping cart
				`)
    })
})

describe("Finalização de Compra.", () => {
    it("Cenário 3", () => {
        cy.visit("http://www.automationpractice.pl/index.php?controller=address&back=order.php%3Fstep%3D1&select_address=1");
        cy.get("#email").type("austregiselojunior@gmail.com");
        cy.get("#passwd").type("12345");
        cy.get("#SubmitLogin").click();
        cy.contains('Add a new address').click();
     
        cy.get("#company").type("OK");
        cy.get("#address1").type("Rua piririparara");
        cy.get("#address2").type("Rua piririparara");
        cy.get("#city").type("Boston");
        cy.get('select[name="id_state"]').select('California');
        cy.get("#postcode").type("123x");
        cy.get("#phone").type("83990005020");
        cy.get("#alias").type("Casa");
        cy.get("#submitAddress").click();


    
     
    })

    it("Cenário 4", () => {
         cy.visit("http://www.automationpractice.pl/index.php?controller=address&back=order.php%3Fstep%3D1&select_address=1");
        cy.get("#email").type("austregiselojunior@gmail.com");
        cy.get("#passwd").type("12345");
        cy.get("#SubmitLogin").click();
        cy.contains('Add a new address').click();
     
        cy.get("#company").type("OK");
        cy.get("#address1").type("Rua piririparara");
        cy.get("#address2").type("Rua piririparara");
        cy.get("#city").type("Boston");
        cy.get('select[name="id_state"]').select('California');
        cy.get("#postcode").type("123x");
        cy.get("#phone").type("83990005020");
        cy.get("#alias").type("Casa");
        cy.get("#submitAddress").click();
        
        cy.get('.alert-danger').should('contain', `There is 1 error`)
    })
})
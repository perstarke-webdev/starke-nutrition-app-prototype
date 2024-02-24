describe('Coach page', () => {

  it('Header contains the correct text', () => {

    cy.visit('http://localhost:9000/#/coach')

    cy.get("[data-test='hero-heading']").contains("Starke Nutrition Coaching (Prototype)")

    cy.get("[data-test='hero-subheading']").contains("Meal-planning")

  })


  it('Nutritional table displays 0 for all values at first', () => {

    cy.visit('http://localhost:9000/#/coach')

    cy.get("[data-test='input']").eq(0).invoke('val').should('eq', '0');
    cy.get("[data-test='input']").eq(1).invoke('val').should('eq', '0');
    cy.get("[data-test='input']").eq(2).invoke('val').should('eq', '0');
    cy.get("[data-test='input']").eq(3).invoke('val').should('eq', '0');

  })


   it.only('Nutritional table displays inputted values', () => {

      cy.visit('http://localhost:9000/#/coach')

      // Input a number into the q-input element
      const inputNumber = 500; // The number you want to test
      cy.get("[data-test='input']").eq(0).type(inputNumber);

      // Verify that the inputted number is displayed
      cy.get("[data-test='input']").eq(0)
        .invoke('val')
        .should('eq', inputNumber.toString());


      // Input a number into the q-input element
      const inputNumber2 = 50; // The number you want to test
      cy.get("[data-test='input']").eq(1).type(inputNumber2);

      // Verify that the inputted number is displayed
      cy.get("[data-test='input']").eq(1)
        .invoke('val')
        .should('eq', inputNumber2.toString());


      // Input a number into the q-input element
      cy.get("[data-test='input']").eq(2).type(inputNumber2);

      // Verify that the inputted number is displayed
      cy.get("[data-test='input']").eq(2)
        .invoke('val')
        .should('eq', inputNumber2.toString());



      // Input a number into the q-input element
      const inputNumber3 = 10; // The number you want to test
      cy.get("[data-test='input']").eq(3).type(inputNumber3);

      // Verify that the inputted number is displayed
      cy.get("[data-test='input']").eq(3)
        .invoke('val')
        .should('eq', inputNumber3.toString());

     })


})

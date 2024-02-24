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


   it('Nutritional table displays inputted values', () => {

      cy.visit('http://localhost:9000/#/coach')

      // Input a number into the q-input element
      const inputNumber = 500; // The number you want to test
      cy.get("[data-test='input']").eq(0).clear().type(inputNumber);

      // Verify that the inputted number is displayed
      cy.get("[data-test='input']").eq(0)
        .invoke('val')
        .should('eq', inputNumber.toString());


      // Input a number into the q-input element
      const inputNumber2 = 50; // The number you want to test
      cy.get("[data-test='input']").eq(1).clear().type(inputNumber2);

      // Verify that the inputted number is displayed
      cy.get("[data-test='input']").eq(1)
        .invoke('val')
        .should('eq', inputNumber2.toString());


      // Input a number into the q-input element
      cy.get("[data-test='input']").eq(2).clear().type(inputNumber2);

      // Verify that the inputted number is displayed
      cy.get("[data-test='input']").eq(2)
        .invoke('val')
        .should('eq', inputNumber2.toString());



      // Input a number into the q-input element
      const inputNumber3 = 10; // The number you want to test
      cy.get("[data-test='input']").eq(3).clear().type(inputNumber3);

      // Verify that the inputted number is displayed
      cy.get("[data-test='input']").eq(3)
        .invoke('val')
        .should('eq', inputNumber3.toString());

     })


   it.only('Button submit returns a matching recipe and displays it correctly', () => {

      cy.visit('http://localhost:9000/#/coach')

      // Enter values
      cy.get("[data-test='input']").eq(0).clear().type(500);
      cy.get("[data-test='input']").eq(1).clear().type(50);
      cy.get("[data-test='input']").eq(2).clear().type(50);
      cy.get("[data-test='input']").eq(3).clear().type(10);

      // Click submit button
      cy.get("[data-test='submit-btn']").click();

      // Get the recipe image element
      cy.get("[data-test='recipe-img']")
        .find("img")
        .should(($img) => {
          // Image src contains correct link
          assert.include($img.attr('src'), 'https://spoonacular.com/recipeImages/');
        });


    // Check if received and displayed nutrients are within 10% range of the given ones

    cy.get("[data-test='received-nutrients']").should(($el) => {
      const textContent = $el.text();
      const values = textContent.match(/\d+/g); // Extract numerical values from the text
      const expectedKcal = 500;
      const expectedProteins = 50;
      const expectedCarbs = 50;
      const expectedFats = 10;

      // Check if the displayed values are within 10% range of the expected values
      expect(parseInt(values[0])).to.be.at.least(expectedKcal * 0.9); // Lower bound
      expect(parseInt(values[0])).to.be.at.most(expectedKcal * 1.1); // Upper bound
      expect(parseInt(values[1])).to.be.at.least(expectedProteins * 0.9); // Lower bound
      expect(parseInt(values[1])).to.be.at.most(expectedProteins * 1.1); // Upper bound
      expect(parseInt(values[2])).to.be.at.least(expectedCarbs * 0.9); // Lower bound
      expect(parseInt(values[2])).to.be.at.most(expectedCarbs * 1.1); // Upper bound
      expect(parseInt(values[3])).to.be.at.least(expectedFats * 0.9); // Lower bound
      expect(parseInt(values[3])).to.be.at.most(expectedFats * 1.1); // Upper bound
    });



   })


})

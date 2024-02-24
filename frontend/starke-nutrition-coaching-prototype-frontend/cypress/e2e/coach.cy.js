describe('Coach page', () => {

  it('Header contains the correct text', () => {

    cy.visit('http://localhost:9000/#/coach')

    cy.get("[data-test='hero-heading']").contains("Starke Nutrition Coaching (Prototype)")

    cy.get("[data-test='hero-subheading']").contains("Meal-planning")

  })

  it.only('Nutritional table displays 0 for all values at first', () => {

    cy.visit('http://localhost:9000/#/coach')

    cy.get("[data-test='input']").eq(0).invoke('val').should('eq', '0');
    cy.get("[data-test='input']").eq(1).invoke('val').should('eq', '0');
    cy.get("[data-test='input']").eq(2).invoke('val').should('eq', '0');
    cy.get("[data-test='input']").eq(3).invoke('val').should('eq', '0');

  })
})

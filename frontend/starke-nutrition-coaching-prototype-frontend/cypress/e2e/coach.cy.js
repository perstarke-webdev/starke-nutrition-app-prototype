describe('Coach page', () => {

  it('Header contains the correct text', () => {

    cy.visit('http://localhost:9000/#/coach')

    cy.get("[data-test='hero-heading']").contains("Starke Nutrition Coaching (Prototype)")

    cy.get("[data-test='hero-subheading']").contains("Meal-planning")

  })

  it('Nutritional table is correctly displayed at first', () => {

    cy.visit('http://localhost:9000/#/coach')

    cy.get("[data-test='hero-heading']").contains("Starke Nutrition Coaching (Prototype)")

    cy.get("[data-test='hero-subheading']").contains("Meal-planning")

  })
})

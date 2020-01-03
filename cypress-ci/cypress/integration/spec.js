describe('First Test', function() {
  it('Visits the Homepage', function() {
    cy.visit('http://localhost:5000')
    cy.contains('This is a test')
  })
})

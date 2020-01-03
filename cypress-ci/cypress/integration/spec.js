describe('My First Test', function() {
  it('Does not do much!', function() {
    expect(true).to.equal(true)
  })
})

describe('My Second Test', function() {
  it('Visits the Homepage', function() {
    cy.visit('http://localhost:5000/')
    cy.contains('This is a test')
  })
})

// describe('Another One', function() {
//   it('This should break', function() {
//     expect(true).to.equal(false)
//   })
// })

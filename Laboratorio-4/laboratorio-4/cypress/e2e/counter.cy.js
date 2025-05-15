describe('Contador funcional', () => {
  beforeEach(() => {
    cy.visit('http://localhost:5173');
  });

  it('debe incrementar correctamente', () => {
    cy.get('[data-cy="btn-increment"]').click();
    cy.get('[data-cy="count-value"]').should('contain', 'Contador: 1');
  });

  it('debe decrementar correctamente', () => {
    cy.get('[data-cy="btn-decrement"]').click();
    cy.get('[data-cy="count-value"]').should('contain', 'Contador: -1');
  });

  it('debe establecer el valor y luego usarlo como paso', () => {
    cy.get('[data-cy="input-set"]').type('5');
    cy.get('[data-cy="btn-set"]').click();
    cy.get('[data-cy="count-value"]').should('contain', 'Contador: 5');

    cy.get('[data-cy="btn-increment"]').click();
    cy.get('[data-cy="count-value"]').should('contain', 'Contador: 10');

    cy.get('[data-cy="btn-decrement"]').click();
    cy.get('[data-cy="count-value"]').should('contain', 'Contador: 5');
  });

  it('debe resetear al valor inicial', () => {
    cy.get('[data-cy="btn-reset"]').click();
    cy.get('[data-cy="count-value"]').should('contain', 'Contador: 0');
  });
});

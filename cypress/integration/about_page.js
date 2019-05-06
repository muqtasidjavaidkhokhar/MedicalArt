describe('about', function () {
    it('about', function () {
        cy.visit('http://127.0.0.1:8000/', { visitTimeout: 5000 }).then(() => {

        });
        cy.get('.current-menu-item > a').contains('Home');
        cy.get('.flex-column > :nth-child(2) > a').contains('About us');
        cy.get('.site-navigation > .flex-column > :nth-child(3) > a').contains('Services');
        cy.get('.flex-column > :nth-child(4) > a').contains('News');
        cy.get('.flex-column > :nth-child(5) > a').contains('Contact');
        cy.get('.flex-column > .call-btn > .d-flex').contains('+34 586 778 8892');
        cy.get('h1').contains('About');
        cy.get('.breadcrumbs > .d-flex > :nth-child(1) > a').contains('Home');
        cy.get('.breadcrumbs > .d-flex > :nth-child(2)').contains('About');
        cy.get('.breadcrumbs > .d-flex > :nth-child(1) > a').contains('Home');
        cy.get('.med-history > .container > .row > :nth-child(1) > h2').contains('MedArt');
        cy.get('.row > :nth-child(1) > p').contains('laoreet et quam non, viverra');
        cy.get('.d-inline-block').contains('Read');
        cy.get('.faq-stuff > .container > :nth-child(1) > :nth-child(1) > h2').contains('Faq');
        cy.get(':nth-child(1) > .professional-box > .d-flex').contains('Professional');
        cy.get(':nth-child(2) > .professional-box > .d-flex').contains('Quality');
        cy.get(':nth-child(1) > .professional-box > p').contains('Lorem ipsum dolor sit amet, cons ');
        cy.get(':nth-child(2) > .professional-box > p').contains('Lorem ipsum dolor sit amet, cons');
        cy.get('.accordion-wrap > :nth-child(1)').contains('Elit mir congue');
        cy.get('.accordion-active > p').contains('Lorem ipsum dolor');
        cy.get('.accordion-wrap > :nth-child(3)').contains('Pulvinar elit mi.');
        cy.get('.accordion-active > p').contains('Lorem ipsum dolor');
        cy.get('.accordion-wrap > :nth-child(5)').contains('Pellentesque');
        cy.get('.accordion-active > p').contains('Lorem ipsum dolor');
        cy.get('.medical-team > .container > .row > :nth-child(1) > h2').contains('The Medical');
        cy.get(':nth-child(2) > .medical-team-wrap > h4').contains('Christinne');
        cy.get('.medical-team').contains('PHD');
        cy.get(':nth-child(3) > .medical-team-wrap > h4').contains('Anna');
        cy.get('.medical-team').contains('PHD');
        cy.get(':nth-child(4) > .medical-team-wrap > h4').contains('Phillip');
        cy.get('.medical-team').contains('PHD');
        cy.get(':nth-child(5) > .medical-team-wrap > h4').contains('Gina');
        cy.get('.medical-team').contains('PHD');
        cy.get('.subscribe-banner > .container > .row > .col-12 > h2').contains('newsletter');
        cy.get('#user_subscription > .button').contains('Subscribe');
        cy.get('#email').type('medart402@gmail.com');
        cy.get('#user_subscription > .button').click();
        cy.get('.foot-about > :nth-child(2)').contains('Lorem ipsum dolor');
        cy.get('.copyright').contains('Copyright');
        cy.get('.foot-contact > h2').contains('Contact');
        cy.get('.foot-contact > .p-0 > :nth-child(1)').contains('Addtress');
        cy.get('.foot-contact > .p-0 > :nth-child(1)').contains('Mitlton');
        cy.get('.foot-contact > .p-0 > :nth-child(2)').contains('Phone');
        cy.get('.foot-contact > .p-0 > :nth-child(2)').contains('+53 345 7953 32453');
        cy.get('.foot-contact > .p-0 > :nth-child(3)').contains('Email');
        cy.get('.foot-contact > .p-0 > :nth-child(3)').contains('yourmail@gmail.com');
        cy.get('.foot-links > h2').contains('Useful');
        cy.get('.p-0 > :nth-child(1) > a').contains('Home');
        cy.get('.p-0 > :nth-child(2) > a').contains('About');
        cy.get('.p-0 > :nth-child(3) > a').contains('Departments');
        cy.get('.p-0 > :nth-child(4) > a').contains('Contact');
        cy.get('.p-0 > :nth-child(5) > a').contains('FAQ');
        cy.get('.p-0 > :nth-child(6) > a').contains('Testimonials')

    })
});

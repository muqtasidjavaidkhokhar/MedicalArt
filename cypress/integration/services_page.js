describe('services', function () {
    it('services', function () {
        cy.visit('http://127.0.0.1:8000/services').then(() => {

        });
        cy.get('.current-menu-item > a').contains('Home');
        cy.get('.flex-column > :nth-child(2) > a').contains('About us');
        cy.get('.site-navigation > .flex-column > :nth-child(3) > a').contains('Services');
        cy.get('.flex-column > :nth-child(4) > a').contains('News');
        cy.get('.flex-column > :nth-child(5) > a').contains('Contact');
        cy.get('.flex-column > .call-btn > .d-flex').contains('+34 586 778 8892');
        cy.get('h1').contains('Services');
        cy.get('.breadcrumbs > .d-flex > :nth-child(1) > a').contains('Home');
        cy.get('.breadcrumbs > .d-flex > :nth-child(2)').contains('Services');
        cy.get('.breadcrumbs > .d-flex > :nth-child(1) > a').contains('Home');
        cy.get('.quality-services > .container > :nth-child(1) > :nth-child(1) > h2').contains('Top Quality');
        cy.get('.row > :nth-child(1) > p').contains('Lorem ipsum dolor');
        cy.get('.row > :nth-child(2) > p').contains('Amet, consectetur');
        cy.get('.w-100 > .button').contains('Read');
        cy.get('.our-departments-wrap > h2').contains('Our');
        cy.get(':nth-child(1) > .our-departments-cont > .entry-header > h3').contains('Cardio');
        cy.get(':nth-child(1) > .our-departments-cont > .entry-content > p').contains('Lorem ipsum dolor sit amet');
        cy.get(':nth-child(1) > .our-departments-cont > .entry-footer > a').contains('read');
        cy.get(':nth-child(2) > .our-departments-cont > .entry-header > h3').contains('Gastro');
        cy.get(':nth-child(2) > .our-departments-cont > .entry-content > p').contains('Donec malesuada lorem');
        cy.get(':nth-child(2) > .our-departments-cont > .entry-footer > a').contains('read');
        cy.get(':nth-child(3) > .our-departments-cont > .entry-header > h3').contains('Medical');
        cy.get(':nth-child(3) > .our-departments-cont > .entry-content > p').contains('Lorem maximus mauri');
        cy.get(':nth-child(3) > .our-departments-cont > .entry-footer > a').contains('read');
        cy.get(':nth-child(4) > .our-departments-cont > .entry-header > h3').contains('Dental');
        cy.get(':nth-child(4) > .our-departments-cont > .entry-content > p').contains('Donec malesuada lorem');
        cy.get(':nth-child(4) > .our-departments-cont > .entry-footer > a').contains('read');
        cy.get(':nth-child(5) > .our-departments-cont > .entry-header > h3').contains('Surgery');
        cy.get(':nth-child(5) > .our-departments-cont > .entry-content > p').contains('maximus mauris scelerisque');
        cy.get(':nth-child(5) > .our-departments-cont > .entry-footer > a').contains('read');
        cy.get(':nth-child(6) > .our-departments-cont > .entry-header > h3').contains('Neurology');
        cy.get(':nth-child(6) > .our-departments-cont > .entry-content > p').contains('Donec malesuada lorem');
        cy.get(':nth-child(6) > .our-departments-cont > .entry-footer > a').contains('read');
        cy.get(':nth-child(7) > .our-departments-cont > .entry-header > h3').contains('Orthopaedy');
        cy.get(':nth-child(7) > .our-departments-cont > .entry-content > p').contains('Lorem maximus mauris');
        cy.get(':nth-child(7) > .our-departments-cont > .entry-footer > a').contains('read');
        cy.get(':nth-child(8) > .our-departments-cont > .entry-header > h3').contains('Pediatry');
        cy.get(':nth-child(8) > .our-departments-cont > .entry-content > p').contains('Donec malesuada lorem');
        cy.get(':nth-child(8) > .our-departments-cont > .entry-footer > a').contains('read');
        cy.get(':nth-child(9) > .our-departments-cont > .entry-header > h3').contains('Ophthal');
        cy.get(':nth-child(9) > .our-departments-cont > .entry-content > p').contains('Lorem maximus mauris');
        cy.get(':nth-child(9) > .our-departments-cont > .entry-footer > a').contains('read');
        cy.get('[data-target="#tab_1"]').contains('Pellentesque');
        cy.get('[data-target="#tab_2"]').contains('Pellentesque');
        cy.get('[data-target="#tab_3"]').contains('Consectetur');
        cy.get('[data-target="#tab_4"]').contains('CMauris');
        cy.get('[data-target="#tab_5"]').contains('Phasellus');
        cy.get('.subscribe-banner > .container > .row > .col-12 > h2').contains('newsletter');
        cy.get('#user_subscription > .button').contains('Subscribe');
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

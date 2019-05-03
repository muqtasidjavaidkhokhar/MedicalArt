describe('elements', function () {
    it('elements', function () {
        cy.visit('http://127.0.0.1:8000/elements').then(() => {

        });
        cy.get('.current-menu-item > a').contains('Home');
        cy.get('.flex-column > :nth-child(2) > a').contains('About us');
        cy.get('.site-navigation > .flex-column > :nth-child(3) > a').contains('Services');
        cy.get('.flex-column > :nth-child(4) > a').contains('News');
        cy.get('.flex-column > :nth-child(5) > a').contains('Contact');
        cy.get('.flex-column > .call-btn > .d-flex').contains('+34 586 778 8892');
        cy.get('h1').contains('Elements');
        cy.get('.breadcrumbs > .d-flex > :nth-child(1) > a').contains('Home');
        cy.get('.breadcrumbs > .d-flex > :nth-child(2)').contains('Elements');
        cy.get('.breadcrumbs > .d-flex > :nth-child(1) > a').contains('Home');
        cy.get(':nth-child(1) > .col-12 > .entry-header > .entry-title').contains('Buttons');
        cy.get('.entry-content > .gradient-bg').contains('Read');
        cy.get('.dark').contains('Read');
        cy.get('.entry-content > :nth-child(3)').contains('Read');
        cy.get(':nth-child(2) > :nth-child(2) > :nth-child(1) > .entry-header > .entry-title').contains('Accordion');
        cy.get('.accordion-wrap > :nth-child(1)').contains('Elit');
        cy.get('[data-target="#tab_1"]').contains('Pellentesque');
        cy.get('[data-target="#tab_2"]').contains('Pellentesque');
        cy.get('[data-target="#tab_3"]').contains('Consectetur');
        cy.get('[data-target="#tab_4"]').contains('CMauris');
        cy.get('[data-target="#tab_5"]').contains('Phasellus');
        cy.get(':nth-child(2) > :nth-child(3) > :nth-child(1) > .entry-header > .entry-title').contains('Loaders');
        cy.get('.offset-lg-1 > .circular-progress-bar > .entry-title').contains('Donation');
        cy.get(':nth-child(2) > .circular-progress-bar > .entry-title').contains('Ambition');
        cy.get(':nth-child(3) > .circular-progress-bar > .entry-title').contains('Good Luck');
        cy.get(':nth-child(4) > .circular-progress-bar > .entry-title').contains('High Tech');
        cy.get(':nth-child(5) > .circular-progress-bar > .entry-title').contains('Science');
        cy.get('.offset-lg-1 > .circular-progress-bar > .entry-title > span').contains('Dolor');
        cy.get(':nth-child(2) > .circular-progress-bar > .entry-title > span').contains('Sit');
        cy.get(':nth-child(3) > .circular-progress-bar > .entry-title > span').contains('Dolor');
        cy.get(':nth-child(4) > .circular-progress-bar > .entry-title > span').contains('Sit');
        cy.get(':nth-child(5) > .circular-progress-bar > .entry-title > span').contains('Dolor');
        cy.get(':nth-child(4) > :nth-child(1) > .entry-header > .entry-title').contains('Milestones');
        cy.get(':nth-child(1) > .counter-box > .entry-title').contains('Blood');
        cy.get(':nth-child(2) > .counter-box > .entry-title').contains('Patients');
        cy.get(':nth-child(3) > .counter-box > .entry-title').contains('Specialities');
        cy.get(':nth-child(4) > .counter-box > .entry-title').contains('Doctors');
        cy.get(':nth-child(5) > :nth-child(1) > .elements-heading > .entry-title').contains('Icon');
        cy.get(':nth-child(1) > .icon-box > .entry-header > .entry-title').contains('Cardiology');
        cy.get(':nth-child(1) > .icon-box > .entry-content > p').contains('Lorem ipsum');
        cy.get(':nth-child(2) > .icon-box > .entry-header > .entry-title').contains('Gastroenterology');
        cy.get(':nth-child(2) > .icon-box > .entry-content > p').contains('Donec');
        cy.get(':nth-child(3) > .icon-box > .entry-header > .entry-title').contains('Medical');
        cy.get(':nth-child(3) > .icon-box > .entry-content > p').contains('Lorem');
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

from django.test import TestCase
from django.urls import reverse
from home.models import news_subs, appointments, appoint_doctor, appoint_depart, ContactForm


class TestIndexView(TestCase):

    def test_index_view(self):
        response = self.client.get(reverse('index'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')


class TextAboutView(TestCase):

    def test_about_View(self):
        response = self.client.get(reverse('about'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/about.html')


class TestServiceVew(TestCase):

    def test_service_view(self):
        response = self.client.get(reverse('services'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/services.html')


class TestContactView(TestCase):

    def test_contact_View(self):
        response = self.client.get(reverse('contact'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/contact.html')


class TestElementView(TestCase):

    def test_elements_view(self):
        response = self.client.get(reverse('elements'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/elements.html')


class TestNewsView(TestCase):

    def test_news_view(self):
        response = self.client.get(reverse('news'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/news.html')


class TestFooterView(TestCase):

    def test_footer_view(self):
        response = self.client.get(reverse('base'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')


class EmailTest(TestCase):
    def setUp(self):
        self.mail = news_subs.objects.create(news_email='shah87061@gmail.com')
        self.url = reverse('sendmail')

    def test_send_email(self):

        response = self.client.post(self.url, data={

            'email': ['shah87061@gmail.com'],

        })
        self.assertEquals(response.status_code, 200)


class EmailTestExcpt(TestCase):

    def test_send_email(self):
        response = reverse('sendmail')

        self.client.post(response, {

            'email': [''],

        })


class TestAppointment(TestCase):

    def setUp(self):
        self.appoint = appointments.objects.create(phone_number='0300766453', patient_name='Saad')

        self.appoint_doctor = appoint_doctor.objects.create(doctor_name='Dr.Ali Shah')
        self.appoint_depart = appoint_depart.objects.create(dep_name='cardiology')
        self.url = reverse('appoint_ment')

    def test_appointments(self):
        self.client.post(self.url, data={

            'department': self.appoint_depart.id,
            'doctor': self.appoint_doctor.id,
            'phone': '0300766453',
            'name': 'Saad',

        })


class TestContactForm(TestCase):

    def setUp(self):
        self.cform = ContactForm.objects.create(name='Ali Adil', email='muqtasidjavaidkhokhar@gmail.com',
                                                subject='Testing', message='hello this is a testing mail')
        self.url = reverse('contactmessage')

    def test_contact_form(self):

        self.client.post(self.url, data={
            'name': 'Ali Adil',
            'email': 'muqtasidjavaidkhokhar@gmail.com',
            'subject': 'Testing',
            'message': 'hello this is a testing mail'
        })



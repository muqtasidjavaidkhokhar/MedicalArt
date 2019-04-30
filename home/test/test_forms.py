from django.test import TestCase
from home.forms import SendMailForm, SendMessageForm


class MailFormTest(TestCase):

    data = {
        'news_email': 'pablo@esebesoftware.com',
    }

    def test_valid_form(self):
        form = SendMailForm(self.data)
        self.assertTrue(form.is_valid())


class SendMessageTest(TestCase):

    data = {
        'name': 'ali',
        'email': 'pablo@esebesoftware.com',
        'subject': 'my name',
        'message': 'Hello This is a test'
    }

    def test_valid_contact(self):
        form = SendMessageForm(self.data)
        self.assertTrue(form.is_valid())


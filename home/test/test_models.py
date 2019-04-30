from django.test import TestCase
from ..models import index, opening_hour, emergency, our_department, patient_testimonial, the_new, news_subs, \
    appoint_depart, appoint_doctor, appointments, MedArtHistory, FaqAndStuff, FaqProQlt, MedicalTeam, ServicesTabs, \
    ContactBlock, ContactForm, Catag, LatestPost, ElementAccTab, IconBoxes, HeadFoot


class IndexTest(TestCase):

    def test_return(self):
        entry = index(slider_l_title="Medical Services")
        self.assertEqual(str(entry), entry.slider_l_title)


class OpenHourTest(TestCase):

    def test_return(self):
        entry = opening_hour(day_open="Friday")
        self.assertEqual(str(entry), entry.day_open)


class EmergencyTest(TestCase):

    def test_return(self):
        entry = emergency(emer_num="03006754876")
        self.assertEqual(str(entry), entry.emer_num)


class OurDepartmentTest(TestCase):

    def test_return(self):
        entry = our_department(dep_name="Gastroenterology")
        self.assertEqual(str(entry), entry.dep_name)


class PatientModelTest(TestCase):

    def test_return(self):
        entry = patient_testimonial(pat_name="Nina Dobrev")
        self.assertEqual(str(entry), entry.pat_name)


class TheNewTest(TestCase):

    def test_return(self):
        entry = the_new(new_title="Medical Science")
        self.assertEqual(str(entry), entry.new_title)


class NewsSubsTest(TestCase):

    def test_return(self):
        entry = news_subs(news_email="ali@gmail.com")
        self.assertEqual(str(entry), entry.news_email)


class AppointDepartTest(TestCase):

    def test_return(self):
        entry = appoint_depart(dep_name="Dental Care")
        self.assertEqual(str(entry), entry.dep_name)


class AppointDoctorTest(TestCase):

    def test_return(self):
        entry = appoint_doctor(doctor_name="Gina Smith")
        self.assertEqual(str(entry), entry.doctor_name)


class AppointmentsTest(TestCase):

    def test_return(self):
        entry = appointments(patient_name="Edward Cullen")
        self.assertEqual(str(entry), entry.patient_name)


class MedHistoryTest(TestCase):

    def test_return(self):
        entry = MedArtHistory(title="Testing")
        self.assertEqual(str(entry), entry.title)


class FaqStuffTest(TestCase):

    def test_return(self):
        entry = FaqAndStuff(title="Test Phase")
        self.assertEqual(str(entry), entry.title)


class FaqProQltTest(TestCase):

    def test_return(self):
        entry = FaqProQlt(title="Testing Phase")
        self.assertEqual(str(entry), entry.title)


class MedTeamTest(TestCase):

    def test_return(self):
        entry = MedicalTeam(title="Gina Smith")
        self.assertEqual(str(entry), entry.title)


class ServiceTabsTest(TestCase):

    def test_return(self):
        entry = ServicesTabs(title="Diabetes")
        self.assertEqual(str(entry), entry.title)


class ContactBlockTest(TestCase):

    def test_return(self):
        entry = ContactBlock(email="sultanmirza@gmail.com")
        self.assertEqual(str(entry), entry.email)


class ContactFormTest(TestCase):

    def test_return(self):
        entry = ContactForm(name="Aslam")
        self.assertEqual(str(entry), entry.name)


class CatagTest(TestCase):

    def test_return(self):
        entry = Catag(cat_name="cardiology")
        self.assertEqual(str(entry), entry.cat_name)


class LatestPostTest(TestCase):

    def test_return(self):
        entry = LatestPost(description="Medicine")
        self.assertEqual(str(entry), entry.description)


class ElementAccTabTest(TestCase):

    def test_return(self):
        entry = ElementAccTab(title="Medicine")
        self.assertEqual(str(entry), entry.title)


class IconBoxesTest(TestCase):

    def test_return(self):
        entry = IconBoxes(name="Medicine")
        self.assertEqual(str(entry), entry.name)


class HeadFootTest(TestCase):

    def test_return(self):
        entry = HeadFoot(description="MedArt")
        self.assertEqual(str(entry), entry.description)









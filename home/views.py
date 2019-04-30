from django.http import HttpResponse
from django.views.generic import TemplateView
from django.core.mail import send_mail
from .models import news_subs, appointments, ContactForm
from django.conf import settings
from django.shortcuts import render

from .models import opening_hour, index, emergency, our_department, patient_testimonial, appoint_doctor, \
    appoint_depart, HeadFoot
from .models import AboutBackImage, MedArtHistory, ServicesTabs, FaqAndStuff, FaqProQlt, MedicalTeam, ServiceBackImage, \
    TopQualityService, ContactBlock, ContactBackImage, NewBacksImage, the_new, Catag, IconBoxes, LatestPost, \
    ElementsBackImage, ElementAccTab, ElementLoader


# INDEX PAGE (MAIN PAGE)


class indexView(TemplateView):
    template_name = 'home/index.html'
    queryset = index.objects.all()
    queryset2 = opening_hour.objects.all()
    queryset3 = emergency.objects.all()
    queryset4 = our_department.objects.all()
    queryset5 = patient_testimonial.objects.all()
    queryset7 = appoint_depart.objects.all()
    queryset8 = appoint_doctor.objects.all()
    queryset9 = the_new.objects.all()

    def get_context_data(self, **kwargs):
        context = super(indexView, self).get_context_data(**kwargs)
        context['object_home'] = self.queryset
        context['hours_open'] = self.queryset2
        context['emerg'] = self.queryset3
        context['depart'] = self.queryset4
        context['pat_test'] = self.queryset5
        context['appo_depart'] = self.queryset7
        context['appo_doctor'] = self.queryset8
        context['new'] = self.queryset9
        return context


def sendmail(request):
    if request.method == 'POST':
        email = request.POST["email"]
        try:
            email = news_subs.objects.get(news_email=request.POST['email'])
            return HttpResponse({'You are already Subscribed'})
        except:
            send_mal = news_subs(news_email=email)
            send_mal.save()
            email = request.POST['email']
            from_email = settings.EMAIL_HOST_USER
            send_mail(subject='MedArt', message='Thank You for subscribing MedArt.', from_email=from_email,
                      recipient_list=[email], fail_silently=False)
            return HttpResponse({'You are Subscribed successfully'})



def appoint_ment(request):
    Name = request.POST["name"]
    Phone = request.POST["phone"]
    Doctor = request.POST["doctor"]
    Department = request.POST["department"]
    app = appointments(patient_name=Name, department_id=int(Department), doctor_id=int(Doctor), phone_number=Phone)
    app.save()

    return HttpResponse({'Your Appointment is Fixed successfully'})


# INDEX PAGE (MAIN PAGE)


class aboutView(TemplateView):
    template_name = 'home/about.html'

    def get_context_data(self, **kwargs):
        context = super(aboutView, self).get_context_data(**kwargs)
        context['about_background'] = AboutBackImage.objects.all()
        context['med_history'] = MedArtHistory.objects.all()
        context['faq_stuff'] = FaqAndStuff.objects.all()
        context['Pro_Qlt'] = FaqProQlt.objects.all()
        context['medical_team'] = MedicalTeam.objects.all()

        return context


class serviceView(TemplateView):
    template_name = 'home/services.html'

    def get_context_data(self, **kwargs):
        context = super(serviceView, self).get_context_data(**kwargs)
        context['service_background'] = ServiceBackImage.objects.all()
        context['top_quality_service'] = TopQualityService.objects.all()
        context['depart'] = our_department.objects.all()
        context['service_tab'] = ServicesTabs.objects.all()

        return context


class contactView(TemplateView):
    template_name = 'home/contact.html'

    def get_context_data(self, **kwargs):
        context = super(contactView, self).get_context_data(**kwargs)
        context['hours_open'] = opening_hour.objects.all()
        context['emerg'] = emergency.objects.all()
        context['contact_block'] = ContactBlock.objects.all()
        context['contact_back_image'] = ContactBackImage.objects.all()

        return context


def contactmessage(request):
    name = request.POST["name"]
    email = request.POST["email"]
    subject = request.POST["subject"]
    message = request.POST["message"]
    send_mal = ContactForm(email=email, name=name, subject=subject, message=message)
    send_mal.save()

    if request.method == 'POST':
        name = request.POST["name"]
        email = request.POST["email"]
        subject = request.POST["subject"]
        message = request.POST["message"]
        from_email = settings.EMAIL_HOST_USER
        send_mail(subject=subject, message=message, from_email=from_email,
                  recipient_list=[email], fail_silently=False)
    return HttpResponse({'Your Message is sent Successfully. We will contact you soon. Thank you'})


class elementView(TemplateView):
    template_name = 'home/elements.html'

    def get_context_data(self, **kwargs):
        context = super(elementView, self).get_context_data(**kwargs)
        context['elements_back_image'] = ElementsBackImage.objects.all()
        context['elements_acc_tab'] = ElementAccTab.objects.all()
        context['service_tab'] = ServicesTabs.objects.all()
        context['element_loader'] = ElementLoader.objects.all()
        context['icon_box'] = IconBoxes.objects.all()

        return context


class newsView(TemplateView):
    template_name = 'home/news.html'

    def get_context_data(self, **kwargs):
        context = super(newsView, self).get_context_data(**kwargs)
        context['new_back_image'] = NewBacksImage.objects.all()
        context['new'] = the_new.objects.all()
        context['hours_open'] = opening_hour.objects.all()
        context['emerg'] = emergency.objects.all()
        context['categories'] = Catag.objects.all()
        context['latest_post'] = LatestPost.objects.all()

        return context


class footerView(TemplateView):
    template_name = 'base.html'

    def get_context_data(self, **kwargs):
        context = super(footerView, self).get_context_data(**kwargs)
        context['head_foot'] = HeadFoot.objects.all()

        return context

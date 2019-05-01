from django.contrib import admin

# Register your models here.
from .models import opening_hour, index, the_new, HeadFoot, ContactBlock, IconBoxes, ElementLoader, ElementAccTab, LatestPost, Catag, ElementsBackImage, NewBacksImage, ContactBackImage, ContactForm, ServicesTabs, FaqAndStuff, ServiceBackImage, TopQualityService, MedicalTeam, FaqProQlt, emergency, MedArtHistory,  our_department, patient_testimonial, news_subs, appoint_depart, appoint_doctor, appointments, AboutBackImage
admin.site.register(index)
admin.site.register(opening_hour)
admin.site.register(emergency)
admin.site.register(our_department)
admin.site.register(patient_testimonial)
admin.site.register(news_subs)
admin.site.register(appoint_depart)
admin.site.register(appoint_doctor)
admin.site.register(appointments)
admin.site.register(AboutBackImage)
admin.site.register(MedArtHistory)
admin.site.register(FaqAndStuff)
admin.site.register(FaqProQlt)
admin.site.register(MedicalTeam)
admin.site.register(ServiceBackImage)
admin.site.register(TopQualityService)
admin.site.register(ServicesTabs)
admin.site.register(ContactBlock)
admin.site.register(ContactForm)
admin.site.register(ContactBackImage)
admin.site.register(NewBacksImage)
admin.site.register(the_new)
admin.site.register(Catag)
admin.site.register(LatestPost)
admin.site.register(ElementsBackImage)
admin.site.register(ElementAccTab)
admin.site.register(ElementLoader)
admin.site.register(IconBoxes)
admin.site.register(HeadFoot)
































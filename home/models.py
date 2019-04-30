from django.db import models


# Create your models here.
class index(models.Model):

    slider_image = models.ImageField(upload_to='images/')
    slider_u_title = models.CharField(max_length=200)
    slider_l_title = models.CharField(max_length=200)
    slider_description = models.TextField()

    def __str__(self):
        return self.slider_l_title


class opening_hour(models.Model):

    day_open = models.CharField(max_length=200)
    time_open = models.CharField(max_length=200)

    def __str__(self):
        return self.day_open


class emergency(models.Model):

    emer_num = models.CharField(max_length=200)
    emer_descrip = models.CharField(max_length=200)

    def __str__(self):
        return self.emer_num


class our_department(models.Model):

    dep_name = models.CharField(max_length=200)
    dep_description = models.TextField()
    dep_image = models.ImageField(upload_to='images/')

    def __str__(self):

        return self.dep_name


class patient_testimonial(models.Model):

    pat_description = models.TextField()
    pat_image = models.ImageField(upload_to='images/')
    pat_name = models.CharField(max_length=200)
    pat_address = models.TextField()

    def __str__(self):
        return self.pat_name


class the_new(models.Model):
    new_image = models.ImageField(upload_to='images/')
    new_title = models.CharField(max_length=200)
    new_date = models.CharField(max_length=200)
    new_by_name = models.CharField(max_length=200)
    new_description = models.TextField()
    new_no_comments = models.CharField(max_length=200)

    def __str__(self):
        return self.new_title


class news_subs(models.Model):

    news_email = models.EmailField(max_length=120)
    news_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.news_email


class appoint_depart(models.Model):

    dep_name = models.CharField(max_length=200)

    def __str__(self):
        return self.dep_name


class appoint_doctor(models.Model):

    doctor_name = models.CharField(max_length=200)

    def __str__(self):
        return self.doctor_name


class appointments(models.Model):

    department = models.ForeignKey(appoint_depart, on_delete=models.CASCADE, max_length=200, null=True, blank=True)
    doctor = models.ForeignKey(appoint_doctor, on_delete=models.CASCADE, max_length=200, null=True, blank=True)
    patient_name = models.CharField(max_length=200, null=True, blank=True)
    phone_number = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return "{}".format(self.patient_name)


class AboutBackImage(models.Model):

    image = models.ImageField(upload_to='images/')


class MedArtHistory(models.Model):

    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title


class FaqAndStuff(models.Model):

    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title


class FaqProQlt(models.Model):

    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title


class MedicalTeam(models.Model):

    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=200)
    qualification = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class ServiceBackImage(models.Model):

    image = models.ImageField(upload_to='images/')


class TopQualityService(models.Model):

    description = models.TextField()


class ServicesTabs(models.Model):

    title = models.CharField(max_length=200)
    tab_title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')
    description = models.TextField()

    def __str__(self):
        return self.title


class ContactBlock(models.Model):

    address = models.CharField(max_length=400)
    phone = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=120)

    def __str__(self):
        return self.email


class ContactForm(models.Model):

    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.name


class ContactBackImage(models.Model):

    image = models.ImageField(upload_to='images/')


class NewBacksImage(models.Model):

    image = models.ImageField(upload_to='images/')


class Catag(models.Model):

    cat_name = models.CharField(max_length=200)

    def __str__(self):
        return self.cat_name


class LatestPost(models.Model):

    image = models.ImageField(upload_to='images/')
    description = models.TextField()
    date = models.CharField(max_length=200)

    def __str__(self):
        return self.description


class ElementsBackImage(models.Model):

    image = models.ImageField(upload_to='images/')


class ElementAccTab(models.Model):

    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title


class ElementLoader(models.Model):

    title = models.CharField(max_length=200)
    description = models.TextField()


class IconBoxes(models.Model):

    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')
    description = models.TextField()

    def __str__(self):
        return self.name


class HeadFoot(models.Model):

    icon = models.ImageField(upload_to='images/')
    description = models.TextField()

    def __str__(self):
        return self.description



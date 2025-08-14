from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from googletrans import Translator
from transliterate import translit

# Initialize translator
translator = Translator()

class OurTeam(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='Images/team/')
    position = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        # Auto-translate name and positon, description if not provided
        if self.name and not self.name_ru:
            self.name_ru = translit(self.name, 'ru')
        if self.position_uz and not self.position_en:
            self.position_en = translator.translate(self.position_uz, src='uz', dest='en').text
        if self.position_uz and not self.position_ru:
            self.position_ru = translator.translate(self.position_uz, src='uz', dest='ru').text
        if self.description_uz and not self.description_en:
            self.description_en = translator.translate(self.description_uz, src='uz', dest='en').text
        if self.description_uz and not self.description_ru:
            self.description_ru = translator.translate(self.description_uz, src='uz', dest='ru').text
        super().save(*args, **kwargs)


class ContactUs(models.Model):
    full_name = models.CharField(max_length=50)
    phone_number = models.IntegerField()
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.full_name
    
    def save(self, *args, **kwargs):
        # Auto-translate name and positon, description if not provided
        if self.message_uz and not self.message_en:
            self.message_en = translator.translate(self.message_uz, src='uz', dest='en').text
        if self.message_uz and not self.message_ru:
            self.message_ru = translator.translate(self.message_uz, src='uz', dest='ru').text

        super().save(*args, **kwargs)

class Services(models.Model):
    SERVICE_CHOICES = [
        ('mobile_app', 'Mobile app'),
        ('web_site', 'Web site'),
        ('crm', 'CRM'),
        ('telegram_bot', 'Telegram bot'),
        ('','')
    ]

    name = models.CharField(max_length=50, choices=SERVICE_CHOICES)
    image = models.ImageField(upload_to='Images/services/')
    description = models.TextField()

    def __str__(self):
        return self.get_name_display()
    
    def save(self, *args, **kwargs):
        if self.name and not self.name_ru:
            self.name_ru = translit(self.name, 'ru')
        if self.description_uz and not self.description_en:
            self.description_en = translator.translate(self.description_uz, src='uz', dest='en').text
        if self.description_uz and not self.description_ru:
            self.description_ru = translator.translate(self.description_uz, src='uz', dest='ru').text
        super().save(*args, **kwargs)


class ServicesDetails(models.Model):
    Company_nomi = models.CharField(max_length=50)
    phone_number = PhoneNumberField()
    service_type = models.ForeignKey(Services, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        # Auto-translate name and positon, description if not provided
        if self.name_uz and not self.name_en:
            self.name_en = translator.translate(self.name_uz, src='uz', dest='en').text
        if self.name_uz and not self.name_ru:
            self.name_ru = translator.translate(self.name_uz, src='uz', dest='ru').text
        if self.description_uz and not self.description_en:
            self.description_en = translator.translate(self.description_uz, src='uz', dest='en').text
        if self.description_uz and not self.description_ru:
            self.description_ru = translator.translate(self.description_uz, src='uz', dest='ru').text
        super().save(*args, **kwargs)



class Feature(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # Auto-translate name and positon, description if not provided
        if self.name_uz and not self.name_en:
            self.name_en = translator.translate(self.name_uz, src='uz', dest='en').text
        if self.name_uz and not self.name_ru:
            self.name_ru = translator.translate(self.name_uz, src='uz', dest='ru').text
        super().save(*args, **kwargs)


class Portfolio(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/portfolio/', blank=True, null=True)
    description = models.TextField(blank=True)
    proect_type = models.ForeignKey(Services,on_delete=models.CASCADE)
    proect_link = models.URLField(blank=True, null=True)
    tehnalogiyalari = models.CharField(max_length=200, blank=True)
    view_count = models.IntegerField(default=0)
    like_count = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        # Auto-translate name and positon, description if not provided
        if self.name_uz and not self.name_en:
            self.name_en = translator.translate(self.name_uz, src='uz', dest='en').text
        if self.name_uz and not self.name_ru:
            self.name_ru = translator.translate(self.name_uz, src='uz', dest='ru').text
        if self.tehnalogiyalari_uz and not self.tehnalogiyalari_en:
            self.tehnalogiyalari_en = translator.translate(self.tehnalogiyalari_uz, src='uz', dest='en').text
        if self.tehnalogiyalari_uz and not self.tehnalogiyalari_ru:
            self.tehnalogiyalari_ru = translator.translate(self.tehnalogiyalari_uz, src='uz', dest='ru').text
        if self.description_uz and not self.description_en:
            self.description_en = translator.translate(self.description_uz, src='uz', dest='en').text
        if self.description_uz and not self.description_ru:
            self.description_ru = translator.translate(self.description_uz, src='uz', dest='ru').text
        super().save(*args, **kwargs)
    


class ImagesPortfolio(models.Model):
    portfolio = models.ForeignKey(Portfolio, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/portfolio/')

    def __str__(self):
        return f"Image for {self.portfolio.name}"

class Blog(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='Images/blog/')
    description = models.TextField()
    # blog_link = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        # Auto-translate name and positon, description if not provided
        if self.name_uz and not self.name_en:
            self.name_en = translator.translate(self.name_uz, src='uz', dest='en').text
        if self.name_uz and not self.name_ru:
            self.name_ru = translator.translate(self.name_uz, src='uz', dest='ru').text
        if self.description_uz and not self.description_en:
            self.description_en = translator.translate(self.description_uz, src='uz', dest='en').text
        if self.description_uz and not self.description_ru:
            self.description_ru = translator.translate(self.description_uz, src='uz', dest='ru').text
        super().save(*args, **kwargs)



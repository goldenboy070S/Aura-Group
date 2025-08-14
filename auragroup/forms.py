from django import forms
from django.forms import ModelForm
from .models import ContactUs
from django import forms
from .models import ServicesDetails
from django.utils.translation import gettext_lazy as _

class ContactForm(ModelForm):
    class Meta:
        model = ContactUs
        fields = ["full_name", "phone_number", "email", "message"]
        widgets = {
            "full_name": forms.TextInput(attrs={
                "class": "bg-[#333344] h-10 rounded-lg mt-1 px-4"
            }),
            "phone_number": forms.TextInput(attrs={
                "class": "bg-[#333344] h-10 rounded-lg mt-1 px-4"
            }),
            "email": forms.EmailInput(attrs={
                "class": "bg-[#333344] h-10 rounded-lg mt-1 px-4"
            }),
            "message": forms.Textarea(attrs={
                "class": "bg-[#333344] rounded-lg mt-1 px-4 py-2"
            }),
        }



class ServicesDetailsForm(forms.ModelForm):
    class Meta:
        model = ServicesDetails
        fields = ['Company_nomi', 'phone_number', 'service_type', 'name', 'description']
        labels = {
            'Company_nomi': _("Kompaniya nomi"),
            'phone_number': _("Telefon raqami"),
            'service_type': _("Xizmat turi"),
            'name': _("Ism"),
            'description': _("Tavsif"),
        }
        widgets = {
            'Company_nomi': forms.TextInput(attrs={
                'class': 'bg-[#09101E] p-2 rounded-lg mb-4 w-full',
                'placeholder': _('Kompaniya nomini kiriting')
            }),
            'phone_number': forms.TextInput(attrs={
                'class': 'bg-[#09101E] p-2 rounded-lg mb-4 w-full',
                'placeholder': _('+998')
            }),
            'service_type': forms.Select(attrs={
                'class': 'bg-[#09101E] p-2 rounded-lg w-full'
            }),
            'name': forms.TextInput(attrs={
                'class': 'bg-[#09101E] p-2 rounded-lg w-full',
                'placeholder': _('Ismingizni kiriting')
            }),
            'description': forms.Textarea(attrs={
                'class': 'bg-[#09101E] p-2 rounded-lg w-full',
                'placeholder': _('Loyihangizni tavsiflang...'),
                'rows': 4
            }),
        }
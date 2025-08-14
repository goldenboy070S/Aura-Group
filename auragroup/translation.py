from modeltranslation.translator import register, TranslationOptions
from .models import (
    OurTeam, ContactUs, Services, ServicesDetails,
    Feature, Portfolio, ImagesPortfolio, Blog
)

@register(OurTeam)
class OurTeamTranslationOptions(TranslationOptions):
    fields = ('name', 'position', 'description')



@register(ContactUs)
class ContactUsTranslationOptions(TranslationOptions):
    fields = ('message',)



@register(Services)
class ServicesTranslationOptions(TranslationOptions):
    fields = ('name', 'description')



@register(ServicesDetails)
class ServicesDetailsTranslationOptions(TranslationOptions):
    fields = ('Company_nomi', 'name', 'description')


@register(Feature)
class FeatureTranslationOptions(TranslationOptions):
    fields = ('name',)


# --- Portfolio ---
@register(Portfolio)
class PortfolioTranslationOptions(TranslationOptions):
    fields = ('name', 'description', 'proect_type', 'tehnalogiyalari')



@register(Blog)
class BlogTranslationOptions(TranslationOptions):
    fields = ('name', 'description')
